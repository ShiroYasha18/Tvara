from sentence_transformers import SentenceTransformer
import os
import time

def load_model(model_name="intfloat/e5-small-v2"):
    """
    Download and load the specified embedding model.
    
    Args:
        model_name: Name of the model to load from Hugging Face
        
    Returns:
        Loaded model instance
    """
    print(f"Loading model: {model_name}")
    start_time = time.time()
    
    # Download and load the model
    model = SentenceTransformer(model_name)
    
    elapsed_time = time.time() - start_time
    print(f"Model loaded in {elapsed_time:.2f} seconds")
    
    return model


if __name__ == "__main__":
    # Test the model loading
    model = load_model()
    print(f"Model loaded successfully: {model}")