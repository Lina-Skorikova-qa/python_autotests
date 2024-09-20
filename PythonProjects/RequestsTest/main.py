import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f3229dda0b5741ab72e64f79a10c248c'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN}
body_create =  {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_update = {
    "pokemon_id": "73034",
    "name": "Пикачус",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "73034"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_update = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_update)
print(response_update.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)


