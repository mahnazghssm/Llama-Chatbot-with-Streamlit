"""
Llama model API utilities.

Author: Mahnaz Ghassemi
Date created: 2024-10-21
"""

import json
from typing import Dict, Union

import requests


def call_llama(model: str, prompt: str, stream: bool = False) -> Union[Dict, str]:
    """Call the Llama model API and return its response."""
    url = "http://localhost:11434/api/generate"

    data = {
        "model": model,
        "prompt": prompt,
        "stream": stream,
    }

    json_data = json.dumps(data)

    response = requests.post(
        url,
        data=json_data,
        headers={"content-type": "application/json"},
    )

    if response.status_code == 200:
        return response.json()

    return f"Error: {response.status_code}"
