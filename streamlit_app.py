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

# --- SIDEBAR: API KEY CONFIGURATION ---
with st.sidebar:
    st.header("🔑 API Configuration")
    openai_key = st.text_input("OpenAI API Key", type="password", help="Enter your OpenAI API key to enable Smart ICAO Search")
    st.caption("This key is handled locally and is not stored externally.")

# 2. HEADER: TIME ZONES ONLY (NATIVE IMPLEMENTATION)
now_utc = datetime.utcnow()
edt = now_utc - timedelta(hours=4)
cdt = now_utc - timedelta(hours=5)
mdt = now_utc - timedelta(hours=6)
pdt = now_utc - timedelta(hours=7)

st.title("🧭 BEACON")
st.caption("The centralized operations hub for Flight Support.")
st.write("---")

# Render Clocks Layout natively using standard metrics blocks
c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    st.metric(label="GMT / UTC", value=f"{now_utc.strftime('%H:%M')} Z")
with c2:
    st.metric(label="Eastern (EDT)", value=edt.strftime("%H:%M"))
with c3:
    st.metric(label="Central (CDT)", value=cdt.strftime("%H:%M"))
with c4:
    st.metric(label="Mountain (MDT)", value=mdt.strftime("%H:%M"))
with c5:
    st.metric(label="Pacific (PDT)", value=pdt.strftime("%H:%M"))

st.write("---")

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
                    
                    # Native high-visibility container
                    with st.container(border=True):
                        st.subheader(f"🎒 Beacon Intel Report: {icao_input}")
                        st.markdown(ai_data)
                else:
                    st.error(f"OpenAI API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An unexpected tracking error occurred: {str(e)}")

st.write("##")

# 3. MAIN DASHBOARD LAYOUT (3-COLUMN GRID USING NATIVE BORDERS)
col_left, col_center, col_right = st.columns([1, 1, 1], gap="large")

# --- LEFT COLUMN: INTERNAL PROPRIETARY APPS ---
with col_left:
    st.subheader("🛠️ Proprietary Apps")
    
    with st.container(border=True):
        st.markdown("#### 🛡️ Operational Mission Assessment")
        st.caption("Risk assessment and operational feasibility tool.")
        st.link_button("Launch Mission Assessment", "https://thrust-aviation-flightsupport-weather-assessment.streamlit.app/", type="primary", use_container_width=True)
    
    st.write(" ")
    with st.container(border=True):
        st.markdown("#### ✉️ Client Communications Newsletter")
        st.caption("Communications script matrix and updates dispatch tool.")
        st.link_button("Open Communications Portal", "https://thrust-aviation-flightsupport-scripts.streamlit.app/", use_container_width=True)
    
    st.write(" ")
    with st.container(border=True):
        st.markdown("#### 📄 Contracts Assessment")
        st.caption("Contract compliance and regulatory validation.")
        st.link_button("Open Contracts Engine", "https://thrust-contract-compliance.streamlit.app/", use_container_width=True)

# --- CENTER COLUMN: AIRSPACE CONTROL SYSTEM ---
with col_center:
    st.subheader("✈️ Airspace Control & Status")
    
    st.link_button("🌐 Graphic TFRs (FAA List)", "https://tfr.faa.gov/tfr3/?page=list", use_container_width=True)
    st.link_button("📡 National Airspace System Status (NAS)", "https://nasstatus.faa.gov/", use_container_width=True)
    st.link_button("🗺️ Flight Radar 24 Sector Map", "https://www.flightradar24.com/39.81,-75.86/8", use_container_width=True)
    st.link_button("📊 FlightAware Tracking Portal", "https://www.flightaware.com/es-ES", use_container_width=True)
    st.link_button("🗃️ FAA NOTAM Data Center", "https://notams.aim.faa.gov/notamSearch/", use_container_width=True)
    st.link_button("✈️ AOPA Destinations & Airports Center", "https://aopa.org/destinations/?t=airports&_gl=1*6m0wou*_gcl_au*MTI4MDE3NzQzNC4xNzc3OTg3Nzk3*_ga*MjgxMDY5NjQ4LjE3Nzc5ODc3ODA.*_ga_SM42H3BVW5*czE3Nzc5ODc3ODAkbzEkZzEkdDE3Nzc5ODc5NzEkajYwJGwwJGgxMTMyNjg1NTQz", use_container_width=True)

# --- RIGHT COLUMN: METEOROLOGY & FORECASTS ---
with col_right:
    st.subheader("⛈️ Real-Time Weather Center")
    
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
