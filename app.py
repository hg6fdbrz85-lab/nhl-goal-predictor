import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="NHL Edge Hunter", layout="wide")
st.title("🏒 NHL Prop & Edge Hunter")
st.caption("Standalone Board: Automated Date-Keyed Schedule & Player Slate")

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
    
    # Date-keyed schedule dictionary so the slate dynamically shifts day-to-day
    schedule_database = {
        "2026-10-06": [
            {
                "Player": "Auston Matthews", "Team": "TOR", "Pos": "C", "Opponent": "vs NSH", "Status": "🟢 Active",
                "Game Total": 6.5, "Spread": "-1.5", "Implied Team Total": 3.6, "Is Fav": True, "Shots Factor": +1.2,
                "Base Sim Prob": 54.0, "SOG Projection": 4.2, "Opp Def Rank": "#18 (Mid)",
                "DraftKings AnyTime": "-145", "FanDuel AnyTime": "-140", "1st Goal (DK)": "+650", "1st Goal (FD)": "+600"
            },
            {
                "Player": "William Nylander", "Team": "TOR", "Pos": "RW", "Opponent": "vs NSH", "Status": "🟢 Active",
                "Game Total": 6.5, "Spread": "-1.5", "Implied Team Total": 3.6, "Is Fav": True, "Shots Factor": +0.9,
                "Base Sim Prob": 42.0, "SOG Projection": 3.5, "Opp Def Rank": "#18 (Mid)",
                "DraftKings AnyTime": "+110", "FanDuel AnyTime": "+105", "1st Goal (DK)": "+900", "1st Goal (FD)": "+850"
            },
            {
                "Player": "Sebastian Aho", "Team": "CAR", "Pos": "C", "Opponent": "@ MTL", "Status": "🟢 Active",
                "Game Total": 6.0, "Spread": "-125", "Implied Team Total": 3.2, "Is Fav": True, "Shots Factor": +1.0,
                "Base Sim Prob": 39.0, "SOG Projection": 3.1, "Opp Def Rank": "#15 (Mid)",
                "DraftKings AnyTime": "+130", "FanDuel AnyTime": "+125", "1st Goal (DK)": "+1000", "1st Goal (FD)": "+950"
            },
            {
                "Player": "Cole Caufield", "Team": "MTL", "Pos": "RW", "Opponent": "vs CAR", "Status": "🟢 Active",
                "Game Total": 6.0, "Spread": "+105", "Implied Team Total": 2.8, "Is Fav": False, "Shots Factor": +1.3,
                "Base Sim Prob": 41.0, "SOG Projection": 3.8, "Opp Def Rank": "#8 (Strong)",
                "DraftKings AnyTime": "+140", "FanDuel AnyTime": "+135", "1st Goal (DK)": "+1100", "1st Goal (FD)": "+1050"
            }
        ]
    }
    
    # Fallback default if a specific date isn't hard-mapped yet
    default_slate = [
        {
            "Player": "Connor McDavid", "Team": "EDM", "Pos": "C", "Opponent": "vs --", "Status": "🟢 Active",
            "Game Total": 6.5, "Spread": "-1.5", "Implied Team Total": 3.8, "Is Fav": True, "Shots Factor": +1.5,
            "Base Sim Prob": 62.0, "SOG Projection": 4.5, "Opp Def Rank": "#20 (Weak)",
            "DraftKings AnyTime": "-130", "FanDuel AnyTime": "-125", "1st Goal (DK)": "+550", "1st Goal (FD)": "+525"
        }
    ]
    
    active_data = schedule_database.get(today_str, default_slate)
    return pd.DataFrame(active_data), today_str

if "nhl_slate" not in st.session_state:
    st.session_state
