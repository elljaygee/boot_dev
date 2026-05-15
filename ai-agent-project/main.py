import os
import time
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.prompts import system_prompt
from functions.call_function import available_functions, call_function

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
    for _ in range(20):
        final_response = False

        for attempt in range(5):
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=messages,
                    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
                )

                if response.candidates:
                    for candidate in response.candidates:
                        messages.append(candidate.content)

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

                    function_results = []

                    if response.function_calls:

                        for function_call in response.function_calls:
                            function_call_result = call_function(function_call, verbose=args.verbose)
                            if not function_call_result.parts:
                                raise Exception(f"No parts in function call result: {function_call_result}")
                            
                            if not function_call_result.parts[0].function_response:
                                raise Exception(f"No FunctionResponse object in function call result: {function_call_result}")
                            
                            if not function_call_result.parts[0].function_response.response:
                                raise Exception(f"No function result in response: {function_call_result}")
                            
                            function_results.append(function_call_result.parts[0])
            
                            if args.verbose:
                                print(f"-> {function_call_result.parts[0].function_response.response}")
                            
                            messages.append(types.Content(role="user", parts=function_results))

                    else:
                        print(response.text)
                        final_response = True
                        
                        break
                    
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(5)

        if final_response:
            break 

    else:
        print("Error: maximum iterations reached without a final response")
        exit(1)

if __name__ == "__main__":
    main()
