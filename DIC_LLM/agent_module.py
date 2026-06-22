import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load secret variables from the .env file into the system environment #gitignore
load_dotenv()

def ask_agent_with_search(prompt_text: str) -> str:
    """
    Calls the Gemini API with Google Search tools enabled.
    Args:
        prompt_text (str): The instructions for the agent.
    Returns:
        str: The generated text response from the LLM or an error message.
    """
    
    # Retrieve the API key securely from the environment
    api_key = os.environ.get("GEMINI_API_KEY")
    
    # Safety check to prevent confusing errors if the .env file is missing
    if not api_key:
        raise ValueError("API Key is missing! Please check your .env file.")

    # Initialize the client using the secure key
    client = genai.Client(api_key=api_key)

    try:
        # Request generation with internet access
        response = client.models.generate_content(
            model='gemini-3.1-pro-preview',
            contents=prompt_text,
            config=types.GenerateContentConfig(
                tools=[{"google_search": {}}],
                temperature=0.2 
            )
        )
        
        # Return the actual text string instead of printing it directly
        return response.text

    except Exception as e:
        # Return the error message to the caller for proper logging/handling
        return f"Error during API call: {e}"