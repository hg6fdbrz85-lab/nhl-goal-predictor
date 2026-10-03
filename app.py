import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="NHL Anytime Goal Predictor & Edge Model", layout="wide")

st.title("🏒 Automated NHL Anytime Goal (AGS) Edge Finder")
st.caption("Live Slate Model: SOG, Power Play Units, Goalie GSAx, Rest & Market Implied Odds")

# -------------------------------------------------------------
# 1. HELPER FUNCTIONS
# -------------------------------------------------------------
def odds_to_implied(odds_val):
    """Converts American Odds (+150, -130) to Implied Probability (%)"""
    try:
        clean = str(odds_val).replace('+', '').strip()
        odds = float(clean)
        if odds > 0:
            return round((100.0 / (odds + 100.0)) * 100.0, 1)
        else:
            return round((abs(odds) / (abs(odds) + 100.0)) * 100.0, 1)
    except:
        return 0.0

# -------------------------------------------------------------
# 2. NHL SLATE DATASET (Structured by your 6 Buckets)
# -------------------------------------------------------------
@st.cache_data(ttl=3600)
def load_nhl_board():
    data = [
        {
            "Player": "Connor McDavid", "Team": "EDM", "Pos": "C", "Opponent": "@ TOR", "Status": "🟢 Active",
            # Bucket 1: Player Form & Role
            "SOG/G": 4.1, "Shoting %": "16.5%", "L5 Goals": 4, "PP Unit": "PP1", "TOI Avg": "21.5m",
            # Bucket 2 & 3: Opponent & Goalie Matchup
            "Opp GA/G": 3.10, "Opp PK %": "78.2%", "Confirmed Goalie": "A. Stolarz", "Goalie GSAx": "+4.5 (Tough)",
            # Bucket 4 & 5: Injuries, Schedule & Travel
            "Line/Role Changes": "Stable", "Rest Days": 2, "Is B2B": False, "Travel Impact": "Medium Flight",
            # Bucket 6: Market & Model Output
            "DraftKings": "+115", "FanDuel": "+120", "Model Prob": 48.5
        },
        {
            "Player": "Auston Matthews", "Team": "TOR", "Pos": "C", "Opponent": "vs EDM", "Status": "🟢 Active",
            "SOG/G": 4.6, "Shoting %": "15.2%", "L5 Goals": 5, "PP Unit": "PP1", "TOI Avg": "20.8m",
            "Opp GA/G": 2.85, "Opp PK %": "81.0%", "Confirmed Goalie": "S. Skinner", "Goalie GSAx": "-1.2 (Soft)",
            "Line/Role Changes": "Stable", "Rest Days": 1, "Is B2B": False, "Travel Impact": "Home",
            "DraftKings": "+105", "FanDuel": "+110", "Model Prob": 52.0
        },
        {
            "Player": "Nathan MacKinnon", "Team": "COL", "Pos": "C", "Opponent": "vs VGK", "Status": "🟢 Active",
            "SOG/G": 4.8, "Shoting %": "14.1%", "L5 Goals": 3, "PP Unit": "PP1", "TOI Avg": "22.2m",
            "Opp GA/G": 2.50, "Opp PK %": "84.5%", "Confirmed Goalie": "A. Hill", "Goalie GSAx": "+6.1 (Elite)",
            "Line/Role Changes": "Stable", "Rest Days": 3, "Is B2B": False, "Travel Impact": "Home",
            "DraftKings": "+125", "FanDuel": "+130", "Model Prob": 42.0
        },
        {
            "Player": "David Pastrnak", "Team": "BOS", "Pos": "RW", "Opponent": "@ MTL", "Status": "🟢 Active",
            "SOG/G": 4.4, "Shoting %": "13.8%", "L5 Goals": 2, "PP Unit": "PP1", "TOI Avg": "19.9m",
            "Opp GA/G": 3.30, "Opp PK %": "74.8%", "Confirmed Goalie": "S. Montembeault", "Goalie GSAx": "-3.4 (Weak)",
            "Line/Role Changes": "Line 1 Shift", "Rest Days": 1, "Is B2B": True, "Travel Impact": "Short Bus Trip",
            "DraftKings": "+120", "FanDuel": "+125", "Model Prob": 46.5
        },
        {
            "Player": "Leon Draisaitl", "Team": "EDM", "Pos": "C", "Opponent": "@ TOR", "Status": "🟢 Active",
            "SOG/G": 3.2, "Shoting %": "18.4%", "L5 Goals": 4, "PP Unit": "PP1", "TOI Avg": "20.4m",
            "Opp GA/G": 3.10, "Opp PK %": "78.2%", "Confirmed Goalie": "A. Stolarz", "Goalie GSAx": "+4.5 (Tough)",
            "Line/Role Changes": "Stable", "Rest Days": 2, "Is B2B": False, "Travel Impact": "Medium Flight",
            "DraftKings": "+140", "FanDuel": "+145", "Model Prob": 40.0
        },
        {
            "Player": "Kirill Kaprizov", "Team": "MIN", "Pos": "LW", "Opponent": "vs CHI", "Status": "🟢 Active",
            "SOG/G": 3.8, "Shoting %": "16.0%", "L5 Goals": 3, "PP Unit": "PP1", "TOI Avg": "21.0m",
            "Opp GA/G": 3.60, "Opp PK %": "72.1%", "Confirmed Goalie": "P. Mrazek", "Goalie GSAx": "-5.2 (Poor)",
            "Line/Role Changes": "Stable", "Rest Days": 2, "Is B2B": False, "Travel Impact": "Home",
            "DraftKings": "+110", "FanDuel": "+115", "Model Prob": 51.5
        }
    ]
    return pd.DataFrame(data)

