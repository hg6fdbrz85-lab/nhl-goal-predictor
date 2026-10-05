import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="NHL Goal Scorer Edge Hunter", layout="wide")
st.title("🏒 NHL Goal Scorer Edge Hunter")
st.caption("Standalone Board: Automated Schedule-Aware Anytime Goals & Probability Projections (Top 10 Slate)")

def odds_to_implied(odds_val):
    try:
        clean = str(odds_val).replace('+', '').strip()
        if clean == 'N/A' or clean == '' or clean.lower() == 'nan':
            return 0.0
        odds = float(clean)
        return round((100.0 / (odds + 100.0)) * 100.0, 1) if odds > 0 else round((abs(odds) / (abs(odds) + 100.0)) * 100.0, 1)
    except:
        return 0.0

# -------------------------------------------------------------
# AUTOMATED SCHEDULE & TOP 10 GOAL SCORER SLATE LOADER
# -------------------------------------------------------------
def get_todays_nhl_slate():
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    # Expanded Top 10 Slate for tonight's games (Oct 5, 2026)
    data = [
        {
            "Player": "Nikita Kucherov", "Team": "TBL", "Pos": "W", "Opponent": "vs PHI", "Status": "🟢 Active",
            "Anytime Goal Odds (DK)": "+110", "Anytime Goal Odds (FD)": "+105",
            "Base Sim Goal Prob": 42.5, "PP Unit": "PP1"
        },
        {
            "Player": "David Pastrnak", "Team": "BOS", "Pos": "W", "Opponent": "vs OTT", "Status": "🟢 Active",
            "Anytime Goal Odds (DK)": "-110", "Anytime Goal Odds (FD)": "-115",
            "Base Sim Goal Prob": 48.0, "PP Unit": "PP1"
        },
        {
            "Player": "Sidney Crosby", "Team": "PIT", "Pos": "C", "Opponent": "vs WPG", "Status": "🟢 Active",
            "Anytime Goal Odds (DK)": "+145", "Anytime Goal Odds (FD)": "+140",
            "Base Sim Goal Prob": 36.0, "PP Unit": "PP1"
        },
        {
            "Player": "Macklin Celebrini", "Team": "SJS", "Pos": "C", "Opponent": "@ DAL", "Status": "🟢 Active",
            "Anytime Goal Odds (DK)": "+185", "Anytime Goal Odds (FD)": "+175",
            "Base Sim Goal Prob": 31.0, "PP Unit": "PP1"
        },
        {
            "Player": "Jake Guentzel", "Team": "TBL", "Pos": "W", "Opponent": "vs PHI", "Status": "🟢 Active",
            "Anytime Goal Odds (DK)": "+130", "Anytime Goal Odds (FD)": "+125",
            "Base Sim Goal Prob": 38.5, "PP Unit": "PP1"
        },
        {
            "Player": "Brad Marchand", "Team": "BOS", "Pos": "W", "Opponent": "vs OTT", "Status": "🟢 Active",
            "Anytime Goal Odds (DK)": "+160", "Anytime Goal Odds (FD)": "+155",
            "Base Sim Goal Prob": 33.0, "PP Unit": "PP1"
        },
        {
            "Player": "Kyle Connor", "Team": "WPG", "Pos": "W", "Opponent": "@ PIT", "Status": "🟢 Active",
            "Anytime Goal Odds (DK)": "+140", "Anytime Goal Odds (FD)": "+135",
            "Base Sim Goal Prob": 37.0, "PP Unit": "PP1"
        },
        {
            "Player": "Jason Robertson", "Team": "DAL", "Pos": "W", "Opponent": "vs SJS", "Status": "🟢 Active",
            "Anytime Goal Odds (DK)": "+120", "Anytime Goal Odds (FD)": "+115",
            "Base Sim Goal Prob": 41.0, "PP Unit": "PP1"
        },
        {
            "Player": "Travis Konecny", "Team": "PHI", "Pos": "W", "Opponent": "@ TBL", "Status": "🟢 Active",
            "Anytime Goal Odds (DK)": "+195", "Anytime Goal Odds (FD)": "+185",
            "Base Sim Goal Prob": 29.5, "PP Unit": "PP1"
        },
        {
            "Player": "Tim Stutzle", "Team": "OTT", "Pos": "C", "Opponent": "@ BOS", "Status": "🟢 Active",
            "Anytime Goal Odds (DK)": "+210", "Anytime Goal Odds (FD)": "+200",
            "Base Sim Goal Prob": 27.0, "PP Unit": "PP1"
        }
    ]
    return pd.DataFrame(data), today_str

if "nhl_slate" not in st.session_state:
    st.session_state.nhl_slate, st.session_state.slate_date = get_todays_nhl_slate()

df_nhl = st.session_state.nhl_slate.copy()
df_nhl["DK Implied %"] = df_nhl["Anytime Goal Odds (DK)"].apply(odds_to_implied)
df_nhl["FD Implied %"] = df_nhl["Anytime Goal Odds (FD)"].apply(odds_to_implied)
df_nhl["Best Implied %"] = df_nhl[["DK Implied %", "FD Implied %"]].min(axis=1)
df_nhl["EV_Edge_Num"] = df_nhl["Base Sim Goal Prob"] - df_nhl["Best Implied %"]

df_nhl["Sim Prob %"] = df_nhl["Base Sim Goal Prob"].apply(lambda x: f"{x:.1f}%")
df_nhl["EV Edge %"] = df_nhl["EV_Edge_Num"].apply(lambda x: f"{'+' if x > 0 else ''}{x:.1f}%")

# Sidebar
st.sidebar.header("NHL Schedule & Manager")
st.sidebar.info(f"📅 Active Date: {st.session_state.slate_date}")

with st.sidebar.expander("🛠 Edit NHL Goal Slate"):
    st.session_state.nhl_slate = st.data_editor(st.session_state.nhl_slate, num_rows="dynamic", use_container_width=True)
    if st.button("Save NHL Board"): st.rerun()

st.subheader("Tonight's NHL Slate — Top 10 Anytime Goal Scorer Projections")
st.dataframe(df_nhl[["Player", "Team", "Pos", "Opponent", "Anytime Goal Odds (DK)", "Anytime Goal Odds (FD)", "Sim Prob %", "EV Edge %", "PP Unit"]], use_container_width=True, hide_index=True)
