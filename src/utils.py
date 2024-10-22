"""
Author: Mahnaz Ghassemi
Date created: 2024-10-21
Description: This module provides a function to call the Llama model API
"""

import json  # Import the json module for JSON data manipulation
from typing import Dict, Union  # Import types for function annotations

import requests  # Import the requests library to handle HTTP requests


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
    url = "http://localhost:11434/api/generate"  # API endpoint for generating responses
    data = {  # Create a dictionary to hold the data for the request
        "model": model,
        "prompt": prompt,
        "stream": stream
    }
    
    json_data = json.dumps(data)  # Convert the data dictionary to a JSON string
    response = requests.post(url, data=json_data, headers={"content-type": "application/json"})  # Send a POST request

    if response.status_code == 200:  # Check if the request was successful
        return response.json()  # Return the JSON response if the request was successful
    else:
        return f"Error: {response.status_code}"  # Return an error message if the request failed