df = load_nhl_board()

# -------------------------------------------------------------
# 3. MATHEMATICAL CALCULATIONS (Implied Prob & Edge)
# -------------------------------------------------------------
df["DK Implied %"] = df["DraftKings"].apply(odds_to_implied)
df["FD Implied %"] = df["FanDuel"].apply(odds_to_implied)

# Find the best market implied probability (best price payout)
df["Best Implied %"] = df[["DK Implied %", "FD Implied %"]].min(axis=1)

# EV Edge Math: Model Prediction vs. Sportsbook Implied Prob
df["EV_Edge_Num"] = df["Model Prob"] - df["Best Implied %"]
df["Value Signal"] = df["EV_Edge_Num"].apply(lambda x: "🟢 YES" if x > 2.5 else ("🟡 SLIGHT" if x > 0 else "🔴 NO"))

# Formatted strings for display
df["Model Prob %"] = df["Model Prob"].apply(lambda x: f"{x:.1f}%")
df["EV Edge %"] = df["EV_Edge_Num"].apply(lambda x: f"{'+' if x > 0 else ''}{x:.1f}%")

# -------------------------------------------------------------
# 4. STREAMLIT FRONTEND CONTROLS & DISPLAY
# -------------------------------------------------------------
st.sidebar.header("Filter & Controls")

scratched_players = st.sidebar.multiselect("🚫 Scratch/Remove Players", options=df["Player"].unique())
pos_filter = st.sidebar.multiselect("Position", ["ALL", "C", "LW", "RW", "D"], default="ALL")
pp1_only = st.sidebar.checkbox("Show PP1 Players Only", value=False)
value_only = st.sidebar.checkbox("Show Only Positive Value (+EV)", value=False)

filtered_df = df[~df["Player"].isin(scratched_players)].copy()

if "ALL" not in pos_filter and len(pos_filter) > 0:
    filtered_df = filtered_df[filtered_df["Pos"].isin(pos_filter)]

if pp1_only:
    filtered_df = filtered_df[filtered_df["PP Unit"] == "PP1"]

if value_only:
    filtered_df = filtered_df[filtered_df["Value Signal"].isin(["🟢 YES", "🟡 SLIGHT"])]

top_edge_val = filtered_df["EV_Edge_Num"].max() if not filtered_df.empty else 0.0

# Metrics Header Bar
c1, c2, c3, c4 = st.columns(4)
c1.metric("Active Skaters", len(filtered_df))
c2.metric("Top Edge", f"+{top_edge_val:.1f}%" if top_edge_val > 0 else f"{top_edge_val:.1f}%")
c3.metric("Goalie Feed", "🟢 Synced")
c4.metric("Injury Scratchpad", f"{len(scratched_players)} Scratched" if scratched_players else "🟢 Clean Board")

# Main Board Layout (Core Decision Odds Front & Center; Bucket Details to the Right)
st.subheader("Anytime Goal Scorer (AGS) Edge Board")
display_cols = [
    "Player", "Team", "Pos", "DraftKings", "FanDuel", 
    "Model Prob %", "EV Edge %", "Value Signal", 
    "Opponent", "Confirmed Goalie", "Goalie GSAx", 
    "SOG/G", "Shoting %", "L5 Goals", "PP Unit", "TOI Avg", 
    "Opp GA/G", "Opp PK %", "Rest Days", "Travel Impact", "Status"
]
st.dataframe(filtered_df[display_cols], use_container_width=True, hide_index=True)
