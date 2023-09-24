import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '6a012dd463c01f331265c080674268fc'


def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id':2363})
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(f'{host}/trainers', params={'trainer_id':2363})
    assert response.json()['trainer_name'] == 'Howard'


