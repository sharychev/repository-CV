import requests

host = 'https://api.pokemonbattle.me:9104'
token = '6a012dd463c01f331265c080674268fc'


response_new_poke = requests.post(f'{host}/pokemons', json={
    "name": "Бенладен",
    "photo": "https://dolnikov.ru/pokemons/albums/069.png"
}, headers={'trainer_token':token})

print(response_new_poke.json())


response_change_poke = requests.put(f'{host}/pokemons', json={
    "pokemon_id": "11151",
    "name": "Батистута",
    "photo": "https://dolnikov.ru/pokemons/albums/099.png"
}, headers={'Content-Type':'application/json', 'trainer_token':token})

print(response_change_poke.json())


response_add_poke = requests.post(f'{host}/trainers/add_pokeball', json={
    "pokemon_id": "11151"
}, headers={'Content-Type':'application/json', 'trainer_token':token})

print(response_add_poke.json())
