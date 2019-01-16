function norm_name(n) {
    var last,firsts;
    if (n.includes(",")) {
	comma_idx=n.indexOf(",");
	last=n.slice(0,comma_idx);
	firsts=n.slice(comma_idx+1);
    }
    else if (n.includes(" ")) {
	space_idx=n.lastIndexOf(" ");
	firsts=n.slice(0,space_idx);
	last=n.slice(space_idx+1);
    }
    else {
	firsts="";
	last=n;
    }
    firsts=firsts.trim();
    last=last.trim();
    first_parts=firsts.split(/[ -]+/);
    abbrv="";
    for (idx in first_parts) {
	abbrv+=first_parts[idx][0];
    }
    if (abbrv) {
	abbrv+=". ";
    }
    return abbrv+last;
}
    
function norm_names(n) {
    var ns=n.split(/ +and +/);
    var norm_names=[];
    for (idx in ns) {
	norm_names.push(norm_name(ns[idx]));
    }
    return norm_names.join(" & ");
}

bibrepo="TurkuNLP/list-of-publications";
bibbranch="master";
bibfile="turkunlp.bib";
bibraw_url="https://raw.githubusercontent.com/"+bibrepo+"/"+bibbranch+"/"+bibfile;
bibpretty_url="https://github.com/"+bibrepo+"/blob/"+bibbranch+"/"+bibfile;



xmlhttp=new XMLHttpRequest();
xmlhttp.open("GET", bibraw_url, false);
xmlhttp.send();
var entries = BibtexParser(xmlhttp.responseText);
var mytable="<thead><tr><th>Author</th><th>Title</th><th>Year</th><th>Forum</th><th>Type</th><th>Links</th><th>URL</th></tr></thead>\n<tbody>\n";

for (eidx in entries["entries"]) {
    var e=entries["entries"][eidx];
    var fields=e["Fields"];
    if (fields["author"]) {
	auth=fields["author"];
    } else if (fields["editor"]) {
	auth=fields["editor"];
    }
    else {
	auth="";
    }
    if (fields["booktitle"]) {
	forum=fields["booktitle"];
    }
    else if (fields["journal"]) {
	forum=fields["journal"];
    }
    else {
	forum="";
    }
    if (fields["url"]) {
	url=fields["url"];
    url='<a href="'+url+'">URL</a>';
    }
    else {
    url="";
    }

    link='<a href="'+bibpretty_url+'#L'+e["lineno"]+'">BibTeX</a>';
    mytable+="<tr><td>"+norm_names(auth)+"</td><td>"+fields["title"]+"</td><td>"+fields["year"]+"</td><td>"+forum+"</td><td>"+e["EntryType"]+"</td><td>"+link+"</td><td>"+url+"</td></tr>\n";
}
mytable+="</tbody>";
$("#pubtable").html(mytable)
