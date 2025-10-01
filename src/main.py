import streamlit as st
import pandas as pd
import os

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
            if _ == 0:
                commander_image_url = info["image_uris"]["png"]

            cards.append(
                {
                    "name": info["name"],
                    "quantity": card["quantity"],
                    "cmc": info["cmc"],
                    "colors": info.get("colors", "Colorless"),
                    "power/toughness": info.get("power", "-1") + "/" + info.get("toughness", "-1"),
                    "type": determine_card_type(info["type_line"])
                })
    return (cards, commander_image_url)

if __name__ == "__main__":
    graphs_ready = False
    cards_provided = False

    st.header("Deck Analyzer")

    input_mode = st.selectbox(
        "Choose the input mode:",
        ("Card list", "Upload txt")
    )

    if input_mode == "Card list":
        decklist = st.text_area("Copy decklist here")
        if st.button("Load decklist") and decklist:
            cards_provided = True

    elif input_mode == "Upload txt":
        uploaded_file = st.file_uploader("Upload .txt decklist", ["txt"])
    
        if st.button("Load decklist") and uploaded_file is not None:
            decklist = uploaded_file.read().decode("utf-8")
            cards_provided = True

    if cards_provided:    
        deck = read_deck(decklist)
        enriched_deck, commander_image_url = add_info(deck)
        df = pd.DataFrame(enriched_deck)

        st.session_state["info"] = (df, enriched_deck, commander_image_url)
        
        st.switch_page("pages/analysis_page.py")

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