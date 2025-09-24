import pandas as pd

# INPUT: Il file path del txt contenente la deck list
# OUTPUT: Un dataframe contenente il nome della carta e la quantita di copie presenti 
def load_deck(filepath: str) -> pd.DataFrame:
    deck = []
    with open(filepath, "r") as decklist:
        for line in decklist:

            line = line.strip()
            if not line:
                continue
            contents = line.split(" ", 1)

            # Caso in cui ho una riga nel formato "Quantità" "Nome Carta"
            if len(contents) == 2 and contents[0].isdigit():
                qty, name = int(contents[0]), contents[1]
            # Caso in cui ho solo il nome della carta e nessuan quantità
            else:
                qty, name = 1, line

            deck.append({"quantity": qty, "name": name})
        return pd.DataFrame(deck)
    
def read_deck(decklist: str) -> pd.DataFrame:
    deck = []
    cards = decklist.splitlines()
    for card in cards:
        card = card.strip()
        if not card:
            continue
        contents = card.split(" ", 1)
        
        # Caso in cui ho una riga nel formato "Quantità" "Nome Carta"
        if len(contents) == 2 and contents[0].isdigit():
            qty, name = int(contents[0]), contents[1]

        # Caso in cui ho solo il nome della carta e nessuan quantità
        else:
            qty, name = 1, card
        deck.append({"quantity": qty, "name": name})
    return pd.DataFrame(deck)

#There is still room for optimizations