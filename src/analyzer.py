import pandas as pd

def mana_curve(deck: pd.DataFrame) -> pd.Series:
    return deck.groupby("cmc")["quantity"].sum()

def color_distribution(deck: pd.DataFrame) -> pd.Series:
    return deck.explode("colors").groupby("colors")["quantity"].sum()