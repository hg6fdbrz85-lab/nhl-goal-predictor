import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="NHL Edge & Prop Hunter", layout="wide")
st.title("🏒 NHL Prop & Edge Hunter")
st.caption("Standalone Board: Bulletproof Date-Keyed Schedule, PP Units & SOG/Points")

def odds_to_implied(odds_val):
    try:
        clean = str(odds_val).replace('+', '').strip()
        if clean == 'N/A' or clean == '' or clean.lower() == 'nan':
            return 0.0
        odds = float(clean)
        return round((100.0 / (odds + 100.0)) * 100.0, 1) if odds > 0 else round((abs(odds) / (abs(odds) + 100.0)) * 100.0, 1)
    except:
        return 0.0

def get_nhl_slate_by_date():
    today_str = datetime.now().strftime("%Y-%m-%d")
    
    schedule_database = {
        "2026-10-07": [
            {
                "Player": "Jack Hughes", "Team": "NJD", "Pos": "C", "Opponent": "vs UTA", "PP Unit": "PP1 (Top Unit)",
                "Game Total": 6.5, "Puck Line / Spread": "-1.5 (+150)", "Implied Team Total": 3.5, "Shots Factor": 1.4,
                "Base Point Prob": 68.0, "SOG Projection": 4.3, "Alt SOG Line": "3+ SOG (+110)",
                "DK SOG (2+)": "-220", "DK Points": "-140", "Anytime Goal": "-135"
            },
            {
                "Player": "Kirill Kaprizov", "Team": "MIN", "Pos": "LW", "Opponent": "@ BUF", "PP Unit": "PP1 (Top Unit)",
                "Game Total": 6.0, "Puck Line / Spread": "+1.5 (-230)", "Implied Team Total": 3.0, "Shots Factor": 1.2,
                "Base Point Prob": 65.0, "SOG Projection": 4.1, "Alt SOG Line": "3+ SOG (+125)",
                "DK SOG (2+)": "-200", "DK Points": "-130", "Anytime Goal": "+115"
            },
            {
                "Player": "Tage Thompson", "Team": "BUF", "Pos": "C", "Opponent": "vs MIN", "PP Unit": "PP1 (Top Unit)",
                "Game Total": 6.0, "Puck Line / Spread": "-0.5 (+105)", "Implied Team Total": 3.1, "Shots Factor": 1.1,
                "Base Point Prob": 60.0, "SOG Projection": 3.8, "Alt SOG Line": "3+ SOG (+135)",
                "DK SOG (2+)": "-185", "DK Points": "-120", "Anytime Goal": "+125"
            },
            {
                "Player": "Alex DeBrincat", "Team": "DET", "Pos": "RW", "Opponent": "vs OTT", "PP Unit": "PP1 (Top Unit)",
                "Game Total": 6.5, "Puck Line / Spread": "-1.5 (+180)", "Implied Team Total": 3.4, "Shots Factor": 1.0,
                "Base Point Prob": 58.0, "SOG Projection": 3.6, "Alt SOG Line": "3+ SOG (+140)",
                "DK SOG (2+)": "-175", "DK Points": "-125", "Anytime Goal": "+135"
            },
            {
                "Player": "Tim Stützle", "Team": "OTT", "Pos": "C", "Opponent": "@ DET", "PP Unit": "PP1 (Top Unit)",
                "Game Total": 6.5, "Puck Line / Spread": "+1.5 (-210)", "Implied Team Total": 3.0, "Shots Factor": 0.9,
                "Base Point Prob": 55.0, "SOG Projection": 3.4, "Alt SOG Line": "3+ SOG (+160)",
                "DK SOG (2+)": "-160", "DK Points": "+110", "Anytime Goal": "+150"
            },
            {
                "Player": "Dylan Larkin", "Team": "DET", "Pos": "C", "Opponent": "vs OTT", "PP Unit": "PP1 (Top Unit)",
                "Game Total": 6.5, "Puck Line / Spread": "-1.5 (+180)", "Implied Team Total": 3.4, "Shots Factor": 0.8,
                "Base Point Prob": 54.0, "SOG Projection": 3.1, "Alt SOG Line": "3+ SOG (+175)",
                "DK SOG (2+)": "-155", "DK Points": "+115", "Anytime Goal": "+160"
            },
            {
                "Player": "Clayton Keller", "Team": "UTA", "Pos": "RW", "Opponent": "@ NJD", "PP Unit": "PP1 (Top Unit)",
                "Game Total": 6.5, "Puck Line / Spread": "+1.5 (-180)", "Implied Team Total": 2.8, "Shots Factor": 0.9,
                "Base Point Prob": 50.0, "SOG Projection": 3.0, "Alt SOG Line": "3+ SOG (+185)",
                "DK SOG (2+)": "-150", "DK Points": "+125", "Anytime Goal": "+190"
            },
            {
                "Player": "Matt Boldy", "Team": "MIN", "Pos": "RW", "Opponent": "@ BUF", "PP Unit": "PP2 (Secondary)",
                "Game Total": 6.0, "Puck Line / Spread": "+1.5 (-230)", "Implied Team Total": 3.0, "Shots Factor": 0.7,
                "Base Point Prob": 48.0, "SOG Projection": 2.8, "Alt SOG Line": "3+ SOG (+200)",
                "DK SOG (2+)": "-140", "DK Points": "+140", "Anytime Goal": "+180"
            },
            {
                "Player": "Nico Hischier", "Team": "NJD", "Pos": "C", "Opponent": "vs UTA", "PP Unit": "PP2 (Secondary)",
                "Game Total": 6.5, "Puck Line / Spread": "-1.5 (+150)", "Implied Team Total": 3.5, "Shots Factor": 0.6,
                "Base Point Prob": 47.0, "SOG Projection": 2.6, "Alt SOG Line": "3+ SOG (+210)",
                "DK SOG (2+)": "-130", "DK Points": "+150", "Anytime Goal": "+175"
            },
            {
                "Player": "Rasmus Dahlin", "Team": "BUF", "Pos": "D", "Opponent": "vs MIN", "PP Unit": "PP1 (Quarterback)",
                "Game Total": 6.0, "Puck Line / Spread": "-0.5 (+105)", "Implied Team Total": 3.1, "Shots Factor": 0.8,
                "Base Point Prob": 42.0, "SOG Projection": 2.9, "Alt SOG Line": "3+ SOG (+190)",
                "DK SOG (2+)": "-145", "DK Points": "+160", "Anytime Goal": "+240"
            }
        ]
    }
    
    if today_str in schedule_database:
        active_data = schedule_database[today_str]
        active_date_used = today_str
    else:
        latest_key = sorted(schedule_database.keys())[-1]
        active_data = schedule_database[latest_key]
        active_date_used = f"{latest_key} (Fallback Active)"
        
    return pd.DataFrame(active_data), active_date_used

