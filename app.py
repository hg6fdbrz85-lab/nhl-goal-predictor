import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="NHL Edge & Prop Hunter", layout="wide")
st.title("🏒 NHL Prop & Edge Hunter")
st.caption("Standalone Board: Bulletproof Date-Keyed Schedule & SOG/Points Analytics")

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
                "Player": "Jack Hughes", "Team": "NJD", "Pos": "C", "Opponent": "vs UTA", "Status": "🟢 Active",
                "Game Total": 6.5, "Implied Team Total": 3.5, "Shots Factor": 1.4,
                "Base Point Prob": 68.0, "SOG Projection": 4.3, "Opp Def Rank": "#21 (Weak)",
                "DraftKings SOG Alt (2+)": "-220", "DraftKings Points": "-140", "Anytime Goal": "-135"
            },
            {
                "Player": "Kirill Kaprizov", "Team": "MIN", "Pos": "LW", "Opponent": "@ BUF", "Status": "🟢 Active",
                "Game Total": 6.0, "Implied Team Total": 3.0, "Shots Factor": 1.2,
                "Base Point Prob": 65.0, "SOG Projection": 4.1, "Opp Def Rank": "#14 (Mid)",
                "DraftKings SOG Alt (2+)": "-200", "DraftKings Points": "-130", "Anytime Goal": "+115"
            },
            {
                "Player": "Tage Thompson", "Team": "BUF", "Pos": "C", "Opponent": "vs MIN", "Status": "🟢 Active",
                "Game Total": 6.0, "Implied Team Total": 3.1, "Shots Factor": 1.1,
                "Base Point Prob": 60.0, "SOG Projection": 3.8, "Opp Def Rank": "#10 (Solid)",
                "DraftKings SOG Alt (2+)": "-185", "DraftKings Points": "-120", "Anytime Goal": "+125"
            },
            {
                "Player": "Alex DeBrincat", "Team": "DET", "Pos": "RW", "Opponent": "vs OTT", "Status": "🟢 Active",
                "Game Total": 6.5, "Implied Team Total": 3.4, "Shots Factor": 1.0,
                "Base Point Prob": 58.0, "SOG Projection": 3.6, "Opp Def Rank": "#19 (Mid)",
                "DraftKings SOG Alt (2+)": "-175", "DraftKings Points": "-125", "Anytime Goal": "+135"
            },
            {
                "Player": "Tim Stützle", "Team": "OTT", "Pos": "C", "Opponent": "@ DET", "Status": "🟢 Active",
                "Game Total": 6.5, "Implied Team Total": 3.0, "Shots Factor": 0.9,
                "Base Point Prob": 55.0, "SOG Projection": 3.4, "Opp Def Rank": "#16 (Mid)",
                "DraftKings SOG Alt (2+)": "-160", "DraftKings Points": "+110", "Anytime Goal": "+150"
            },
            {
                "Player": "Dylan Larkin", "Team": "DET", "Pos": "C", "Opponent": "vs OTT", "Status": "🟢 Active",
                "Game Total": 6.5, "Implied Team Total": 3.4, "Shots Factor": 0.8,
                "Base Point Prob": 54.0, "SOG Projection": 3.1, "Opp Def Rank": "#19 (Mid)",
                "DraftKings SOG Alt (2+)": "-155", "DraftKings Points": "+115", "Anytime Goal": "+160"
            },
            {
                "Player": "Clayton Keller", "Team": "UTA", "Pos": "RW", "Opponent": "@ NJD", "Status": "🟢 Active",
                "Game Total": 6.5, "Implied Team Total": 2.8, "Shots Factor": 0.9,
                "Base Point Prob": 50.0, "SOG Projection": 3.0, "Opp Def Rank": "#9 (Strong)",
                "DraftKings SOG Alt (2+)": "-150", "DraftKings Points": "+125", "Anytime Goal": "+190"
            },
            {
                "Player": "Matt Boldy", "Team": "MIN", "Pos": "RW", "Opponent": "@ BUF", "Status": "🟢 Active",
                "Game Total": 6.0, "Implied Team Total": 3.0, "Shots Factor": 0.7,
                "Base Point Prob": 48.0, "SOG Projection": 2.8, "Opp Def Rank": "#14 (Mid)",
                "DraftKings SOG Alt (2+)": "-140", "DraftKings Points": "+140", "Anytime Goal": "+180"
            },
            {
                "Player": "Nico Hischier", "Team": "NJD", "Pos": "C", "Opponent": "vs UTA", "Status": "🟢 Active",
                "Game Total": 6.5, "Implied Team Total": 3.5, "Shots Factor": 0.6,
                "Base Point Prob": 47.0, "SOG Projection": 2.6, "Opp Def Rank": "#21 (Weak)",
                "DraftKings SOG Alt (2+)": "-130", "DraftKings Points": "+150", "Anytime Goal": "+175"
            },
            {
                "Player": "Rasmus Dahlin", "Team": "BUF", "Pos": "D", "Opponent": "vs MIN", "Status": "🟢 Active",
                "Game Total": 6.0, "Implied Team Total": 3.1, "Shots Factor": 0.8,
                "Base Point Prob": 42.0, "SOG Projection": 2.9, "Opp Def Rank": "#10 (Solid)",
                "DraftKings SOG Alt (2+)": "-145", "DraftKings Points": "+160", "Anytime Goal": "+240"
            }
        ]
    }
    
    # BULLETPROOF FALLBACK: If today's key isn't found, grab the most recent available date instead of crashing or showing McDavid
    if today_str in schedule_database:
        active_data = schedule_database[today_str]
        active_date_used = today_str
    else:
        # Fallback to the latest dictionary key available so the app never blanks out
        latest_key = sorted(schedule_database.keys())[-1]
        active_data = schedule_database[latest_key]
        active_date_used = f"{latest_key} (Fallback Active)"
        
    return pd.DataFrame(active_data), active_date_used

if "nhl_slate" not in st.session_state:
    st.session_state.nhl_slate, st.session_state.nhl_date = get_nhl_slate_by_date()

df = st.session_state.nhl_slate.copy()
df["Total Point Prob"] = df["Base Point Prob"] + (df["Shots Factor"] * 2.0)
df["DK SOG Implied %"] = df["DraftKings SOG Alt (2+)"].apply(odds_to_implied)
df["Value Signal"] = df["Total Point Prob"].apply(lambda x: "🟢 HIGH" if x > 60 else ("🟡 MODERATE" if x > 50 else "🔴 LOW"))

df["Point Prob %"] = df["Total Point Prob"].apply(lambda x: f"{x:.1f}%")

st.sidebar.header("NHL Schedule & Manager")
st.sidebar.info(f"📅 Active Date: {st.session_state.nhl_date}")

with st.sidebar.expander("🛠 Edit NHL Slate"):
    st.session_state.nhl_slate = st.data_editor(st.session_state.nhl_slate, num_rows="dynamic", use_container_width=True)
    if st.button("Save NHL Board"): st.rerun()

st.subheader("Active NHL Slate — SOG & Points Focus Board")
st.dataframe(
    df[[
        "Player", "Team", "Pos", "Opponent", "Game Total", "Implied Team Total",
        "SOG Projection", "DraftKings SOG Alt (2+)", "Point Prob %", "DraftKings Points", 
        "Anytime Goal", "Opp Def Rank", "Value Signal"
    ]], 
    use_container_width=True, 
    hide_index=True
)
