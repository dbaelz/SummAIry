# SummAIry - Summarize text files
Command line tool to summarize text files using AI with a local Ollama instance. The project is mainly developed with AI itself using Visual Studio Code, the [Continue.dev extension](https://www.continue.dev/), local Ollama instance and Python. So it's more a playground for developing with AI assistant (as agent and chat), using AI tools and learning about AI itself.

## Features
- Summarize text files using AI
  - `--model MODEL` argument to select model (default `llama3.1:8b`)
  - `--file FILE` argument to select file
  - `--text "a text"` argument to provide a text
  - `--question QUESTION` argument to select question (default `Summarize the following text:`)
- List all available models with `--list-models`

## Example usage
To summarize a text file using the default settings, you can run:
- `python src/main.py --file example/python-ai.md`
- `python src/main.py --file example/python-ai.md --question "Count how many times AI is mentioned in this text:"`
- `python src/main.py --file example/python-ai.md --model qwen2.5`
- `python src/main.py --text "strawberry" --question "How many letter 'R' are in this text:"`

List all available models:
- `python src/main.py --list-models`

## Installation
1. Install Python (3.8 or higher)
2. Clone this repository
3. Run `pip install -r requirements.txt`
4. Run `python src/main.py`

## Requirements
- Ollama installed and running locally
- Optional: Default model is `llama3.1:8b`. Otherwise it's necessary to specifiy the model with the `--model` argument.


## Contribution
Feel free to contribute via pull requests.

## License
The project is licensed by the [Apache 2 license](LICENSE).