import matplotlib.pyplot as plt

def plot_mana_curve(curve):
    curve.plot(kind="bar", figsize=(8,4), title="Mana Curve")
    plt.xlabel("Converted Mana Cost")
    plt.ylabel("Number of Cards")
    plt.show()

def plot_color_distribution(colors):
    colors.plot(kind="pie", autopct="%.1f%%", figsize=(6,6), title="Color Distribution")
    plt.ylabel("")
    plt.show()