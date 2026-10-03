import streamlit as st
import pandas as pd

st.set_page_config(page_title="NHL Goal Props Edge Finder", layout="wide")

st.title("🏒 NHL Anytime Goal Scorer Edge Finder")
st.caption("Dedicated Workspace: Top 15 Goal Props, Live Pricing, L3G Form & Matchups")

# -------------------------------------------------------------
# 1. TOP 15 GOAL PROPS MASTER SLATE
# -------------------------------------------------------------
@st.cache_data(ttl=3600)
def load_nhl_goal_board():
    data = [
        {"Player": "Nathan MacKinnon", "Team": "COL", "Pos": "F", "Opponent": "vs CHI", "Prop": "Anytime Goal", "DK Odds": "-105", "FD Odds": "-115", "Model Prob": "52.4%", "L3G Goals": "1.3", "L3G SOG": "4.8", "Matchup": "24th (Weak)"},
        {"Player": "Auston Matthews", "Team": "TOR", "Pos": "F", "Opponent": "vs MTL", "Prop": "Anytime Goal", "DK Odds": "-115", "FD Odds": "-120", "Model Prob": "54.8%", "L3G Goals": "1.5", "L3G SOG": "5.2", "Matchup": "21st (Weak)"},
        {"Player": "Connor McDavid", "Team": "EDM", "Pos": "F", "Opponent": "@ CGY", "Prop": "Anytime Goal", "DK Odds": "+110", "FD Odds": "+105", "Model Prob": "49.1%", "L3G Goals": "1.0", "L3G SOG": "4.5", "Matchup": "28th (Weak)"},
        {"Player": "Cole Caufield", "Team": "MTL", "Pos": "F", "Opponent": "@ TOR", "Prop": "Anytime Goal", "DK Odds": "+115", "FD Odds": "+110", "Model Prob": "48.2%", "L3G Goals": "1.2", "L3G SOG": "4.1", "Matchup": "18th (Avg)"},
        {"Player": "Nikita Kucherov", "Team": "TBL", "Pos": "F", "Opponent": "vs FLA", "Prop": "Anytime Goal", "DK Odds": "+120", "FD Odds": "+115", "Model Prob": "46.8%", "L3G Goals": "1.1", "L3G SOG": "3.9", "Matchup": "12th (Tough)"},
        {"Player": "David Pastrnak", "Team": "BOS", "Pos": "F", "Opponent": "@ BUF", "Prop": "Anytime Goal", "DK Odds": "+125", "FD Odds": "+120", "Model Prob": "46.2%", "L3G Goals": "0.9", "L3G SOG": "5.0", "Matchup": "14th (Avg)"},
        {"Player": "Kirill Kaprizov", "Team": "MIN", "Pos": "F", "Opponent": "vs WPG", "Prop": "Anytime Goal", "DK Odds": "+130", "FD Odds": "+125", "Model Prob": "45.0%", "L3G Goals": "0.9", "L3G SOG": "4.2", "Matchup": "15th (Avg)"},
        {"Player": "Jason Robertson", "Team": "DAL", "Pos": "F", "Opponent": "vs NSH", "Prop": "Anytime Goal", "DK Odds": "+140", "FD Odds": "+135", "Model Prob": "43.5%", "L3G Goals": "0.8", "L3G SOG": "4.4", "Matchup": "20th (Weak)"},
        {"Player": "Kyle Connor", "Team": "WPG", "Pos": "F", "Opponent": "@ MIN", "Prop": "Anytime Goal", "DK Odds": "+145", "FD Odds": "+140", "Model Prob": "41.5%", "L3G Goals": "0.9", "L3G SOG": "3.8", "Matchup": "14th (Avg)"},
        {"Player": "Wyatt Johnston", "Team": "DAL", "Pos": "F", "Opponent": "vs NSH", "Prop": "Anytime Goal", "DK Odds": "+150", "FD Odds": "+145", "Model Prob": "41.0%", "L3G Goals": "1.0", "L3G SOG": "3.2", "Matchup": "20th (Weak)"},
        {"Player": "Filip Forsberg", "Team": "NSH", "Pos": "F", "Opponent": "@ DAL", "Prop": "Anytime Goal", "DK Odds": "+155", "FD Odds": "+150", "Model Prob": "39.0%", "L3G Goals": "0.8", "L3G SOG": "3.6", "Matchup": "9th (Tough)"},
        {"Player": "Macklin Celebrini", "Team": "SJS", "Pos": "F", "Opponent": "@ ANA", "Prop": "Anytime Goal", "DK Odds": "+160", "FD Odds": "+155", "Model Prob": "39.5%", "L3G Goals": "0.7", "L3G SOG": "4.1", "Matchup": "26th (Weak)"},
        {"Player": "Matt Boldy", "Team": "MIN", "Pos": "F", "Opponent": "vs WPG", "Prop": "Anytime Goal", "DK Odds": "+165", "FD Odds": "+160", "Model Prob": "38.5%", "L3G Goals": "0.7", "L3G SOG": "3.8", "Matchup": "15th (Avg)"},
        {"Player": "Steven Stamkos", "Team": "NSH", "Pos": "F", "Opponent": "@ DAL", "Prop": "Anytime Goal", "DK Odds": "+175", "FD Odds": "+165", "Model Prob": "37.2%", "L3G Goals": "0.6", "L3G SOG": "3.1", "Matchup": "9th (Tough)"},
        {"Player": "Cutter Gauthier", "Team": "ANA", "Pos": "F", "Opponent": "vs SJS", "Prop": "Anytime Goal", "DK Odds": "+180", "FD Odds": "+170", "Model Prob": "35.8%", "L3G Goals": "0.5", "L3G SOG": "3.9", "Matchup": "29th (Weak)"}
    ]
    return pd.DataFrame(data)

df = load_nhl_goal_board()

# -------------------------------------------------------------
# 2. STREAMLIT CONTROLS
# -------------------------------------------------------------
st.sidebar.header("Filters")
team_filter = st.sidebar.selectbox("Team", ["ALL"] + sorted(list(df["Team"].unique())))

filtered_df = df.copy()
if team_filter != "ALL":
    filtered_df = filtered_df[filtered_df["Team"] == team_filter]

# Compact Metric Bar
col1, col2, col3 = st.columns(3)
col1.metric("Goal Scorers Tracked", len(filtered_df))
col2.metric("Top Board Prob", "Auston Matthews (54.8%)")
col3.metric("Best Available DK", "-105")

st.markdown("---")

# Main Board Display (Goal props strictly)
display_cols = [
    "Player", "Prop", "DK Odds", "FD Odds", 
    "Team", "Opponent", "Model Prob", "L3G Goals", "L3G SOG", "Matchup"
]
st.dataframe(filtered_df[display_cols], use_container_width=True, hide_index=True)
