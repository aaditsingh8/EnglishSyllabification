import os
from dotenv import load_dotenv
import requests

load_dotenv()

# Merriam-Webster Dictionary API
API_KEY = os.getenv('API_KEY')


def create_dictionary_request(word: str):
    url = f'https://dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={API_KEY}'
    response = requests.get(url)
    result = response.json()
    try:
        return result[0]['hwi']['hw']
    except (KeyError, TypeError):
        return None


if __name__ == '__main__':
    print(create_dictionary_request('degenerate'))
