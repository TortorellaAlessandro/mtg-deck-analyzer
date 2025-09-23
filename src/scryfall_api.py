import requests
import json
import os

BASE_URL =  "https://api.scryfall.com/cards/named"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_FILE = os.path.join(BASE_DIR, "data", "cards_cache.json")

# Controllo se esiste la mia cache e nel caso la carico per poterla usare
try:
    with open(CACHE_FILE, "r") as cache_file:
        local_cache = json.load(cache_file)
except json.JSONDecodeError:
    local_cache = {}

def get_card_info(card_name: str) -> dict:
    # Se la carta è gia nella mia cache allora la prendo da lì e basta
    if card_name in local_cache:
        return local_cache[card_name]
    
    #Se la carta non è nella cache allora mandero una richiesta all'api
    response = requests.get(BASE_URL, params={"exact": card_name})
    
    #Se la richiesta ha avuto successo, salvo i dati nella cache locale e ritorno i dati ottenuti
    if response.status_code == 200:
        data = response.json()
        local_cache[card_name] = data
        with open(CACHE_FILE, "w") as cache_file:
            json.dump(local_cache, cache_file, indent= 2)
        return data
    
    #Se la richiesta non va a buon fine allora ritorno un errore
    else:
        return {"name": card_name, "error": "Card not found"}
    