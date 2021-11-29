---
title: Textual paraphrase dataset for deep language modeling
layout: page
---

The project gathered a large dataset of Finnish paraphrase pairs (over 100,000) accompanied by a small test set of Swedish paraphrases. The paraphrases are selected and classified manually, so as to minimize lexical overlap, and provide examples that are maximally structurally and lexically different. The objective is to create a dataset which is challenging and better tests the capabilities of natural language understanding. An important feature of the data is that most paraphrase pairs are distributed in their document context. The primary application for the dataset is the development and evaluation of deep language models, and representation learning in general. The project is funded by the [European Language Grid](https://www.european-language-grid.eu/expo-projects/textual-paraphrase-dataset-for-deep-language-modeling/) (2020-2021) and the Academy of Finland (2021-2023).

## Data and model download

* The full manually **annotated dataset** is on [GitHub](https://github.com/TurkuNLP/Turku-paraphrase-corpus) and the [European Language Grid](https://live.european-language-grid.eu/catalogue/corpus/7754)
* A **model** trained on this data to classify text segment pairs into the various classes of paraphrase is documented and downloadble in the following notebook [[GitHub]](https://github.com/TurkuNLP/Turku-paraphrase-models/blob/main/para_notebook.ipynb) [[Colab]](https://colab.research.google.com/github/TurkuNLP/Turku-paraphrase-models/blob/main/para_notebook.ipynb)
* A collection of **paraphrase candidates** (500K positive and 5M negative) gathered using the above model and useful for further training in a straightforward classification setup is [downloadable here](http://dl.turkunlp.org/turku-paraphrase/pos-neg-candidates/)
* Finnish **SentenceBERT** models fine-tuned on the data are available for download [here](http://dl.turkunlp.org/finnish-sbert/). They can also be accessed using Huggingface with the model names [TurkuNLP/sbert-cased-finnish-paraphrase](https://huggingface.co/TurkuNLP/sbert-cased-finnish-paraphrase) and [TurkuNLP/sbert-uncased-finnish-paraphrase](https://huggingface.co/TurkuNLP/sbert-uncased-finnish-paraphrase), where example code snippets are provided. Check out the [DEMO](http://epsilon-it.utu.fi/sbert400m).

## Documentation and publications

* An initial release of the data is described in [this Nodalida'21 paper](https://aclanthology.org/2021.nodalida-main.29/)
* The annotation guidelines of the data are [on arxiv](https://arxiv.org/abs/2108.07499)
* The data files are documented in the README file of the [data release](https://github.com/TurkuNLP/Turku-paraphrase-corpus)
* <a href="assets/files/paraphrase-poster.pdf">Project poster</a>

## Annotation tools and other software

* Annotation tools: [candidate selection](https://github.com/TurkuNLP/pick-para-anno), [candidate annotation](https://github.com/TurkuNLP/rew-para-anno), [statistics](https://github.com/TurkuNLP/stats-para-anno)

## How to cite?

J. Kanerva & F. Ginter & LH. Chang & I. Rastas & V. Skantsi & HM. Kupari & J. Kilpeläinen & J. Saarni & M. Sevón & O. Tarkka. 2021. *Finnish Paraphrase Corpus.*  Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa 2021) pp. 288-298.

```
@inproceedings{kanerva-etal-2021-finnish,
    title = "{F}innish Paraphrase Corpus",
    author = {Kanerva, Jenna and Ginter, Filip and Chang, Li-Hsin and Rastas, 
    Iiro and Skantsi, Valtteri and Kilpel{\"a}inen, Jemina and Kupari, Hanna-Mari and 
    Saarni, Jenna and Sev{\'o}n, Maija and Tarkka, Otto},
    booktitle = "Proceedings of the 23rd Nordic Conference on Computational Linguistics (NoDaLiDa'21)",
    year = "2021",
    publisher = {Link{\"o}ping University Electronic Press, Sweden},
    url = "https://aclanthology.org/2021.nodalida-main.29",
    pages = "288--298"}
```

## Acknowledgements

* **Project team**: Li-Hsin Chang, Filip Ginter, Jenna Kanerva, Jemina Kilpeläinen, Hanna-Mari Kupari, Aurora Piirto, Iiro Rastas, Jenna Saarni, Maija Sevón, Valtteri Skantsi, Otto Tarkka (alphabetic order)
* **Funding**:
  * [European Language Grid](https://www.european-language-grid.eu/)
  * Academy of Finland
* **Data**:
  * [opensubtitles.org](https://opensubtitles.org)


<figure>
  <img style="width:50%" src="assets/images/paraphrase_team.jpg" />
  <figcaption style="width:50%">The project team: Filip Ginter, Jenna Saarni, Jemina Kilpeläinen, Li-Hsin Chang, Otto Tarkka, Jenna Kanerva, Maija Sevón, Hanna-Mari Kupari. Not on the image: Valtteri Skantsi, Aurora Piirto</figcaption>
</figure>

