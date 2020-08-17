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
