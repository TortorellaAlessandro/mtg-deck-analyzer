import pandas as pd

def mana_curve(deck: pd.DataFrame) -> pd.Series:
    return deck.groupby("cmc")["quantity"].sum()

def color_distribution(deck: pd.DataFrame) -> pd.Series:
    return deck.explode("colors").groupby("colors")["quantity"].sum()

def type_distribution(deck: pd.DataFrame) -> pd.Series:
    return deck.groupby("type")["quantity"].sum()

def creatures_stats(deck: pd.DataFrame) -> pd.Series:
    return deck[deck["power/toughness"] != "-1/-1"].groupby("power/toughness")["quantity"].sum()