if "nhl_slate" not in st.session_state:
    st.session_state.nhl_slate, st.session_state.nhl_date = get_nhl_slate_by_date()

df = st.session_state.nhl_slate.copy()
df["Total Point Prob"] = df["Base Point Prob"] + (df["Shots Factor"] * 2.0)
df["Value Signal"] = df["Total Point Prob"].apply(lambda x: "🟢 HIGH" if x > 60 else ("🟡 MODERATE" if x > 50 else "🔴 LOW"))
df["Point Prob %"] = df["Total Point Prob"].apply(lambda x: f"{x:.1f}%")

st.sidebar.header("NHL Schedule & Manager")
st.sidebar.info(f"📅 Active Date: {st.session_state.nhl_date}")

with st.sidebar.expander("🛠 Edit Slate, PP Units & Lines"):
    st.markdown("Update PP units, lines, or odds directly below:")
    st.session_state.nhl_slate = st.data_editor(st.session_state.nhl_slate, num_rows="dynamic", use_container_width=True)
    if st.button("Save Updates"): st.rerun()

st.subheader("Active NHL Slate — PP Units, SOG & Points Board")
st.dataframe(
    df[[
        "Player", "Team", "Opponent", "PP Unit", "Game Total", "Puck Line / Spread", 
        "SOG Projection", "Alt SOG Line", "DK SOG (2+)", "Point Prob %", 
        "DK Points", "Anytime Goal", "Value Signal"
    ]], 
    use_container_width=True, 
    hide_index=True
)
