import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="NHL Edge Hunter", layout="wide")
st.title("🏒 NHL Prop & Edge Hunter")
st.caption("Standalone Board: Automated Date-Keyed Schedule & Top 10 Player Slate")

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
        "2026-10-06": [
            {
                "Player": "Auston Matthews", "Team": "TOR", "Pos": "C", "Opponent": "vs NSH", "Status": "🟢 Active",
                "Game Total": 6.5, "Spread": "-1.5", "Implied Team Total": 3.6, "Is Fav": True, "Shots Factor": 1.2,
                "Base Sim Prob": 54.0, "SOG Projection": 4.2, "Opp Def Rank": "#18 (Mid)",
                "DraftKings AnyTime": "-145", "FanDuel AnyTime": "-140", "1st Goal (DK)": "+650", "1st Goal (FD)": "+600"
            },
            {
                "Player": "William Nylander", "Team": "TOR", "Pos": "RW", "Opponent": "vs NSH", "Status": "🟢 Active",
                "Game Total": 6.5, "Spread": "-1.5", "Implied Team Total": 3.6, "Is Fav": True, "Shots Factor": 0.9,
                "Base Sim Prob": 42.0, "SOG Projection": 3.5, "Opp Def Rank": "#18 (Mid)",
                "DraftKings AnyTime": "+110", "FanDuel AnyTime": "+105", "1st Goal (DK)": "+900", "1st Goal (FD)": "+850"
            },
            {
                "Player": "Mitch Marner", "Team": "TOR", "Pos": "RW", "Opponent": "vs NSH", "Status": "🟢 Active",
                "Game Total": 6.5, "Spread": "-1.5", "Implied Team Total": 3.6, "Is Fav": True, "Shots Factor": 0.6,
                "Base Sim Prob": 35.0, "SOG Projection": 2.7, "Opp Def Rank": "#18 (Mid)",
                "DraftKings AnyTime": "+160", "FanDuel AnyTime": "+155", "1st Goal (DK)": "+1200", "1st Goal (FD)": "+1100"
            },
            {
                "Player": "Filip Forsberg", "Team": "NSH", "Pos": "LW", "Opponent": "@ TOR", "Status": "🟢 Active",
                "Game Total": 6.5, "Spread": "+1.5", "Implied Team Total": 2.9, "Is Fav": False, "Shots Factor": 1.1,
                "Base Sim Prob": 40.0, "SOG Projection": 3.9, "Opp Def Rank": "#12 (Solid)",
                "DraftKings AnyTime": "+135", "FanDuel AnyTime": "+130", "1st Goal (DK)": "+1000", "1st Goal (FD)": "+950"
            },
            {
                "Player": "Steven Stamkos", "Team": "NSH", "Pos": "C", "Opponent": "@ TOR", "Status": "🟢 Active",
                "Game Total": 6.5, "Spread": "+1.5", "Implied Team Total": 2.9, "Is Fav": False, "Shots Factor": 1.0,
                "Base Sim Prob": 38.0, "SOG Projection": 3.4, "Opp Def Rank": "#12 (Solid)",
                "DraftKings AnyTime": "+150", "FanDuel AnyTime": "+145", "1st Goal (DK)": "+1100", "1st Goal (FD)": "+1050"
            },
            {
                "Player": "Sebastian Aho", "Team": "CAR", "Pos": "C", "Opponent": "@ MTL", "Status": "🟢 Active",
                "Game Total": 6.0, "Spread": "-125", "Implied Team Total": 3.2, "Is Fav": True, "Shots Factor": 1.0,
                "Base Sim Prob": 39.0, "SOG Projection": 3.1, "Opp Def Rank": "#15 (Mid)",
                "DraftKings AnyTime": "+130", "FanDuel AnyTime": "+125", "1st Goal (DK)": "+1000", "1st Goal (FD)": "+950"
            },
            {
                "Player": "Andrei Svechnikov", "Team": "CAR", "Pos": "RW", "Opponent": "@ MTL", "Status": "🟢 Active",
                "Game Total": 6.0, "Spread": "-125", "Implied Team Total": 3.2, "Is Fav": True, "Shots Factor": 1.2,
                "Base Sim Prob": 37.0, "SOG Projection": 3.6, "Opp Def Rank": "#15 (Mid)",
                "DraftKings AnyTime": "+145", "FanDuel AnyTime": "+140", "1st Goal (DK)": "+1100", "1st Goal (FD)": "+1000"
            },
            {
                "Player": "Cole Caufield", "Team": "MTL", "Pos": "RW", "Opponent": "vs CAR", "Status": "🟢 Active",
                "Game Total": 6.0, "Spread": "+105", "Implied Team Total": 2.8, "Is Fav": False, "Shots Factor": 1.3,
                "Base Sim Prob": 41.0, "SOG Projection": 3.8, "Opp Def Rank": "#8 (Strong)",
                "DraftKings AnyTime": "+140", "FanDuel AnyTime": "+135", "1st Goal (DK)": "+1100", "1st Goal (FD)": "+1050"
            },
            {
                "Player": "Nick Suzuki", "Team": "MTL", "Pos": "C", "Opponent": "vs CAR", "Status": "🟢 Active",
                "Game Total": 6.0, "Spread": "+105", "Implied Team Total": 2.8, "Is Fav": False, "Shots Factor": 0.7,
                "Base Sim Prob": 32.0, "SOG Projection": 2.5, "Opp Def Rank": "#8 (Strong)",
                "DraftKings AnyTime": "+195", "FanDuel AnyTime": "+190", "1st Goal (DK)": "+1500", "1st Goal (FD)": "+1400"
            },
            {
                "Player": "Ryan O'Reilly", "Team": "NSH", "Pos": "C", "Opponent": "@ TOR", "Status": "🟢 Active",
                "Game Total": 6.5, "Spread": "+1.5", "Implied Team Total": 2.9, "Is Fav": False, "Shots Factor": 0.5,
                "Base Sim Prob": 28.0, "SOG Projection": 2.2, "Opp Def Rank": "#12 (Solid)",
                "DraftKings AnyTime": "+230", "FanDuel AnyTime": "+220", "1st Goal (DK)": "+1800", "1st Goal (FD)": "+1600"
            }
        ]
    }
    
    default_slate = [
        {
            "Player": "Connor McDavid", "Team": "EDM", "Pos": "C", "Opponent": "vs --", "Status": "🟢 Active",
            "Game Total": 6.5, "Spread": "-1.5", "Implied Team Total": 3.8, "Is Fav": True, "Shots Factor": 1.5,
            "Base Sim Prob": 62.0, "SOG Projection": 4.5, "Opp Def Rank": "#20 (Weak)",
            "DraftKings AnyTime": "-130", "FanDuel AnyTime": "-125", "1st Goal (DK)": "+550", "1st Goal (FD)": "+525"
        }
    ]
    
    active_data = schedule_database.get(today_str, default_slate)
    return pd.DataFrame(active_data), today_str

