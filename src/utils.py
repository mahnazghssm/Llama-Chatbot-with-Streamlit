"""
Author: Mahnaz Ghassemi
Date created: 2024-10-21
Description: This module provides a function to call the Llama model API
"""

import json
from typing import Dict, Union
import requests


def call_llama(model: str, prompt: str, stream: bool = False) -> Union[Dict, str]:
    """
    Call the Llama model API to generate a response based on the provided prompt.

    Args:
        model (str): The name of the model to use (e.g., "llama2").
        prompt (str): The input text prompt to send to the model.
        stream (bool): Whether to stream the response. Defaults to False.

    Returns:
        Union[Dict, str]: 
            - If successful, returns a dictionary containing the model's response.
            - If an error occurs, returns an error message string.
    """
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": stream
    }

    try:
        response = requests.post(url, json=data, headers={"Content-Type": "application/json"})
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        return f"Error: {str(e)}"
