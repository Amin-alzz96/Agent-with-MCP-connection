from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()
# Get the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Check if the API key is set correctly
if OPENAI_API_KEY is None:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
# Initialize the OpenAI LLM with the API key
def llm():
    """Initialize the OpenAI LLM with the API key."""
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

# if __name__ == "__main__":

#     llm = llm()
#     messages = [
#     (
#         "system",
#         "You are a helpful assistant that translates English to French. Translate the user sentence.",
#     ),
#     ("human", "I love programming."),
#     ]
#     response = llm.invoke(messages)
#     print(response)