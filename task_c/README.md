# Task C: Text Vectorization with Hugging Face

This project implements text embedding generation and similarity search using the E5 model from Hugging Face. It demonstrates how to generate vector representations of text and perform semantic similarity search.

## Overview

The implementation uses the `intfloat/e5-small-v2` model, which is a state-of-the-art text embedding model that maps text to dense vector representations. These embeddings capture semantic meaning, allowing for effective similarity search.

## Features

- Load and use the E5 model for text embedding
- Generate embeddings for sample sentences
- Perform similarity search using cosine similarity
- Demonstration script with example queries

## Project Structure

- `requirements.txt`: Dependencies required for the project
- `model_loader.py`: Utility for loading the E5 model
- `sample_data.py`: Sample sentences for demonstration
- `similarity_search.py`: Core functionality for embedding generation and similarity search
- `demo.py`: Demonstration script showing the system in action
- `2212.03533v2.pdf`: Research paper reference for embedding techniques

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. The first time you run any script, it will download the E5 model (approximately 130MB).

## Usage

### Running the Demo

To see the system in action, run the demo script:

```bash
python demo.py
```

This will:
1. Load the E5 model
2. Generate embeddings for sample sentences
3. Run similarity searches for example queries
4. Display the most similar sentences for each query

### Using in Your Own Code

```python
# Import the necessary functions
from similarity_search import generate_embeddings, find_similar_sentences
from model_loader import load_model

# Load the model (do this once and reuse)
model = load_model()

# Your sentences
sentences = ["Your first sentence", "Your second sentence", ...]

# Generate embeddings
embedding_dict = generate_embeddings(sentences, model)

# Search for similar sentences
query = "Your search query"
similar_sentences = find_similar_sentences(query, embedding_dict, model, top_k=3)

# Process results
for sentence, score in similar_sentences:
    print(f"[{score:.4f}] {sentence}")
```

## Technical Details

### E5 Model

The E5 model (`intfloat/e5-small-v2`) is designed specifically for text embeddings. It expects inputs in specific formats:
- For queries: `query: {text}`
- For passages: `passage: {text}`

This implementation handles the formatting automatically.

### Similarity Calculation

Similarity between texts is calculated using cosine similarity between their embedding vectors. The score ranges from -1 (completely dissimilar) to 1 (identical), though with normalized embeddings the practical range is usually 0 to 1.

## References

- [E5 Model on Hugging Face](https://huggingface.co/intfloat/e5-small-v2)
- [Sentence Transformers Documentation](https://www.sbert.net/)
- Research paper included in the repository (2212.03533v2.pdf)