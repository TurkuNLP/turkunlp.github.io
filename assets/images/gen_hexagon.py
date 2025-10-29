#!/usr/bin/env python3
"""
Hexagon Honeycomb Face Composition Generator

This script creates a honeycomb-like layout of hexagonal tiles from square face images.
Each face image is converted to a hexagonal tile and arranged in a configurable grid.
"""

import argparse
import math
import os
import re
import sys
from typing import List, Tuple, Optional
from PIL import Image, ImageDraw
import numpy as np
import cv2

# Global face detector cache
_face_detector = None


def get_face_detector():
    """Get or initialize the face detector."""
    global _face_detector
    if _face_detector is None:
        # Try to load haarcascade from OpenCV data directory
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        _face_detector = cv2.CascadeClassifier(cascade_path)
        if _face_detector.empty():
            print("Warning: Face detector not loaded, face centering will be disabled")
    return _face_detector


def detect_face_center(image: Image.Image, filename: Optional[str] = None) -> Optional[Tuple[int, int]]:
    """
    Detect face in image and return its center coordinates.
    
    Args:
        image: PIL Image
        filename: Optional filename for error messages
        
    Returns:
        Tuple (center_x, center_y) or None if no face detected
    """
    detector = get_face_detector()
    if detector is None or detector.empty():
        return None
    
    # Convert PIL to OpenCV format
    img_array = np.array(image)
    if image.mode == 'RGBA':
        # Convert RGBA to RGB
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGBA2RGB)
    elif image.mode != 'RGB':
        img_array = np.array(image.convert('RGB'))
    
    # Convert to grayscale for face detection
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    
    # Detect faces
    faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))
    
    if len(faces) == 0:
        if filename:
            print(f"No face detected in {filename}", file=sys.stderr)
        else:
            print("No face detected", file=sys.stderr)
        return None
    
    # Use the largest face if multiple detected
    largest_face = max(faces, key=lambda f: f[2] * f[3])
    x, y, w, h = largest_face
    
    # Calculate center
    center_x = x + w // 2
    center_y = y + h // 2
    
    return (center_x, center_y)


def create_hexagonal_tile(image: Image.Image, tile_width: int, border_width: int = 5, 
                         border_color: str = 'white', center_on_face: bool = True, 
                         filename: Optional[str] = None) -> Image.Image:
    """
    Convert a square image to a hexagonal tile with transparent background.
    
    Args:
        image: Input square image (PIL Image)
        tile_width: Width of the hexagonal tile in pixels
        border_width: Width of the border around the hexagon
        border_color: Color of the border
        center_on_face: If True, detect face and center crop on it
        filename: Optional filename for face detection error messages
        
    Returns:
        PIL Image with hexagonal tile on transparent background
    """
    # Calculate hexagon dimensions
    hex_radius = tile_width // 2
    hex_height = int(hex_radius * math.sqrt(3))
    
    # Create output image with transparent background
    output_size = (tile_width + 2 * border_width, hex_height + 2 * border_width)
    output = Image.new('RGBA', output_size, (0, 0, 0, 0))
    
    # Crop to square - center on face if requested and face is detected
    size = min(image.size)
    if center_on_face:
        face_center = detect_face_center(image, filename)
        if face_center is not None:
            # Center the square crop on the face
            center_x, center_y = face_center
            half_size = size // 2
            
            # Calculate crop boundaries centered on face
            left = center_x - half_size
            top = center_y - half_size
            right = left + size
            bottom = top + size
            
            # Adjust if crop extends beyond image boundaries
            if left < 0:
                right += -left
                left = 0
            if top < 0:
                bottom += -top
                top = 0
            if right > image.width:
                left -= (right - image.width)
                right = image.width
            if bottom > image.height:
                top -= (bottom - image.height)
                bottom = image.height
            
            # Ensure we don't go negative after adjustments
            left = max(0, left)
            top = max(0, top)
            
            image = image.crop((left, top, left + size, top + size))
        else:
            # Fall back to default crop
            image = image.crop((0, 0, size, size))
    else:
        # Default crop from top-left
        image = image.crop((0, 0, size, size))
    
    # Resize to tile size
    image = image.resize((tile_width, tile_width), Image.Resampling.LANCZOS)
    
    # Create mask for hexagon shape
    mask = Image.new('L', (tile_width, tile_width), 0)
    draw_mask = ImageDraw.Draw(mask)
    
    # Calculate hexagon vertices
    center_x, center_y = tile_width // 2, tile_width // 2
    vertices = []
    for i in range(6):
        angle = math.pi / 3 * i
        x = center_x + hex_radius * math.cos(angle)
        y = center_y + hex_radius * math.sin(angle)
        vertices.append((x, y))
    
    # Draw hexagon mask
    draw_mask.polygon(vertices, fill=255)
    
    # Apply mask to image
    image.putalpha(mask)
    
    # Paste image onto output with border offset
    output.paste(image, (border_width, border_width), image)
    
    # Draw border if specified
    if border_width > 0:
        draw = ImageDraw.Draw(output)
        # Calculate border hexagon vertices
        border_vertices = []
        for i in range(6):
            angle = math.pi / 3 * i
            x = center_x + border_width + hex_radius * math.cos(angle)
            y = center_y + border_width + hex_radius * math.sin(angle)
            border_vertices.append((x, y))
        
        # Draw border
        draw.polygon(border_vertices, outline=border_color, width=border_width)
    
    return output


