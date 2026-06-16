import streamlit as st
from datetime import datetime, timedelta

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Beacon | Flight Support Command Center",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- THRUST LOGO (FIRST THING AT THE TOP) ---
top_logo_col1, top_logo_col2, top_logo_col3 = st.columns([1, 1, 1])
with top_logo_col2:
    st.image(
        "https://thrust-aviation.com/wp-content/uploads/2024/02/Logo-White-500-2-e1710003051285.png",
        use_container_width=True
    )

# NATIVE APP TITLE & CAPTION (No HTML strings to break the app)
st.title("🧭 BEACON")
st.caption("The centralized operations hub for Flight Support.")
st.write("---")

# 2. HEADER: TIME ZONES ONLY
now_utc = datetime.utcnow()
edt = now_utc - timedelta(hours=4)
cdt = now_utc - timedelta(hours=5)
mdt = now_utc - timedelta(hours=6)
pdt = now_utc - timedelta(hours=7)

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

# --- STANDARD ICAO SEARCH SECTION ---
st.markdown("### 🔍 Standard Airport Search")
icao_input = st.text_input("Enter Airport ICAO Code", placeholder="e.g., KJFK, MMUN, LEMD").upper().strip()

if icao_input:
    if len(icao_input) >= 3:
        with st.container(border=True):
            st.subheader(f"📊 Live Dispatch Links for: {icao_input}")
            st.write("Select a link below to instantly view real-time weather, TAFs, FBO directories, and chart data:")
            
            link_col1, link_col2, link_col3, link_col4 = st.columns(4)
            with link_col1:
                st.link_button("📑 METAR & TAF Weather", f"https://metar-taf.com/{icao_input}", use_container_width=True, type="primary")
            with link_col2:
                st.link_button("🛬 FlightAware Portal", f"https://www.flightaware.com/resources/airport/{icao_input}", use_container_width=True)
            with link_col3:
                st.link_button("🗺️ SkyVector Charts", f"https://skyvector.com/airport/{icao_input}", use_container_width=True)
            with link_col4:
                st.link_button("📡 Live Ground Radar", f"https://www.flightradar24.com/data/airports/{icao_input.lower()}", use_container_width=True)
    else:
        st.warning("Please enter a valid airport code (e.g., standard 3 or 4 letter identifiers).")

st.write("##")

# 3. MAIN DASHBOARD LAYOUT (THIS CREATES COL_RIGHT!)
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
    
    st.link_
