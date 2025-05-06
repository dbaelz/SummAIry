import argparse
import html
import json
import ollama
from typing import Optional


PROGRAM_NAME = "SummAIry"
VERSION = "0.0.1"

default_question = "Summarize the following text:\n"
default_model = 'llama3.1:8b'

def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize text files", add_help=True)
    parser.add_argument("-v", "--version", action="version", version=f"{PROGRAM_NAME} - version {VERSION}")
    
    mutually_exclusive_group = parser.add_mutually_exclusive_group(required=False)
    mutually_exclusive_group.add_argument("-lsm", "--list-models", action='store_true')
    mutually_exclusive_group.add_argument("-f", "--file", type=str, help="Path to input file")
    
    parser.add_argument("-q", "--question", type=str, nargs="?", default=default_question,
                    help=f"Optional: Custom question instead of '{default_question}'")
    parser.add_argument("-m", "--model", type=str, nargs="?", default=default_model,
                    help=f"Optional: Custom Ollama model instead of '{default_model}'")


    args = parser.parse_args()

    if args.list_models:
        list_models()
    elif args.file:        
        print(summarize_file(args.model, args.question, args.file))
    else:
        print("No input file provided.")

def list_models() -> None:
    response = ollama.list()
    print("Available models:")
    for model in response.models:
        print('-', model.model)

def summarize_file(model: str, question: str, input_file: str) -> str:    
    with open(input_file, 'r') as f:
        content = f.read()


    try:
        response: ollama.ChatResponse = ollama.chat(model=model, messages=[
            {
                'role': 'user',
                'content': f'{question}\n{content}'
            },
        ])
        return response.message.content
    except ollama.ResponseError as e:
        print(f"Error: {e}")
        return ""
    

if __name__ == "__main__":
    main()