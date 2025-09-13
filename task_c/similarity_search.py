"""
Similarity Search using E5 Embeddings

This module implements text embedding generation and similarity search
using the E5 model from Hugging Face.

References:
- E5 model: https://huggingface.co/intfloat/e5-small-v2
- Based on concepts from the provided research paper (2212.03533v2.pdf)
"""

import numpy as np
from scipy.spatial.distance import cosine
import time
from typing import List, Tuple, Dict, Any

# Import our custom modules
from model_loader import load_model
from sample_data import get_sample_sentences


def generate_embeddings(sentences: List[str], model=None):
    """
    Generate embeddings for a list of sentences using the E5 model.
    
    Args:
        sentences: List of sentences to embed
        model: Pre-loaded model (if None, will load the model)
        
    Returns:
        Dictionary with sentences as keys and their embeddings as values
    """
    if model is None:
        print("Loading E5 model...")
        model = load_model()
    
    # E5 models expect input in the format "query: " or "passage: "
    # For similarity search, we use "passage: " prefix
    prefixed_sentences = [f"passage: {sentence}" for sentence in sentences]
    
    print(f"Generating embeddings for {len(sentences)} sentences...")
    start_time = time.time()
    
    # Generate embeddings
    embeddings = model.encode(prefixed_sentences, normalize_embeddings=True)
    
    end_time = time.time()
    print(f"Embeddings generated in {end_time - start_time:.2f} seconds")
    
    # Create a dictionary mapping sentences to their embeddings
    embedding_dict = {sentence: embedding for sentence, embedding in zip(sentences, embeddings)}
    
    return embedding_dict


def find_similar_sentences(query: str, embedding_dict: Dict[str, np.ndarray], model=None, top_k: int = 3) -> List[Tuple[str, float]]:
    """
    Find the most similar sentences to a query using cosine similarity.
    
    Args:
        query: The query sentence
        embedding_dict: Dictionary mapping sentences to their embeddings
        model: Pre-loaded model (if None, will load the model)
        top_k: Number of top results to return
        
    Returns:
        List of tuples (sentence, similarity_score) sorted by similarity (highest first)
    """
    if model is None:
        print("Loading E5 model...")
        model = load_model()
    
    # E5 models expect input in the format "query: " for queries
    prefixed_query = f"query: {query}"
    
    # Generate embedding for the query
    query_embedding = model.encode([prefixed_query], normalize_embeddings=True)[0]
    
    # Calculate similarity scores
    similarities = []
    for sentence, embedding in embedding_dict.items():
        # Calculate cosine similarity (1 - cosine distance)
        similarity = 1 - cosine(query_embedding, embedding)
        similarities.append((sentence, similarity))
    
    # Sort by similarity score (highest first)
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    # Return top-k results
    return similarities[:top_k]


if __name__ == "__main__":
    # Load the model
    model = load_model()
    
    # Get sample sentences
    sentences = get_sample_sentences()
    
    # Generate embeddings
    embedding_dict = generate_embeddings(sentences, model)
    
    # Example query
    query = "How do neural networks work?"
    
    print(f"\nQuery: '{query}'")
    print("Finding most similar sentences...")
    
    # Find similar sentences
    similar_sentences = find_similar_sentences(query, embedding_dict, model)
    
    # Print results
    print("\nTop 3 most similar sentences:")
    for i, (sentence, score) in enumerate(similar_sentences, 1):
        print(f"{i}. [{score:.4f}] {sentence}")