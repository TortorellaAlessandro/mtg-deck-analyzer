import streamlit as st
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
    graphs_ready = False

    st.header("Deck Analyzer")

    file_name = st.text_input("Insert the name of the .txt file", "hakbal.txt")
    
    if st.button("Load decklist") and file_name:
        path = os.path.join(BASE_DIR, "data", file_name)
        deck = load_deck(path)
        enriched_deck = add_info(deck)

        df = pd.DataFrame(enriched_deck)

        curve = mana_curve(df)
        colors = color_distribution(df)

        graphs_ready = True

    tab_curve, tab_colors = st.tabs(["Mana Curve", "Color Distribution"])

    with tab_curve:
        if graphs_ready:
            st.bar_chart(curve)
    with tab_colors:
        if graphs_ready:
            st.bar_chart(colors)