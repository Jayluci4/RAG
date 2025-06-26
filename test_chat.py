from llama_index.core.llms import ChatMessage
from llama_index.llms.google_genai import GoogleGenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the LLM
llm = GoogleGenAI(model="gemini-2.0-flash")

# Create chat messages
messages = [
    ChatMessage(
        role="system", content="You are a pirate with a colorful personality"
    ),
    ChatMessage(role="user", content="Tell me a story"),
]

# Get response
response = llm.chat(messages)
