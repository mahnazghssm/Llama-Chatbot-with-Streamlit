# Llama Chatbot with Streamlit

A simple chatbot built with Streamlit and connected to a locally running Llama model through Ollama.

## Features

- Chat interface built with Streamlit
- Conversation history using Streamlit session state
- Llama model integration through the Ollama API
- Local model execution

## Project Structure

```text
Llama_Chatbot_with_Streamlit/
├── README.md
├── requirements.txt
└── src/
    ├── app.py
    └── utils.py
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mahnazghssm/Llama-Chatbot-with-Streamlit.git
cd Llama-Chatbot-with-Streamlit
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up Ollama

Make sure Ollama is installed and running on your computer.

The project uses the `llama2` model. If you don't already have it, pull the model with:

```bash
ollama pull llama2
```

Make sure the Ollama API is running on:

```text
http://localhost:11434
```

### 5. Run the application

```bash
streamlit run src/app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## How It Works

The Streamlit app takes the user's message and sends it to the local Llama model through the Ollama API.

`app.py` handles the chat interface and conversation history, while `utils.py` contains the function used to send requests to the Ollama API.

## Requirements

- Python 3.8+
- Streamlit
- Requests
- Ollama
- Llama 2 model

## Future Improvements

- Add better error handling for API connection problems
- Add streaming responses
- Allow users to select different Llama models