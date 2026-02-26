# Transformers con Hugging Face

https://huggingface.co/facebook/bart-large-cnn

TO improve later


Input preprocessing
a) Tokenization
The text "Artificial Intelligence is amazing." is split into tokens (words or subwords).

Example: "Artificial Intelligence" → ["Art", "##ificial", "Intelligence"] (depends on the tokenizer)

Each token is converted into a number (token ID) that the model can understand.

Example: [1234, 5678, 90, 11]

b) Special tokens and attention masks
Transformers need start/end tokens and attention masks:

[CLS] or [BOS] → marks the start

[EOS] → marks the end

Attention mask → tells the model which tokens are actual text vs padding

2️⃣ Passing tokens through the model
The model is a neural network with layers of transformers.

Each token vector passes through:

Embedding layer → turns token IDs into dense vectors

Attention layers → each token “looks at” all other tokens to understand context

Feedforward layers → processes each token’s information

Output layer → predicts next token probabilities (or summary tokens)

For text2text-generation, it generates tokens one by one, sometimes using strategies like beam search or greedy decoding.

3️⃣ Output decoding
The model outputs a sequence of token IDs.

The pipeline automatically converts these IDs back to human-readable text.

[432, 111, 55] → "AI is incredible."

It handles removing special tokens like [BOS] or [EOS].

4️⃣ Postprocessing
The pipeline also applies:

Truncation / padding to match model limits

Optional filtering (like avoiding repeated words or bad tokens)

Returning results in a consistent format (e.g., {'generated_text': "..."})

✅ Summary of the pipeline steps
Step	What happens	Who handles it?
Input preprocessing	Text → tokens, special tokens, attention masks	Tokenizer
Model forward pass	Token embeddings → attention → feedforward → logits	Transformer model
Output decoding	Token IDs → human-readable text	Pipeline + tokenizer
Postprocessing	Remove special tokens, format output	Pipelin



![Window Builder ](../../../x-assets/0485/hg1.png)

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


