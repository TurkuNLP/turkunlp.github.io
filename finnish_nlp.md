---
layout: page
title: Finnish NLP
---

## Finnish Parser <a id="parser"></a>

Finnish dependency parser pipeline, which include **tokenization, sentence splitting, lemmatization, morphological tagging and dependency parsing**.

[More information on the parser project](parser.html)
 
 **Contact:** Filip Ginter (figint@utu.fi), Jenna Kanerva (jmnybl@utu.fi) or [github issue tracker](https://github.com/TurkuNLP/Turku-neural-parser-pipeline/issues)
 
## UD_Finnish treebank (Turku Dependency Treebank) <a id="treebank"></a>
 
 UD_Finnish treebank is a broad-coverage dependency-annotated treebank of general Finnish annotated in the [Universal Dependencies scheme](http://universaldependencies.org/). The treebank has about 200,000 words and 15,000 sentences.
 
The original Turku Dependency Treebank (TDT) was annotated in the Stanford dependency scheme, and later converted into the UD scheme. The UD version of the treebank is the main version, which is maintained. The UD version is distributed trough the UD project ([data](http://universaldependencies.org/#download)). The original version (TDT) is also available upon request but it is not maintained anymore. The original treebank has also additional data available regarding the annotation process (double annotations, timestamps etc).

**Online treebank search:** Finnish (UDv2.0) treebank in <http://bionlp-www.utu.fi/dep_search/>

**License:** CC BY-SA 4.0

**Main references:**
Haverinen, K.; Nyblom, J.; Viljanen, T.; Laippala, V.; Kohonen, S.; Missilä, A.; Ojala, S.; Salakoski, T.; Ginter, F.: Building the essential resources for Finnish: the Turku Dependency Treebank. Language Resources and Evaluation. 2013. [DOI: 10.1007/s10579-013-9244-1](http://dx.doi.org/10.1007/s10579-013-9244-1)

Pyysalo, Sampo; Kanerva, Jenna; Missilä, Anna; Laippala, Veronika; Ginter, Filip: Universal Dependencies for Finnish. Proceedings of NoDaLiDa 2015 <https://aclweb.org/anthology/W/W15/W15-1821.pdf>

**Contact:** Filip Ginter (figint@utu.fi), Jenna Kanerva (jmnybl@utu.fi)

## Finnish Internet Parsebank <a id="parsebank"></a>

A mass-scale corpus of Internet Finnish with automatic syntactic analysis. Currently includes about 3.7 billion tokens.

The project has three aims: 1) The creation of a language resource with automatic morphological and syntactic analyses, 2) The classification of the entire Parsebank to coherent subcorpora, 3) The creation of an online user interface

**Online search of the morpho-syntactic features:** Finnish Internet Parsebank corpus in [Dep Search](http://depsearch-depsearch.rahtiapp.fi/ds_demo/)

**Online search for words and their contexts:** Finnish Internet Parsebank corpus in [NoSketchEngine](http://epsilon-it.utu.fi/nse/) 

**Semantic similarity of words:** An online demo which lets you query semantically similar words using a word2vec model trained on the Parsebank data, <http://epsilon-it.utu.fi/wv_demo/>. Embedding models in binary form are available [here](http://dl.turkunlp.org/finnish-embeddings/).

**Word frequency list:** A Finnish word frequency list can be downloaded at <http://dl.turkunlp.org/finnish-parsebank/>. It's calculated from the Parsebank data and sorted in descending order. If you use this in your research, please cite us.

**Main references:**
J. Luotolahti; J. Kanerva; V. Laippala; S. Pyysalo; F. Ginter. Towards Universal Web Parsebanks. Proceedings of the International Conference on Dependency Linguistics (Depling'15). 2015

**Contact:** Filip Ginter (figint@utu.fi), Veronika Laippala (mavela@utu.fi)

## Search Tool for Dependency Graphs (dep_search) <a id="depsearch"></a>

Tool for searching morpho-syntactic constructions from dependency graphs.

Beta version of the tool's new demo: <http://depsearch-depsearch.rahtiapp.fi/ds_demo/>

**Main references:**
J. Luotolahti; J. Kanerva; S. Pyysalo; F. Ginter. SETS: Scalable and Efficient Tree Search in Dependency Graphs. Proceedings of the 2015 Conference of the North American Chapter of the Association for Computational Linguistics: Demonstrations. 2015

J. Luotolahti; J. Kanerva; F. Ginter. Dep_search: Efficient Search Tool for Large Dependency Parsebanks. Proceedings of the 21st Nordic Conference on Computational Linguistics (NoDaLiDa). 2017

**Contact:** Filip Ginter (figint@utu.fi), Juhani Luotolahti (mjluot@utu.fi)

## Finnish Propbank <a id="propbank"></a>

Finnish PropBank is a collection of predicates annotated with their sense and arguments. The data builds on top of the Turku Dependency Treebank (TDT), more specifically its Universal Dependencies version.

More information on the propbank's project page: <http://turkunlp.github.io/Finnish_PropBank/>

**License:** CC BY-SA 4.0

**Main references:**
Haverinen, K.; Kanerva, J.; Kohonen, S.; Missilä, A.; Ojala, S.; Viljanen, T.; Laippala, V.; Ginter, F. The Finnish Proposition Bank. Language Resources and Evaluation. 2015

**Contact:** Filip Ginter (figint@utu.fi), Jenna Kanerva (jmnybl@utu.fi)

## Finnish BERT (FinBERT) <a id="finbert"></a>

BERT model trained from scratch on Finnish.

More information on the FinBERT's project page: <https://github.com/TurkuNLP/FinBERT>

**License:** CC BY 4.0

**Main references:** A. Virtanen; J. Kanerva; R. Ilo; J. Luoma; J. Luotolahti; T. Salakoski; F. Ginter; S. Pyysalo. Multilingual is not enough: BERT for Finnish. arXiv preprint arXiv:1912.07076. 2019

**Contact:** [github issue tracker](https://github.com/TurkuNLP/FinBERT/issues)

## Finnish NER <a id="fin-ner"></a>

A state-of-the-art Finnish NER system

More information and online demo on the [NER's project page](fin-ner.html)

**Main references:** Jouni Luoma, Miika Oinonen, Maria Pyykönen, Veronika Laippala, Sampo Pyysalo. 2020. A Broad-coverage Corpus for Finnish Named Entity Recognition. In Proceedings of The 12th Language Resources and Evaluation Conference (LREC'2020). [BibTeX](https://www.aclweb.org/anthology/2020.lrec-1.567.bib)

**Contact:** Sampo Pyysalo (sampo.pyysalo@gmail.com)

## Finnish paraphrase <a id="fin-para"></a>

Textual paraphrase dataset for deep language modeling gathers a large dataset of Finnish and Swedish paraphrases.

[More information on the paraphrase project](paraphrase.html)

**Contact:** Filip Ginter (figint@utu.fi)

## Finnish Ice Hockey Data2Text <a id="hockey-data2text"></a>

The Turku Hockey Data2Text dataset for ice hockey news generation is a collection of ice hockey statistics combined with Finnish natural language descriptions of the game events.

[More information on the data2text page](hockey_data2text.html)

**Main references:** Jenna Kanerva, Samuel Rönnqvist, Riina Kekki, Tapio Salakoski, Filip Ginter. 2019.	Template-free Data-to-Text Generation of Finnish Sports News. In	Proceedings of the 22nd Nordic Conference on Computational Linguistics (NoDaLiDa’19). [BibTeX](https://aclanthology.org/W19-6125/)

**Contact:** Jenna Kanerva (jmnybl@utu.fi), Filip Ginter (figint@utu.fi)


