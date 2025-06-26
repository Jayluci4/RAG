import os
from google import generativeai as genai
from llama_index.core import Settings
from llama_index.core.llms import ChatMessage
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

def init_settings():
    if os.getenv("GOOGLE_API_KEY") is None:
        raise RuntimeError("GOOGLE_API_KEY is missing in environment variables")
    
    # Initialize Gemini client
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    
    # Example chat messages
    messages = [
        ChatMessage(
            role="system", content="You are a pirate with a colorful personality"
        ),
        ChatMessage(role="user", content="Tell me a story"),
    ]
    
    # Set up LlamaIndex settings with Gemini
    Settings.llm = GoogleGenAI(model="gemini-2.0-flash")
    
    # Set up Google GenAI embedding model
    embed_model = GoogleGenAIEmbedding(
        model_name="text-embedding-004",
        embed_batch_size=100,
        api_key=os.getenv("GOOGLE_API_KEY")
    )
    Settings.embed_model = embed_model
