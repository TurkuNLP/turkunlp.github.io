---
layout: page
title: FinGPT-3
---

We have trained generative [GPT-3](https://en.wikipedia.org/wiki/GPT-3)-like models for Finnish. The models are documented in our manuscript [FinGPT: Large Generative Models for a Small Language](https://arxiv.org/abs/2311.05640) (see citation below).

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
@misc{luukkonen2023fingpt,
      title={FinGPT: Large Generative Models for a Small Language}, 
      author={Risto Luukkonen and Ville Komulainen and Jouni Luoma and Anni Eskelinen and Jenna Kanerva and Hanna-Mari Kupari and Filip Ginter and Veronika Laippala and Niklas Muennighoff and Aleksandra Piktus and Thomas Wang and Nouamane Tazi and Teven Le Scao and Thomas Wolf and Osma Suominen and Samuli Sairanen and Mikko Merioksa and Jyrki Heinonen and Aija Vahtola and Samuel Antao and Sampo Pyysalo},
      year={2023},
      eprint={2311.05640},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
}
```

---

**Acknowledgments**: The models were created in collaboration with the National Library of Finland (<https://www.kansalliskirjasto.fi>). We wish to acknowledge CSC – IT Center for Science, Finland, for generous computational resources. This project has received funding from the European Union’s Horizon Europe research and innovation programme under grant agreement No 101070350.
