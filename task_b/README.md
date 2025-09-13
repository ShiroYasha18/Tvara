# Gemini 2.0 Flash API Client

A simple Python client for interacting with the Gemini 2.0 Flash API.

## Setup

1. Install the required dependencies:

```bash
pip install requests
```

2. Set your Gemini API key as an environment variable:

```bash
export GEMINI_API_KEY="your-api-key-here"
```

Or provide it directly when running the CLI.

## Usage

### Command Line Interface

```bash
# Basic usage with prompt input
python cli.py -p "Tell me about quantum computing"

# Adjust generation parameters
python cli.py -p "Write a short story" -t 0.9 -m 2048

# Display raw API response for debugging
python cli.py -p "Hello, Gemini" --raw

# Provide API key directly
python cli.py -p "What's the weather like?" -k "your-api-key-here"
```

### Python API

```python
from gemini_client import GeminiClient

# Initialize client
client = GeminiClient(api_key="your-api-key-here")

# Generate a response
response = client.generate_response(
    prompt="Explain how neural networks work",
    temperature=0.7,
    max_tokens=1024,
    raw_response=False
)

# Print the response text
print(response["text"])
```

## Features

- Simple Python client for Gemini 2.0 Flash API
- Command-line interface for quick testing
- Adjustable generation parameters (temperature, max tokens)
- Option to view raw API responses for debugging