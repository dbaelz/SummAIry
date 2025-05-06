# SumAIrry - Summarize text files
Command line tool to summarize text files using AI with a local Ollama instance. The project is mainly developed with AI itself using Visual Studio Code, the [Continue.dev plugin](https://www.continue.dev/), local Ollama instance and Python. So it's more a playground for developing with AI assistant (and chat), using AI tools and learning about AI itself.

## Features
- Summarize text files using AI
  - `--file FILE` argument to select file
  - `--model MODEL` argument to select model (default `llama3.1:8b`)
  - `--question QUESTION` argument to select question (default `Summarize the following text:`)
- List all available models with `--list-models`

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