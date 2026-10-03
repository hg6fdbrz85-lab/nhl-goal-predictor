import streamlit as st
import pandas as pd

st.set_page_config(page_title="NHL Goal Props Edge Finder", layout="wide")

st.title("🏒 NHL Anytime Goal Scorer Edge Finder")
st.caption("Dedicated Workspace: Goal Props, Live Pricing, L3G Form & Matchups")

# -------------------------------------------------------------
# 1. GOAL PROPS MASTER SLATE ONLY
# -------------------------------------------------------------
@st.cache_data(ttl=3600)
def load_nhl_goal_board():
    data = [
        {
            "Player": "Nathan MacKinnon", "Team": "COL", "Pos": "F", "Opponent": "vs CHI",
            "Prop": "Anytime Goal", "DK Odds": "-105", "FD Odds": "-115",
            "Model Prob": "52.4%", "L3G Goals": "1.3", "L3G SOG": "4.8", "Matchup": "24th (Weak)"
        },
        {
            "Player": "Connor McDavid", "Team": "EDM", "Pos": "F", "Opponent": "@ CGY",
            "Prop": "Anytime Goal", "DK Odds": "+110", "FD Odds": "+105",
            "Model Prob": "49.1%", "L3G Goals": "1.0", "L3G SOG": "4.5", "Matchup": "28th (Weak)"
        },
        {
            "Player": "Auston Matthews", "Team": "TOR", "Pos": "F", "Opponent": "vs MTL",
            "Prop": "Anytime Goal", "DK Odds": "-115", "FD Odds": "-120",
            "Model Prob": "54.8%", "L3G Goals": "1.5", "L3G SOG": "5.2", "Matchup": "21st (Weak)"
        },
        {
            "Player": "David Pastrnak", "Team": "BOS", "Pos": "F", "Opponent": "@ BUF",
            "Prop": "Anytime Goal", "DK Odds": "+125", "FD Odds": "+120",
            "Model Prob": "46.2%", "L3G Goals": "0.9", "L3G SOG": "5.0", "Matchup": "14th (Avg)"
        },
        {
            "Player": "Leon Draisaitl", "Team": "EDM", "Pos": "F", "Opponent": "@ CGY",
            "Prop": "Anytime Goal", "DK Odds": "+120", "FD Odds": "+115",
            "Model Prob": "47.5%", "L3G Goals": "1.1", "L3G SOG": "3.8", "Matchup": "28th (Weak)"
        }
    ]
    return pd.DataFrame(data)

df = load_nhl_goal_board()

# -------------------------------------------------------------
# 2. STREAMLIT CONTROLS
# -------------------------------------------------------------
st.sidebar.header("Filters")
team_filter = st.sidebar.selectbox("Team", ["ALL"] + list(df["Team"].unique()))

filtered_df = df.copy()
if team_filter != "ALL":
    filtered_df = filtered_df[filtered_df["Team"] == team_filter]

# Compact Metric Bar
col1, col2, col3 = st.columns(3)
col1.metric("Goal Scorers", len(filtered_df))
col2.metric("Featured Anchor", "Nathan MacKinnon")
col3.metric("DK Odds", "-105")

st.markdown("---")

# Main Board Display (Goal props front and center)
display_cols = [
    "Player", "Prop", "DK Odds", "FD Odds", 
    "Team", "Opponent", "Model Prob", "L3G Goals", "L3G SOG", "Matchup"
]
st.dataframe(filtered_df[display_cols], use_container_width=True, hide_index=True)
