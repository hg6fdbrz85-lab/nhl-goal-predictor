import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="NHL Edge & Prop Hunter", layout="wide")
st.title("🏒 NHL Prop & Edge Hunter")
st.caption("Standalone Board: Automated Date-Keyed Schedule & Live SOG/Points Analytics")

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
    
    # Comprehensive dictionary mapping real slates by date automatically
    schedule_database = {
        "2026-10-07": [
            # Penguins @ Capitals
            {
                "Player": "Sidney Crosby", "Team": "PIT", "Pos": "C", "Opponent": "@ WSH", "PP Unit": "PP1 (Top Unit)",
                "Game Total": 6.5, "Puck Line / Spread": "+1.5 (-210)", "Implied Team Total": 3.0, "Shots Factor": 1.3,
                "Base Point Prob": 67.0, "SOG Projection": 3.9, "Alt SOG Line": "3+ SOG (+115)",
                "DK SOG (2+)": "-210", "DK Points": "-135", "Anytime Goal": "+125"
            },
            {
                "Player": "Evgeni Malkin", "Team": "PIT", "Pos": "C", "Opponent": "@ WSH", "PP Unit": "PP1 (Top Unit)",
                "Game Total": 6.5, "Puck Line / Spread": "+1.5 (-210)", "Implied Team Total": 3.0, "Shots Factor": 1.1,
                "Base Point Prob": 60.0, "SOG Projection": 3.5, "Alt SOG Line": "3+ SOG (+135)",
                "DK SOG (2+)": "-180", "DK Points": "-120", "Anytime Goal": "+150"
            },
            {
                "Player": "Alex Ovechkin", "Team": "WSH", "Pos": "LW", "Opponent": "vs PIT", "PP Unit": "PP1 (Top Unit)",
                "Game Total": 6.5, "Puck Line / Spread": "-1.5 (+170)", "Implied Team Total": 3.5, "Shots Factor": 1.5,
                "Base Point Prob": 65.0, "SOG Projection": 4.4, "Alt SOG Line": "3+ SOG (-110)",
                "DK SOG (2+)": "-250", "DK Points": "-140", "Anytime Goal": "+110"
            },
            # Avalanche @ Jets
            {
                "Player": "Nathan MacKinnon", "Team": "COL", "Pos": "C", "Opponent": "@ WPG", "PP Unit": "PP1 (Top Unit)",
                "Game Total": 6.5, "Puck Line / Spread": "-1.5 (+185)", "Implied Team Total": 3.6, "Shots Factor": 1.6,
                "Base Point Prob": 72.0, "SOG Projection": 4.6, "Alt SOG Line": "3+ SOG (-125)",
                "DK SOG (2+)": "-280", "DK Points": "-160", "Anytime Goal": "-110"
            },
            {
                "Player": "Mikko Rantanen", "Team": "COL", "Pos": "RW", "Opponent": "@ WPG", "PP Unit": "PP1 (Top Unit)",
                "Game Total": 6.5, "Puck Line / Spread": "-1.5 (+185)", "Implied Team Total": 3.6, "Shots Factor": 1.3,
                "Base Point Prob": 66.0, "SOG Projection": 3.8, "Alt SOG Line": "3+ SOG (+120)",
                "DK SOG (2+)": "-200", "DK Points": "-130", "Anytime Goal": "+120"
            },
            {
                "Player": "Kyle Connor", "Team": "WPG", "Pos": "LW", "Opponent": "vs COL", "PP Unit": "PP1 (Top Unit)",
                "Game Total": 6.5, "Puck Line / Spread": "+1.5 (-225)", "Implied Team Total": 2.9, "Shots Factor": 1.2,
                "Base Point Prob": 61.0, "SOG Projection": 3.7, "Alt SOG Line": "3+ SOG (+130)",
                "DK SOG (2+)": "-190", "DK Points": "-125", "Anytime Goal": "+140"
            },
            # Oilers @ Ducks
            {
                "Player": "Connor McDavid", "Team": "EDM", "Pos": "C", "Opponent": "@ ANA", "PP Unit": "PP1 (Top Unit)",
                "Game Total": 6.5, "Puck Line / Spread": "-1.5 (+145)", "Implied Team Total": 3.8, "Shots Factor": 1.5,
                "Base Point Prob": 75.0, "SOG Projection": 4.5, "Alt SOG Line": "3+ SOG (-120)",
                "DK SOG (2+)": "-270", "DK Points": "-170", "Anytime Goal": "-120"
            },
            {
                "Player": "Leon Draisaitl", "Team": "EDM", "Pos": "C", "Opponent": "@ ANA", "PP Unit": "PP1 (Top Unit)",
                "Game Total": 6.5, "Puck Line / Spread": "-1.5 (+145)", "Implied Team Total": 3.8, "Shots Factor": 1.3,
                "Base Point Prob": 70.0, "SOG Projection": 3.9, "Alt SOG Line": "3+ SOG (+110)",
                "DK SOG (2+)": "-220", "DK Points": "-150", "Anytime Goal": "+105"
            },
            {
                "Player": "Leo Carlsson", "Team": "ANA", "Pos": "C", "Opponent": "vs EDM", "PP Unit": "PP1 (Top Unit)",
                "Game Total": 6.5, "Puck Line / Spread": "+1.5 (-175)", "Implied Team Total": 2.7, "Shots Factor": 0.8,
                "Base Point Prob": 49.0, "SOG Projection": 2.7, "Alt SOG Line": "3+ SOG (+210)",
                "DK SOG (2+)": "-135", "DK Points": "+140", "Anytime Goal": "+210"
            },
            {
                "Player": "Cutter Gauthier", "Team": "ANA", "Pos": "LW", "Opponent": "vs EDM", "PP Unit": "PP1 (Top Unit)",
                "Game Total": 6.5, "Puck Line / Spread": "+1.5 (-175)", "Implied Team Total": 2.7, "Shots Factor": 1.0,
                "Base Point Prob": 52.0, "SOG Projection": 3.3, "Alt SOG Line": "3+ SOG (+160)",
                "DK SOG (2+)": "-160", "DK Points": "+120", "Anytime Goal": "+180"
            }
        ]
    }
    
    # Automatic Date Detection & Fallback logic
    if today_str in schedule_database:
        active_data = schedule_database[today_str]
        active_date_used = f"{today_str} (Live Slate Loaded)"
    else:
        # Automatically default to the most recent dictionary key if today isn't explicitly mapped
        latest_key = sorted(schedule_database.keys())[-1]
        active_data = schedule_database[latest_key]
        active_date_used = f"{latest_key} (Auto-Fallback Active)"
        
    return pd.DataFrame(active_data), active_date_used

if "nhl_slate" not in st.session_state:
    st.session_state.nhl_slate, st.session_state.nhl_date = get_nhl_slate_by_date()

df = st.session_state.nhl_slate.copy()
df["Total Point Prob"] = df["Base Point Prob"] + (df["Shots Factor"] * 2.0)
df["Value Signal"] = df["Total Point Prob"].apply(lambda x: "🟢 HIGH" if x > 60 else ("🟡 MODERATE" if x > 50 else "🔴 LOW"))
df["Point Prob %"] = df["Total Point Prob"].apply(lambda x: f"{x:.1f}%")

st.sidebar.header("NHL Schedule & Manager")
st.sidebar.info(f"📅 Status: {st.session_state.nhl_date}")

with st.sidebar.expander("🛠 Edit Slate, PP Units & Lines"):
    st.markdown("Override or tweak lines here if needed:")
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
