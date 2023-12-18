---
layout: page
title: FinGPT-3
---

We have trained generative [GPT-3](https://en.wikipedia.org/wiki/GPT-3)-like models for Finnish. The models are documented in our manuscript [FinGPT: Large Generative Models for a Small Language](https://aclanthology.org/2023.emnlp-main.164/) ([PDF](https://aclanthology.org/2023.emnlp-main.164.pdf); see citation below).

The models are available via the Hugging Face model repository:

* [Finnish GPT-3 small](https://huggingface.co/TurkuNLP/gpt3-finnish-small)
* [Finnish GPT-3 medium](https://huggingface.co/TurkuNLP/gpt3-finnish-medium)
* [Finnish GPT-3 large](https://huggingface.co/TurkuNLP/gpt3-finnish-large)
* [Finnish GPT-3 xl](https://huggingface.co/TurkuNLP/gpt3-finnish-xl)
* [Finnish GPT-3 3B](https://huggingface.co/TurkuNLP/gpt3-finnish-3B)
* [Finnish GPT-3 8B](https://huggingface.co/TurkuNLP/gpt3-finnish-8B)
* [Finnish GPT-3 13B](https://huggingface.co/TurkuNLP/gpt3-finnish-13B)
* [BLOOM + Finnish 176B](https://huggingface.co/TurkuNLP/bloom-finnish-176b) ("BLUUMI")

You can also find a simple example of generating text with these models
[here](https://github.com/TurkuNLP/finngen-tools/blob/main/text_generation_example.ipynb).

---

**Citation**

If you use these models, please consider citing the study introducing them:

```
@inproceedings{luukkonen2023fingpt,
    title = "{F}in{GPT}: Large Generative Models for a Small Language",
    author = "Luukkonen, Risto and Komulainen, Ville and Luoma, Jouni and Eskelinen, Anni and Kanerva, Jenna and Kupari, Hanna-Mari and Ginter, Filip and Laippala, Veronika and Muennighoff, Niklas and Piktus, Aleksandra and Wang, Thomas and Tazi, Nouamane and Scao, Teven and Wolf, Thomas and Suominen, Osma and Sairanen, Samuli and Merioksa, Mikko and Heinonen, Jyrki and Vahtola, Aija and Antao, Samuel and Pyysalo, Sampo",
    booktitle = "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
    year = "2023",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.emnlp-main.164",
    doi = "10.18653/v1/2023.emnlp-main.164",
    pages = "2710--2726",
}
```

---

**Acknowledgments**: The models were created in collaboration with the National Library of Finland (<https://www.kansalliskirjasto.fi>). We wish to acknowledge CSC – IT Center for Science, Finland, for generous computational resources. This project has received funding from the European Union’s Horizon Europe research and innovation programme under grant agreement No 101070350.
