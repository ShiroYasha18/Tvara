"""
Demonstration of E5 Embedding and Similarity Search

This script demonstrates how to use the similarity_search module
to generate embeddings and find similar sentences.
"""

from similarity_search import generate_embeddings, find_similar_sentences
from sample_data import get_sample_sentences
from model_loader import load_model


def run_demo():
    print("E5 Embedding and Similarity Search Demo")
    print("-" * 50)
    
    # Load the model (load once and reuse)
    print("\nLoading E5 model...")
    model = load_model()
    
    # Get sample sentences
    sentences = get_sample_sentences()
    print(f"\nLoaded {len(sentences)} sample sentences")
    
    # Generate embeddings for all sentences
    print("\nGenerating embeddings for all sentences...")
    embedding_dict = generate_embeddings(sentences, model)
    
    # Example queries
    queries = [
        "How do neural networks work?",
        "What is unsupervised learning?",
        "Explain computer vision technology"
    ]
    
    # Run similarity search for each query
    for query in queries:
        print(f"\n\nQuery: '{query}'")
        print("Finding most similar sentences...")
        
        # Find similar sentences
        similar_sentences = find_similar_sentences(query, embedding_dict, model, top_k=3)
        
        # Print results
        print("\nTop 3 most similar sentences:")
        for i, (sentence, score) in enumerate(similar_sentences, 1):
            print(f"{i}. [{score:.4f}] {sentence}")


if __name__ == "__main__":
    run_demo()