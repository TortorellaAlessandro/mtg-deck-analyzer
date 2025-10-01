import streamlit as st

from analyzer import mana_curve, color_distribution, creatures_stats, type_distribution

if __name__ == "__main__":
    st.set_page_config(initial_sidebar_state="collapsed", layout= "wide")

    left, right = st.columns([1, 2])


    df, enriched_deck, commander_image_url = st.session_state.info

    with left:
        st.image(commander_image_url)

    with right:
        tab_curve, tab_colors, tab_type, tab_stats = st.tabs(["Mana Curve", "Color Distribution","Type Distribution", "Stats Distribution"])
        with tab_curve:
            st.bar_chart(mana_curve(df))
        with tab_colors:
            st.bar_chart(color_distribution(df))
        with tab_type:
            st.bar_chart(type_distribution(df))
        with tab_stats:
            st.bar_chart(creatures_stats(df))