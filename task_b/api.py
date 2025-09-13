from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import Optional, Dict, Any
from gemini_client import GeminiClient
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI(title="Gemini 2.0 Flash API")

# Initialize the Gemini client
api_key = os.environ.get("GEMINI_API_KEY")
# Fallback to the hardcoded API key if environment variable is not set
if not api_key:
    api_key = "AIzaSyDSKBupwR_jNNUTFeodQkOl26LlA0gjxcU"
    
gemini_client = GeminiClient(api_key=api_key)

# Define request model
class PromptRequest(BaseModel):
    prompt: str
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 1024
    debug: Optional[bool] = False

@app.post("/v1beta/models/gemini-2.0-flash:generateContent")
async def generate_content(request: PromptRequest = Body(...)):
    try:
        response = gemini_client.generate_response(
            prompt=request.prompt,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
            raw_response=request.debug
        )
        
        if "error" in response and not request.debug:
            raise HTTPException(status_code=500, detail=response["error"])
            
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Add a simple health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)