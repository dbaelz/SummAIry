import argparse
import html
import json
from typing import Optional

from ollama import chat
from ollama import ChatResponse
from ollama import ResponseError

default_question = "Summarize the following text:"
default_model = 'llama3.1:8b'

def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize text files")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.0.1")
    
    parser.add_argument("input_file", type=str, help="Path to input file")
    parser.add_argument("-q", "--question", type=str, nargs="?", default=default_question,
                    help="Optional: Custom question instead of '${default_question}'")
    parser.add_argument("-m", "--model", type=str, nargs="?", default=default_model,
                    help="Optional: Custom Ollama model instead of '${default_model}'")


    args = parser.parse_args()

    if args.input_file:        
        print(summarize_file(args.model, args.question, args.input_file))
    else:
        print("No input file provided.")

def summarize_file(model: str, question: str, input_file: str) -> str:    
    with open(input_file, 'r') as f:
        content = f.read()


    try:
        response: ChatResponse = chat(model=model, messages=[
            {
                'role': 'user',
                'content': f'{question}\n{content}'
            },
        ])
        return response.message.content
    except ResponseError as e:
        print(f"Error: {e}")
        return ""
    

if __name__ == "__main__":
    main()