import requests
import json
import os
from typing import Dict, Any, Optional

class GeminiClient:
    """A simple client for interacting with Gemini 2.0 Flash API"""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the Gemini client with API key"""
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided or set as GEMINI_API_KEY environment variable")
        
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
        
    def generate_response(self, prompt: str, temperature: float = 0.7, max_tokens: int = 1024, raw_response: bool = False) -> Dict[Any, Any]:
        """Generate a response from Gemini 2.0 Flash
        
        Args:
            prompt: The text prompt to send to the model
            temperature: Controls randomness (0.0-1.0)
            max_tokens: Maximum number of tokens to generate
            raw_response: If True, returns the raw API response
            
        Returns:
            Response from the API as a dictionary
        """
        headers = {
            "Content-Type": "application/json"
        }
        
        data = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }],
            "generationConfig": {
                "temperature": temperature,
                "maxOutputTokens": max_tokens
            }
        }
        
        url = f"{self.base_url}?key={self.api_key}"
        
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            
            if raw_response:
                return result
            
            # Extract the generated text from the response
            if "candidates" in result and len(result["candidates"]) > 0:
                candidate = result["candidates"][0]
                if "content" in candidate and "parts" in candidate["content"]:
                    parts = candidate["content"]["parts"]
                    if parts and "text" in parts[0]:
                        return {"text": parts[0]["text"]}
            
            return {"error": "Unable to parse response", "raw": result}
            
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}