"""
Sample data for embedding and similarity search demonstration.

This module provides a collection of sample sentences that can be used
for demonstrating embedding generation and similarity search functionality.
"""

# Sample sentences from a hypothetical PDF document about machine learning
SAMPLE_SENTENCES = [
    "Machine learning is a subset of artificial intelligence that focuses on data-driven algorithms.",
    "Neural networks are computing systems inspired by the biological neural networks in animal brains.",
    "Deep learning is part of a broader family of machine learning methods based on artificial neural networks.",
    "Supervised learning algorithms build a mathematical model from labeled training data.",
    "Unsupervised learning is a type of algorithm that learns patterns from unlabeled data.",
    "Reinforcement learning is about taking suitable actions to maximize reward in a particular situation.",
    "Natural language processing helps computers understand, interpret, and manipulate human language.",
    "Computer vision is an interdisciplinary field that deals with how computers can gain high-level understanding from digital images or videos.",
    "Transfer learning is a machine learning technique where a model developed for one task is reused for a second related task.",
    "Feature extraction involves reducing the number of resources required to describe a large set of data."
]


def get_sample_sentences():
    """Return the list of sample sentences."""
    return SAMPLE_SENTENCES


def get_sentence_by_index(index):
    """Return a specific sentence by its index."""
    if 0 <= index < len(SAMPLE_SENTENCES):
        return SAMPLE_SENTENCES[index]
    else:
        raise IndexError(f"Index {index} out of range. Valid range: 0-{len(SAMPLE_SENTENCES)-1}")


if __name__ == "__main__":
    # Print all sample sentences with their indices
    for i, sentence in enumerate(SAMPLE_SENTENCES):
        print(f"[{i}] {sentence}")