if "nhl_slate" not in st.session_state:
    st.session_state.nhl_slate, st.session_state.nhl_date = get_nhl_slate_by_date()

df = st.session_state.nhl_slate.copy()
df["Sim Prob"] = df["Base Sim Prob"] + df["Shots Factor"]
df["DK Implied %"] = df["DraftKings AnyTime"].apply(odds_to_implied)
df["FD Implied %"] = df["FanDuel AnyTime"].apply(odds_to_implied)
df["Best Implied %"] = df[["DK Implied %", "FD Implied %"]].min(axis=1)
df["EV_Edge_Num"] = df["Sim Prob"] - df["Best Implied %"]
df["Value Signal"] = df["EV_Edge_Num"].apply(lambda x: "🟢 YES" if x > 2.5 else ("🟡 SLIGHT" if x > 0 else "🔴 NO"))

df["Sim Prob %"] = df["Sim Prob"].apply(lambda x: f"{x:.1f}%")
df["EV Edge %"] = df["EV_Edge_Num"].apply(lambda x: f"{'+' if x > 0 else ''}{x:.1f}%")

st.sidebar.header("NHL Schedule & Manager")
st.sidebar.info(f"📅 Active Date: {st.session_state.nhl_date}")

with st.sidebar.expander("🛠 Edit NHL Slate"):
    st.session_state.nhl_slate = st.data_editor(st.session_state.nhl_slate, num_rows="dynamic", use_container_width=True)
    if st.button("Save NHL Board"): st.rerun()

st.subheader("Active NHL Slate — Top 10 Goal Scoring & Analytics Board")
st.dataframe(
    df[[
        "Player", "Team", "Pos", "Opponent", "Game Total", "Spread", "Implied Team Total",
        "DraftKings AnyTime", "FanDuel AnyTime", "Sim Prob %", "EV Edge %", "Value Signal", 
        "SOG Projection", "Opp Def Rank", "1st Goal (DK)", "1st Goal (FD)"
    ]], 
    use_container_width=True, 
    hide_index=True
)
