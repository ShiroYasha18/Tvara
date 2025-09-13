# Gemini 2.0 Flash API Client

A simple Python client for interacting with the Gemini 2.0 Flash API, featuring both a command-line interface and a FastAPI web service.

## Features

- Simple Python client for Gemini 2.0 Flash API
- Command-line interface for quick testing
- FastAPI web service with the same endpoint path as the official Gemini API
- Adjustable generation parameters (temperature, max tokens)
- Option to view raw API responses for debugging
- Health check endpoint for monitoring

## Setup

1. Install the required dependencies:

```bash
pip install requests fastapi uvicorn python-dotenv pydantic
```

2. Set your Gemini API key:

   **Option 1:** Create a `.env` file in the project directory:
   ```
   GEMINI_API_KEY=your-api-key-here
   ```

   **Option 2:** Set as an environment variable:
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```

   **Option 3:** Provide it directly when running the CLI

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

### FastAPI Web Service

1. Start the FastAPI server:

```bash
uvicorn api:app --reload
```

2. Send requests to the API endpoint:

```bash
# Using curl
curl -X POST http://localhost:8000/v1beta/models/gemini-2.0-flash:generateContent \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Tell me about quantum computing", "temperature":0.7, "max_tokens":1024, "debug":false}'
```

3. Check API health:

```bash
curl http://localhost:8000/health
```

4. Access interactive API documentation at: http://localhost:8000/docs

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

## API Parameters

Both the CLI and FastAPI service support the following parameters:

| Parameter    | Description                                   | Default | Range     |
|--------------|-----------------------------------------------|---------|----------|
| prompt       | The text prompt to send to the model          | -       | -        |
| temperature  | Controls randomness of the output             | 0.7     | 0.0-1.0  |
| max_tokens   | Maximum number of tokens to generate          | 1024    | 1-8192   |
| debug/raw    | Returns the raw API response if true          | false   | true/false |

## Error Handling

The client handles common errors including:
- Missing API key
- Network connectivity issues
- API rate limiting
- Invalid requests

## Repository Structure

- `gemini_client.py` - Core client for Gemini API
- `cli.py` - Command-line interface
- `api.py` - FastAPI web service
- `.env` - Environment variables (not tracked in git)
- `.gitignore` - Excludes sensitive files like .env