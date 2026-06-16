import streamlit as st
from datetime import datetime, timedelta
import requests

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Beacon | Flight Support Command Center",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. COCKPIT DARK THEME STYLING (Fixed for Python 3.14 string parsing)
css_style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    .clock-box {
        background-color: #1E293B;
        border-radius: 8px;
        padding: 12px;
        text-align: center;
        border: 1px solid #334155;
        font-family: 'JetBrains Mono', monospace;
    }
    .clock-gmt { background-color: #0284C7; border: 1px solid #38BDF8; }
    .clock-title { font-size: 0.8rem; color: #94A3B8; font-weight: bold; text-transform: uppercase; }
    .clock-time { font-size: 1.4rem; font-weight: 700; color: #FFFFFF; margin-top: 4px; }
    .app-card {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #38BDF8;
        margin-bottom: 12px;
    }
    .section-header {
        font-size: 1.4rem;
        font-weight: 700;
        color: #F8FAFC;
        border-bottom: 2px solid #334155;
        padding-bottom: 8px;
        margin-bottom: 15px;
    }
    .intel-box {
        background-color: #0F172A;
        border: 2px solid #10B981;
        padding: 20px;
        border-radius: 8px;
        margin-top: 15px;
    }
</style>
"""
st.markdown(css_style, unsafe_allowed_html=True)

# --- SIDEBAR: API KEY CONFIGURATION ---
with st.sidebar:
    st.header("🔑 API Configuration")
    openai_key = st.text_input("OpenAI API Key", type="password", help="Enter your OpenAI API key to enable Smart ICAO Search")
    st.caption("This key is handled locally and is not stored externally.")

# 3. HEADER: TIME ZONES ONLY
now_utc = datetime.utcnow()
edt = now_utc - timedelta(hours=4)
cdt = now_utc - timedelta(hours=5)
mdt = now_utc - timedelta(hours=6)
pdt = now_utc - timedelta(hours=7)

c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    st.markdown(f'<div class="clock-box clock-gmt"><div class="clock-title" style="color:#E0F2FE;">GMT / UTC</div><div class="clock-time">{now_utc.strftime("%H:%M")} Z</div></div>', unsafe_allowed_html=True)
with c2:
    st.markdown(f'<div class="clock-box"><div class="clock-title">Eastern (EDT)</div><div class="clock-time">{edt.strftime("%H:%M")}</div></div>', unsafe_allowed_html=True)
with c3:
    st.markdown(f'<div class="clock-box"><div class="clock-title">Central (CDT)</div><div class="clock-time">{cdt.strftime("%H:%M")}</div></div>', unsafe_allowed_html=True)
with c4:
    st.markdown(f'<div class="clock-box"><div class="clock-title">Mountain (MDT)</div><div class="clock-time">{mdt.strftime("%H:%M")}</div></div>', unsafe_allowed_html=True)
with c5:
    st.markdown(f'<div class="clock-box"><div class="clock-title">Pacific (PDT)</div><div class="clock-time">{pdt.strftime("%H:%M")}</div></div>', unsafe_allowed_html=True)

st.write("##")

# --- QUICK ICAO SEARCH SECTION ---
st.markdown("### 🔍 Smart ICAO Search")
icao_input = st.text_input("Enter Airport Code", placeholder="e.g., KJFK, MMUN, LEMD").upper().strip()

if icao_input:
    if not openai_key:
        st.warning("⚠️ Please provide your OpenAI API Key in the left sidebar to use the Smart Search feature.")
    else:
        with st.spinner(f"Querying intelligence for {icao_input}..."):
            try:
                headers = {
                    "Authorization": f"Bearer {openai_key}",
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": "gpt-4o",
                    "messages": [
                        {"role": "system", "content": "You are an expert dispatch assistant for high-tier Flight Support operations."},
                        {"role": "user", "content": f"Provide comprehensive aviation operational data for {icao_input}. Include: 1) General Airport Info & Operating Hours, 2) Estimated Current Weather & TAF trends, 3) Available FBOs on field, and 4) Notable Operational constraints. Format cleanly using bullet points and bold titles."}
                    ],
                    "temperature": 0.3
                }
                response = requests.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers)
                
                if response.status_code == 200:
                    ai_data = response.json()['choices'][0]['message']['content']
                    st.markdown(f'<div class="intel-box">🎒 <b>Beacon Intel Report: {icao_input}</b></div>', unsafe_allowed_html=True)
                    st.info("Airport details generated successfully:")
                    st.markdown(ai_data)
                    st.divider()
                else:
                    st.error(f"OpenAI API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An unexpected tracking error occurred: {str(e)}")

st.write("##")

# 4. MAIN DASHBOARD LAYOUT (3-COLUMN GRID)
col_left, col_center, col_right = st.columns([1, 1, 1], gap="large")

# --- LEFT COLUMN: INTERNAL PROPRIETARY APPS ---
with col_left:
    st.markdown('<div class="section-header">🛠️ Proprietary Apps</div>', unsafe_allowed_html=True)
    
    st.markdown('<div class="app-card"><h4>🛡️ Operational Mission Assessment</h4><p style="font-size:0.85rem; color:#94A3B8;">Risk assessment and operational feasibility tool.</p></div>', unsafe_allowed_html=True)
    st.link_button("Launch Mission Assessment", "https://thrust-aviation-flightsupport-weather-assessment.streamlit.app/", type="primary", use_container_width=True)
    st.write("#")
    
    st.markdown('<div class="app-card" style="border-left-color: #F59E0B;"><h4>✉️ Client Communications Newsletter</h4><p style="font-size:0.85rem; color:#94A3B8;">Communications script matrix and updates dispatch tool.</p></div>', unsafe_allowed_html=True)
    st.link_button("Open Communications Portal", "https://thrust-aviation-flightsupport-scripts.streamlit.app/", use_container_width=True)
    st.write("#")
    
    st.markdown('<div class="app-card" style="border-left-color: #10B981;"><h4>📄 Contracts Assessment</h4><p style="font-size:0.85rem; color:#94A3B8;">Contract compliance and regulatory validation.</p></div>', unsafe_allowed_html=True)
    st.link_button("Open Contracts Engine", "https://thrust-contract-compliance.streamlit.app/", use_container_width=True)

# --- CENTER COLUMN: AIRSPACE CONTROL SYSTEM ---
with col_center:
    st.markdown('<div class="section-header">✈️ Airspace Control & Status</div>', unsafe_allowed_html=True)
    
    st.link_button("🌐 Graphic TFRs (FAA List)", "https://tfr.faa.gov/tfr3/?page=list", use_container_width=True)
    st.link_button("📡 National Airspace System Status (NAS)", "https://nasstatus.faa.gov/", use_container_width=True)
    st.link_button("🗺️ Flight Radar 24 Sector Map", "https://www.flightradar24.com/39.81,-75.86/8", use_container_width=True)
    st.link_button("📊 FlightAware Tracking Portal", "https://www.flightaware.com/es-ES", use_container_width=True)
    st.link_button("🗃️ FAA NOTAM Data Center", "https://notams.aim.faa.gov/notamSearch/", use_container_width=True)
    st.link_button("✈️ AOPA Destinations & Airports Center", "https://aopa.org/destinations/?t=airports&_gl=1*6m0wou*_gcl_au*MTI4MDE3NzQzNC4xNzc3OTg3Nzk3*_ga*MjgxMDY5NjQ4LjE3Nzc5ODc3ODA.*_ga_SM42H3BVW5*czE3Nzc5ODc3ODAkbzEkZzEkdDE3Nzc5ODc5NzEkajYwJGwwJGgxMTMyNjg1NTQz", use_container_width=True)

# --- RIGHT COLUMN: METEOROLOGY & FORECASTS ---
with col_right:
    st.markdown('<div class="section-header">⛈️ Real-Time Weather Center</div>', unsafe_allowed_html=True)
    
    st.markdown("**GOES-East CONUS Satellite (Live)**")
    st.components.v1.iframe(
        src="https://www.star.nesdis.noaa.gov/GOES/conus_band.php?sat=G16&band=11&length=24",
        height=380,
        scrolling=True
    )
    
    st.write("##")
    st.markdown("**Meteorological Dashboards**")
    st.link_button("📑 TAF / METAR Regional Search", "https://metar-taf.com/?c=158495.-809033.4#google_vignette", use_container_width=True)
    st.link_button("🌀 National Hurricane Center (NHC)", "https://www.nhc.noaa.gov/", use_container_width=True)
    st.link_button("🗺️ NWS National Forecast Maps", "https://www.weather.gov/forecastmaps/", use_container_width=True)
