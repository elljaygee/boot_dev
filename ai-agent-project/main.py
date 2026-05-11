import os
import time
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.prompts import system_prompt

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("No API key found")
client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

def main():
    for attempt in range(5):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=messages,
                config=types.GenerateContentConfig(system_instruction=system_prompt),
            )

            if not response.usage_metadata:
                raise RuntimeError("No metadata found")
            
            else:
                prompt_tokens = response.usage_metadata.prompt_token_count
                response_tokens = response.usage_metadata.candidates_token_count
                user_prompt = args.user_prompt

                if args.verbose == True:
                    print(f"User prompt: {user_prompt}")
                    print(f"Prompt tokens: {prompt_tokens}")
                    print(f"Response tokens: {response_tokens}")

                print(response.text)

            break

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
