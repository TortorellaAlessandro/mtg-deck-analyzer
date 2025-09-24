import streamlit as st
import pandas as pd
import os
import sys

from deck_loader import load_deck, read_deck
from scryfall_api import get_card_info
from analyzer import mana_curve, color_distribution, creatures_stats, type_distribution

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def determine_card_type(type_line: str)-> str:
    target = type_line.lower()
    if "creature" in target:
        return "Creature"
    elif "artifact" in target:
        return "Artifact"
    elif "enchantment" in target:
        return "Enchantment"
    elif "instant" in target:
        return "Instant"
    elif "sorcery" in target:
        return "Sorcery"
    elif "planeswalker" in target:
        return "Planeswalker"
    elif "land" in target:
        return "Land"
    else:
        return "Other"

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
                    "colors": info.get("colors", "Colorless"),
                    "power/toughness": info.get("power", "-1") + "/" + info.get("toughness", "-1"),
                    "type": determine_card_type(info["type_line"])
                })
    return cards

if __name__ == "__main__":
    graphs_ready = False
    cards_provided = False

    st.header("Deck Analyzer")

    input_mode = st.selectbox(
        "Choose the input mode:",
        ("Card list", "Local txt")
    )

    if input_mode == "Card list":
        decklist = st.text_area("Copy decklist here")
        if st.button("Load decklist") and decklist:
            deck = read_deck(decklist)
            cards_provided = True

    elif input_mode == "Local txt":
        file_name = st.text_input("Insert the name of the .txt file", "hakbal.txt")
    
        if st.button("Load decklist") and file_name:
            path = os.path.join(BASE_DIR, "data", file_name)
            deck = load_deck(path)
            cards_provided = True

    if cards_provided:    
        enriched_deck = add_info(deck)

        df = pd.DataFrame(enriched_deck)

        graphs_ready = True

    tab_curve, tab_colors, tab_type, tab_stats = st.tabs(["Mana Curve", "Color Distribution","Type Distribution", "Stats Distribution"])
    if graphs_ready:
        with tab_curve:
            st.bar_chart(mana_curve(df))
        with tab_colors:
            st.bar_chart(color_distribution(df))
        with tab_type:
            st.bar_chart(type_distribution(df))
        with tab_stats:
            st.bar_chart(creatures_stats(df))