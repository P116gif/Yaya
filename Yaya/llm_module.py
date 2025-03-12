# llm_module.py

import requests
import re
from tts_module import text_to_speech

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def generate_response(input_file):
    """
    Sends a prompt to Deepseek R1:8B via Ollama's REST API and returns the response.
    """
    try:
        
        with open(input_file, "r", encoding="utf-8") as file:
                content = file.read()
                prompt =  content

        # Define the payload for the API request
        payload = {
            "model": "deepseek-r1:8b",  # Use the correct model name
            "prompt": prompt,          # The input prompt
            "stream": False            # Set to True if you want streaming responses
        }

        print("Sending post request to Ollama API")
        # Send a POST request to the Ollama API
        response = requests.post(OLLAMA_API_URL, json=payload)

        # Check if the request was successful
        if response.status_code == 200:

            # Parse the JSON response
            print("Received response\n")
            response_data = response.json()
            raw_response = response_data.get("response", "No response from LLM")

            cleaned_response = re.sub(r"<think>.*?</think>", "", raw_response, flags=re.DOTALL).strip()
            
            text_to_speech(cleaned_response)
            return cleaned_response
        else:
            # Return an error message if the request failed
            return f"Error: {response.text}"
    except Exception as e:
        # Handle any exceptions that occur during the request
        return f"Exception occurred: {str(e)}"