def get_content_bbox(image: Image.Image) -> Tuple[int, int, int, int]:
    """
    Get bounding box of non-transparent content in RGBA image.
    
    Args:
        image: PIL Image with alpha channel
        
    Returns:
        Tuple (left, top, right, bottom) bounding box
    """
    # Convert to numpy array for efficient processing
    img_array = np.array(image)
    
    # Find all pixels with non-zero alpha
    alpha_channel = img_array[:, :, 3]
    non_transparent = np.where(alpha_channel > 0)
    
    if len(non_transparent[0]) == 0:
        # No content, return image bounds
        return (0, 0, image.width, image.height)
    
    # Get bounding box coordinates
    top = int(non_transparent[0].min())
    bottom = int(non_transparent[0].max()) + 1
    left = int(non_transparent[1].min())
    right = int(non_transparent[1].max()) + 1
    
    return (left, top, right, bottom)


def layout_hexagonal_tiles(tile_rows: List[List[Image.Image]], tile_width: int) -> Image.Image:
    """
    Layout hexagonal tiles in rows to create a proper honeycomb pattern.
    
    Args:
        tile_rows: List of lists, where each inner list contains tiles for one row
        tile_width: Width of each tile
        
    Returns:
        Final composed image (cropped to content bounding box)
    """
    if not tile_rows or not tile_rows[0]:
        raise ValueError("No tiles provided")
    
    # Calculate hexagonal dimensions
    hex_radius = tile_width // 2
    hex_height = int(hex_radius * math.sqrt(3))  # Height of hexagon
    tile_height = hex_height + 2 * 5  # Total tile height including border
    
    # Proper honeycomb spacing:
    # Even rows (0, 2, 4, ...) start at left margin
    # Odd rows (1, 3, 5, ...) are shifted to the right
    # Horizontal spacing: tile_width + space for interlocking tile's upper edge
    # Vertical spacing: smaller for interlocking
    horizontal_spacing = int(tile_width * 1.5)-1  # Space for interlocking tile's upper edge
    vertical_spacing = int(hex_height/2)-1  # Smaller vertical spacing for interlocking
    row_offset = (tile_width * 0.75)  # Half tile width + half of horizontal edge
    
    # Calculate total dimensions
    max_tiles_per_row = max(len(row) for row in tile_rows)
    
    # Calculate canvas size - need to account for tile dimensions
    total_width = int(max_tiles_per_row * horizontal_spacing + row_offset + tile_width)
    total_height = int(len(tile_rows) * vertical_spacing + tile_height)
    
    # Create output image
    output = Image.new('RGBA', (total_width, total_height), (0, 0, 0, 0))
    
    # Place tiles in honeycomb pattern
    for row_idx, row in enumerate(tile_rows):
        for col_idx, tile in enumerate(row):
            # Calculate base position
            x = int(col_idx * horizontal_spacing)
            y = int(row_idx * vertical_spacing)
            
            # Apply honeycomb offset for odd rows
            if row_idx % 2 == 1:
                x += int(row_offset)
            
            # Paste tile
            output.paste(tile, (x, y), tile)
    
    # Crop to actual content bounding box
    bbox = get_content_bbox(output)
    output = output.crop(bbox)
    
    return output


