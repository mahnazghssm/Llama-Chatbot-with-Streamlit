# Llama Chatbot with Streamlit

A simple chatbot built with Streamlit and connected to a locally running Llama model through Ollama.

## Features

- Chat interface built with Streamlit
- Conversation history using Streamlit session state
- Llama model integration through the Ollama API
- Local model execution

## Project Structure

```text id="kq5n8w"
Llama-Chatbot-with-Streamlit/
├── README.md
├── requirements.txt
├── .gitignore
└── src/
    ├── app.py
    └── utils.py
```

## Installation

### 1. Clone the repository

```bash id="4v9p1k"
git clone https://github.com/mahnazghssm/Llama-Chatbot-with-Streamlit.git
cd Llama-Chatbot-with-Streamlit
```

### 2. Create a virtual environment

```bash id="2q5x7c"
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash id="7g8m2d"
pip install -r requirements.txt
```

### 4. Set up Ollama

Make sure Ollama is installed and running on your computer.

The project uses the `llama2` model. If you don't already have it, pull the model with:

```bash id="f8q3vz"
ollama pull llama2
```

Make sure the Ollama API is running on:

```text id="d3n6rt"
http://localhost:11434
```

### 5. Run the application

```bash id="w4m7yx"
streamlit run src/app.py
```

The application will open in your browser at:

```text id="c2k9pl"
http://localhost:8501
```

## How It Works

The Streamlit app takes the user's message and sends it to the local Llama model through the Ollama API.

`app.py` handles the chat interface and conversation history, while `utils.py` contains the function used to send requests to the Ollama API. If Ollama isn't running or the request fails, the error is shown in the chat instead of crashing the app.

## Requirements

- Python 3.8+
- Streamlit
- Requests
- Ollama
- Llama 2 model

## Future Improvements

- Add streaming responses
- Allow users to select different Llama models

## License

This project is licensed under the MIT License.
