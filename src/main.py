import argparse
import html
import json
import ollama
import tiktoken
from typing import Optional


PROGRAM_NAME = "SummAIry"
VERSION = "0.0.1"

default_question = "Summarize the following text:"
default_model = 'llama3.1:8b'

def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize text files", add_help=True)
    parser.add_argument("-v", "--version", action="version", version=f"{PROGRAM_NAME} - version {VERSION}")
    
    mutually_exclusive_group = parser.add_mutually_exclusive_group(required=False)
    mutually_exclusive_group.add_argument("-lsm", "--list-models", action='store_true')
    mutually_exclusive_group.add_argument("-f", "--file", type=str, help="Path to input file")
    mutually_exclusive_group.add_argument("-t", "--text", type=str, help="Raw text input")
    
    parser.add_argument("-q", "--question", type=str, nargs="?", default=default_question,
                    help=f"Optional: Custom question instead of '{default_question}'")
    parser.add_argument("-m", "--model", type=str, nargs="?", default=default_model,
                    help=f"Optional: Custom Ollama model instead of '{default_model}'")
    parser.add_argument("-c", "--chunked", action="store_true",
                    help="Split text into chunks and summarize each one separately")

    args = parser.parse_args()

    if args.list_models:
        list_models()
    elif args.file is not None and args.text is None:    
        with open(args.file, 'r') as f:
            content = f.read()
        print(summarize_file(args.model, args.question, args.chunked, content))
    elif args.text is not None and args.file is None:
        print(summarize_file(args.model, args.question, args.chunked, args.text))
    else:
        print("No input file provided.")

def list_models() -> None:
    response = ollama.list()
    print("Available models:")
    for model in response.models:
        print('-', model.model)

def summarize_file(model: str, question: str, chunked: bool, content: str) -> str:
    # Hardcoded conservative limit for chunk size
    # Ollama doesn't support fetching the current context length to calculate it
    # See https://github.com/ollama/ollama/issues/3582
    max_chunk_size = 3072
    
    if chunked:
        chunks = get_token_chunks(content, max_chunk_size)
        
        summaries = []
        for chunk in chunks:
            try:
                response: ollama.ChatResponse = ollama.chat(model=model, messages=[
                    {
                        'role': 'user',
                        'content': f'{question}\n{chunk}'
                    },
                ])
                summaries.append(response.message.content)
            except ollama.ResponseError as e:
                print(f"Error summarizing chunked text: {e}")
        
        return "\n".join(summaries)
    else:
        try:
            response: ollama.ChatResponse = ollama.chat(model=model, messages=[
                {
                    'role': 'user',
                    'content': f'{question}\n{content}'
                },
            ])
            return response.message.content
        except ollama.ResponseError as e:
            print(f"Error summarizing text: {e}")
            return ""
        
# Use tiktoken with gpt2 tolkenizer to chunk text as hacky workaround/hacky solution
# Another solution would be to download the tokenizer.json with HuggingFace Tokenizer library
# when the model is available there
def get_token_chunks(text: str, max_tokens: int, model_name: str = 'gpt2') -> list[str]:
    enc = tiktoken.get_encoding(model_name)
    tokens = enc.encode(text)
    chunks = [tokens[i:i+max_tokens] for i in range(0, len(tokens), max_tokens)]
    return [enc.decode(chunk) for chunk in chunks]


if __name__ == "__main__":
    main()