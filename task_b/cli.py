#!/usr/bin/env python3
import argparse
import json
import os
from gemini_client import GeminiClient

def main():
    parser = argparse.ArgumentParser(description="Gemini 2.0 Flash API Client")
    parser.add_argument("--prompt", "-p", type=str, help="Text prompt to send to Gemini")
    parser.add_argument("--temperature", "-t", type=float, default=0.7, help="Temperature for generation (0.0-1.0)")
    parser.add_argument("--max-tokens", "-m", type=int, default=1024, help="Maximum tokens to generate")
    parser.add_argument("--raw", "-r", action="store_true", help="Display raw API response for debugging")
    parser.add_argument("--api-key", "-k", type=str, help="Gemini API key (or set GEMINI_API_KEY env var)")
    
    args = parser.parse_args()
    
    if not args.prompt:
        prompt = input("Enter your prompt: ")
    else:
        prompt = args.prompt
    
    try:
        client = GeminiClient(api_key=args.api_key)
        response = client.generate_response(
            prompt=prompt,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            raw_response=args.raw
        )
        
        if args.raw:
            print(json.dumps(response, indent=2))
        elif "error" in response:
            print(f"Error: {response['error']}")
        else:
            print(response["text"])
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()