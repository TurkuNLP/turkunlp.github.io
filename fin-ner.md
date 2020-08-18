---
layout: page
title: Finnish NER
---

We have trained an NER system based on FinBERT and a new NER annotation layer of the UD_Finnish-TDT treebank. In comparisons, the NER system surpassed the state-of-the-art.

Links and resources:
  * [Online demo](http://86.50.253.19:8001/tagdemo/)
  * [LREC2020 Paper](http://www.lrec-conf.org/proceedings/lrec2020/pdf/2020.lrec-1.567.pdf)
  * [Code](https://github.com/jouniluoma/keras-bert-ner)
  * [Trained model](http://dl.turkunlp.org/turku-ner-models/)
  * [Data](https://github.com/TurkuNLP/turku-ner-corpus)

Note: the latest model available for download from <http://dl.turkunlp.org/turku-ner-models/combined-ext-model-130220.tar.gz> uses [OntoNotes NE types](https://catalog.ldc.upenn.edu/docs/LDC2013T19/OntoNotes-Release-5.0.pdf#page=21):

| Type | Description |
|---|---|
|PERSON	| People, including fictional
| NORP	| Nationalities or religious or political groups
| FAC	| Buildings, airports, highways, bridges, etc.
| ORG	| Companies, agencies, institutions, etc.
| GPE	| Countries, cities, states
| LOC	| Non-GPE locations, mountain ranges, bodies of water
| PRODUCT	| Objects, vehicles, foods, etc. (Not services.)
| EVENT	| Named hurricanes, battles, wars, sports events, etc.
| WORK_OF_ART	| Titles of books, songs, etc.
| LAW	| Named documents made into laws
| LANGUAGE	| Any named language
| DATE	| Absolute or relative dates or periods
| TIME	| Times smaller than a day
| PERCENT	| Percentage, including "%"
| MONEY	| Monetary values, including unit
| QUANTITY	| Measurements, as of weight or distance
| ORDINAL	| "first", "second"
| CARDINAL	| Numerals that do not fall under another type

To run a server version of the tagger locally (in UNIX):

```
git clone https://github.com/spyysalo/keras-bert-ner.git
cd keras-bert-ner/
git submodule init
git submodule update
wget http://dl.turkunlp.org/turku-ner-models/combined-ext-model-130220.tar.gz
tar xvzf combined-ext-model-130220.tar.gz
python3 serve.py --ner_model_dir combined-ext-model
```

and then try

```
curl http://127.0.0.1:8080?text=Turun+yliopisto
```

or

```
curl -G --data-urlencode "text=Turun yliopisto" http://127.0.0.1:8080
```

If you use this system or data, please cite:

Jouni Luoma, Miika Oinonen, Maria Pyykönen, Veronika Laippala, Sampo Pyysalo. 2020. A Broad-coverage Corpus for Finnish Named Entity Recognition. In Proceedings of The 12th Language Resources and Evaluation Conference (LREC'2020). [BibTeX](https://www.aclweb.org/anthology/2020.lrec-1.567.bib)
