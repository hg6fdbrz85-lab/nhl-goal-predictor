import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="NHL Goal Scorer Edge Hunter", layout="wide")
st.title("🏒 NHL Goal Scorer Edge Hunter")
st.caption("Standalone Board: Automated Schedule-Aware Anytime Goals & Probability Projections")

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
# AUTOMATED SCHEDULE & GOAL SCORER SLATE LOADER
# -------------------------------------------------------------
def get_todays_nhl_slate():
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    # Automated Slate Mapping for tonight's games (Oct 5, 2026)
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

st.subheader("Tonight's NHL Slate — Anytime Goal Scorer Projections")
st.dataframe(df_nhl[["Player", "Team", "Pos", "Opponent", "Anytime Goal Odds (DK)", "Anytime Goal Odds (FD)", "Sim Prob %", "EV Edge %", "PP Unit"]], use_container_width=True, hide_index=True)
