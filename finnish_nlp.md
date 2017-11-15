---
layout: page
title: Finnish NLP
---

## Finnish Parser

Finnish dependency parser pipeline, which include tokenization, sentence splitting, lemmatization, tagging and dependency parsing.

 More information on the parser's project page: <http://turkunlp.github.io/Finnish-dep-parser/>
 
 **Contact:** Filip Ginter (ginter@cs.utu.fi), Jenna Kanerva (jmnybl@utu.fi) or [github issue tracker](https://github.com/TurkuNLP/Finnish-dep-parser/issues)
 
## UD_Finnish treebank (Turku Dependency Treebank)
 
 UD_Finnish treebank is a broad-coverage dependency-annotated treebank of general Finnish annotated in the [Universal Dependencies scheme](http://universaldependencies.org/). The treebank has about 200,000 words and 15,000 sentences.
 
The original Turku Dependency Treebank (TDT) was annotated in the Stanford dependency scheme, and later converted into the UD scheme. The UD version of the treebank is the main version, which is maintained. The UD version is distributed trough the UD project ([data](http://universaldependencies.org/#download)). The original version (TDT) is also available upon request but it is not maintained anymore. The original treebank has also additional data available regarding the annotation process (double annotations, timestamps etc).

**Online treebank search:** Finnish (UDv2.0) treebank in <http://bionlp-www.utu.fi/dep_search/>

**License:** CC BY-SA 4.0

**Main references:**
Haverinen, K.; Nyblom, J.; Viljanen, T.; Laippala, V.; Kohonen, S.; Missilä, A.; Ojala, S.; Salakoski, T.; Ginter, F.: Building the essential resources for Finnish: the Turku Dependency Treebank. Language Resources and Evaluation. 2013. [DOI: 10.1007/s10579-013-9244-1](http://dx.doi.org/10.1007/s10579-013-9244-1)

Pyysalo, Sampo; Kanerva, Jenna; Missilä, Anna; Laippala, Veronika; Ginter, Filip: Universal Dependencies for Finnish. Proceedings of NoDaLiDa 2015 <https://aclweb.org/anthology/W/W15/W15-1821.pdf>

**Contact:** Filip Ginter (ginter@cs.utu.fi), Jenna Kanerva (jmnybl@utu.fi)

## Finnish Internet Parsebank

A mass-scale corpus of Internet Finnish with automatic syntactic analysis. Currently includes about 3.7 billion tokens.

The project has three aims: 1) The creation of a language resource with automatic morphological and syntactic analyses, 2) The classification of the entire Parsebank to coherent subcorpora, 3) The creation of an online user interface

**Online search of the morpho-syntactic features:** Finnish Internet Parsebank corpus in <http://bionlp-www.utu.fi/dep_search/>

**Semantic similarity of words:** An online demo which lets you query semantically similar words using a word2vec model trained on the Parsebank data, <http://bionlp-www.utu.fi/wv_demo/>

**Word frequency list:** A Finnish word frequency list can be downloaded at <http://bionlp-www.utu.fi/.jmnybl/finnish_vocab.txt.gz>. It's calculated from the Parsebank data and sorted in descending order. If you use this in your research, please cite us.

**Main references:**
J. Luotolahti; J. Kanerva; V. Laippala; S. Pyysalo; F. Ginter. Towards Universal Web Parsebanks. Proceedings of the International Conference on Dependency Linguistics (Depling'15). 2015

**Contact:** Filip Ginter (ginter@cs.utu.fi), Veronika Laippala (mavela@utu.fi)

## Search Tool for Dependency Graphs (dep_search)

Tool for searching morpho-syntactic constructions from dependency graphs.

More information on the dep_search's project page: <http://bionlp-www.utu.fi/dep_search/>

**Main references:**
J. Luotolahti; J. Kanerva; S. Pyysalo; F. Ginter. SETS: Scalable and Efficient Tree Search in Dependency Graphs. Proceedings of the 2015 Conference of the North American Chapter of the Association for Computational Linguistics: Demonstrations. 2015

J. Luotolahti; J. Kanerva; F. Ginter. Dep_search: Efficient Search Tool for Large Dependency Parsebanks. Proceedings of the 21st Nordic Conference on Computational Linguistics (NoDaLiDa). 2017

**Contact:** Filip Ginter (ginter@cs.utu.fi), Juhani Luotolahti (mjluot@utu.fi)

## Finnish Propbank

Finnish PropBank is a collection of predicates annotated with their sense and arguments. The data builds on top of the Turku Dependency Treebank (TDT), more specifically its Universal Dependencies version.

More information on the propbank's project page: <http://turkunlp.github.io/Finnish_PropBank/>

**License:** CC BY-SA 4.0

**Main references:**
Haverinen, K.; Kanerva, J.; Kohonen, S.; Missilä, A.; Ojala, S.; Viljanen, T.; Laippala, V.; Ginter, F. The Finnish Proposition Bank. Language Resources and Evaluation. 2015

**Contact:** Filip Ginter (ginter@cs.utu.fi), Jenna Kanerva (jmnybl@utu.fi)
