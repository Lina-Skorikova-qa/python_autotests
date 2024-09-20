import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f3229dda0b5741ab72e64f79a10c248c'
HEADER = {'Content-type' : 'application/json'}
TRAINER_ID = '10523'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = response = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['id'] == '10523'
