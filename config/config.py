import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
MODEL_NAME = os.getenv("MODEL_NAME", "default-model-name")





