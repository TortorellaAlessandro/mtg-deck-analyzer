import pandas as pd
import os
import sys

from deck_loader import load_deck
from scryfall_api import get_card_info
from analyzer import mana_curve, color_distribution
from visualizer import plot_mana_curve, plot_color_distribution

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def add_info(deck):
    cards = []
    for _, card in deck.iterrows():
        info = get_card_info(card["name"])
        if "error" not in info:
            cards.append(
                {
                    "name": info["name"],
                    "quantity": card["quantity"],
                    "cmc": info["cmc"],
                    "colors": info["colors"]
                })
    return cards

if __name__ == "__main__":
    #Default decklist
    path = "VStudioCode\mtg-deck-analyzer\data\hakbal.txt"
    #If given from the terminal will analyze the given path
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        path = os.path.join(BASE_DIR, "data", file_name)

    deck = load_deck(path)
    enriched_deck = add_info(deck)

    df = pd.DataFrame(enriched_deck)

    curve = mana_curve(df)
    plot_mana_curve(curve)

    colors = color_distribution(df)
    plot_color_distribution(colors)