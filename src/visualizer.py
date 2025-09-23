import matplotlib.pyplot as plt

def plot_mana_curve(curve):
    fig, ax = plt.subplots(figsize=(8,4))
    curve.plot(kind="bar", ax=ax, title="Mana Curve")
    ax.set_xlabel("Converted Mana Cost")
    ax.set_ylabel("Number of Cards")
    plt.close(fig)   
    return fig

def plot_color_distribution(colors):
    fig, ax = plt.subplots(figsize=(6,6))
    colors.plot(
        kind="pie", 
        autopct="%.1f%%", 
        ax=ax,
        title="Color Distribution"
    )
    ax.set_ylabel("")
    plt.close(fig)  
    return fig