def extract_images_from_markdown(markdown_path: str) -> List[str]:
    """
    Extract image paths from markdown file using regex to find <img src="..."> tags.
    
    Args:
        markdown_path: Path to the markdown file
        
    Returns:
        List of image paths in the order they appear in the markdown file
    """
    try:
        with open(markdown_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Markdown file '{markdown_path}' not found")
        return []
    except Exception as e:
        print(f"Error reading markdown file: {e}")
        return []
    
    # Regex pattern to match <img src="path" ...> tags
    # This will capture the src attribute value
    img_pattern = r'<img[^>]*src=["\']([^"\']+)["\'][^>]*>'
    
    matches = re.findall(img_pattern, content, re.IGNORECASE)
    
    if not matches:
        print("No <img> tags found in the markdown file")
        return []
    
    print(f"Found {len(matches)} image references in markdown file")
    return matches


def organize_images_into_rows(image_paths: List[str], num_columns: int) -> List[List[str]]:
    """
    Organize image paths into rows with alternating sizes.
    Even rows (0,2,4...) have num_columns images.
    Odd rows (1,3,5...) have num_columns-1 images.
    
    Args:
        image_paths: List of paths to input images
        num_columns: Number of columns for even rows
        
    Returns:
        List of lists, where each inner list contains image paths for one row
    """
    rows = []
    i = 0
    row_idx = 0
    
    while i < len(image_paths):
        if row_idx % 2 == 0:
            # Even rows: num_columns images
            row_size = num_columns
        else:
            # Odd rows: num_columns-1 images
            row_size = num_columns - 1
        
        row = image_paths[i:i + row_size]
        rows.append(row)
        i += row_size
        row_idx += 1
    
    return rows


def main():
    """Main function to run the hexagon honeycomb generator."""
    parser = argparse.ArgumentParser(description='Generate hexagon honeycomb from face images in markdown file')
    parser.add_argument('markdown_file', help='Markdown file containing <img> tags with image references')
    parser.add_argument('output_path', help='Output path for the final composition')
    parser.add_argument('--columns', type=int, default=2, help='Number of columns (default: 2)')
    parser.add_argument('--tile-width', type=int, default=100, help='Width of each tile in pixels (default: 100)')
    parser.add_argument('--border-width', type=int, default=5, help='Border width in pixels (default: 5)')
    parser.add_argument('--border-color', default='gray', help='Border color (default: gray)')
    parser.add_argument('--background-color', default='black', help='Background color for the composition (default: black)')
    parser.add_argument('--no-center-on-face', dest='center_on_face', action='store_false', default=True, help='Disable face centering (default: face centering enabled)')
    
    args = parser.parse_args()
    
    # Extract image paths from markdown file
    image_paths = extract_images_from_markdown(args.markdown_file)
    image_paths=[os.path.basename(path) for path in image_paths]
    
    if not image_paths:
        print(f"No image references found in {args.markdown_file}")
        return
    
    print(f"Found {len(image_paths)} images")
    print(f"Organizing into {args.columns} columns")
    
    # Organize images into rows
    image_rows = organize_images_into_rows(image_paths, args.columns)
    
    # Process each image into hexagonal tiles
    tile_rows = []
    for row_idx, row_paths in enumerate(image_rows):
        print(f"Processing row {row_idx + 1}/{len(image_rows)}")
        tile_row = []
        for path in row_paths:
            try:
                image = Image.open(path)
                tile = create_hexagonal_tile(
                    image, 
                    args.tile_width, 
                    args.border_width, 
                    args.border_color,
                    args.center_on_face,
                    path
                )
                tile_row.append(tile)
            except Exception as e:
                print(f"Error processing {path}: {e}")
                continue
        tile_rows.append(tile_row)
    
    # Layout tiles into final composition
    print("Creating final composition...")
    final_image = layout_hexagonal_tiles(tile_rows, args.tile_width)
    
    # Save result
    # Handle different output formats
    output_ext = os.path.splitext(args.output_path)[1].lower()
    
    if output_ext in ['.jpg', '.jpeg']:
        # Convert RGBA to RGB with specified background for JPEG
        rgb_image = Image.new('RGB', final_image.size, args.background_color)
        rgb_image.paste(final_image, mask=final_image.split()[-1])  # Use alpha channel as mask
        rgb_image.save(args.output_path)
    else:
        # For PNG and other formats, add background if specified
        if args.background_color != 'transparent':
            # Create background and composite the image
            background = Image.new('RGB', final_image.size, args.background_color)
            background.paste(final_image, mask=final_image.split()[-1])
            background.save(args.output_path)
        else:
            # Save with transparency
            final_image.save(args.output_path)
    
    print(f"Composition saved to {args.output_path}")


if __name__ == "__main__":
    main()
