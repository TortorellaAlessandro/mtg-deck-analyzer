import pandas as pd

from deck_loader import load_deck
from scryfall_api import get_card_info
from analyzer import mana_curve, color_distribution
from visualizer import plot_mana_curve, plot_color_distribution

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
    deck = load_deck("VStudioCode\mtg-deck-analyzer\data\hakbal.txt")
    enriched_deck = add_info(deck)

    df = pd.DataFrame(enriched_deck)

    curve = mana_curve(df)
    plot_mana_curve(curve)

    colors = color_distribution(df)
    plot_color_distribution(colors)