
# Hugging Face

Hugging Face pasó de ser una simple app de chatbot (2016) a convertirse en una de las principales plataformas de IA del mundo gracias a apostar por el open source.

2018–2019 → Cambian de dirección
👉 Deciden centrarse en inteligencia artificial y procesamiento de lenguaje natural (NLP)
👉 Lanzan la librería Transformers

2020 en adelante → Crecimiento muy rápido
👉 Se convierte en una plataforma clave para compartir modelos de IA
👉 Nace el concepto de “GitHub de los modelos”
👉 Empresas grandes empiezan a usarla

**Herramientas comunes**
1. Transformers (pipeline) – Uso local

Es parte de la librería de Hugging Face Transformers
Se ejecuta en tu propio código (Python)
Descargas el modelo y lo ejecutas en tu máquina o servidor

2. Inference API – Uso remoto

Servicio en la nube de Hugging Face
Haces una petición HTTP (API) o a través del cliente y ellos ejecutan el modelo


## Transformers (Pipeline)

https://huggingface.co/facebook/bart-large-cnn


![Hugging Face ](../../../../desarrollo-multiplataforma/x-assets/0485/hf.png)

Llevar a cabo usando **Colab**

## Resumen de textos

```python
from transformers import pipeline

# Create a summarization pipeline
summarizer = pipeline("text-generation", model="facebook/bart-large-cnn")


# Example text
text = """
Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are
programmed to think like humans and mimic their actions. AI has a wide range of applications,
from natural language processing to computer vision, and it is transforming industries
such as healthcare, finance, and transportation.
"""

# Generate summary
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)


# Ejecutar en otra celda ****
print(summary)
print(summary[0]["generated_text"])
```


## Preguntas y respuestas

```python
from transformers import pipeline
question_answerer = pipeline("question-answering", model='distilbert-base-cased-distilled-squad')

context = r"""
Extractive Question Answering is the task of extracting an answer from a text given a question. An example of a
question answering dataset is the SQuAD dataset, which is entirely based on that task. If you would like to fine-tune
a model on a SQuAD task, you may leverage the examples/pytorch/question-answering/run_squad.py script.
"""

result = question_answerer(question="What is a good example of a question answering dataset?", context=context)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end:{result['end']}")

```


# Inference API

```python
import os
from huggingface_hub import InferenceClient
from google.colab import userdata

client = InferenceClient(
    provider="hf-inference",
    api_key=userdata.get('HF_TOKEN')
)

result = client.summarization(
    "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.",
    model="facebook/bart-large-cnn",
)

print(result)
```