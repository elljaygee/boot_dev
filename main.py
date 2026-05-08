import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    print("Hello from ai-agent-project!")


if __name__ == "__main__":
    main()
