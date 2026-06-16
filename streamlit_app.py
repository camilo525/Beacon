import streamlit as st
from datetime import datetime, timedelta

# 1. MANAGEMENT APP CONFIGURATION
st.set_page_config(
    page_title="BEACON | Operational Command Center",
    page_icon=":globe_with_meridians:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- BRAND EXTRACTION LAYER (TOP) ---
top_logo_col1, top_logo_col2, top_logo_col3 = st.columns([1, 0.8, 1])
with top_logo_col2:
    st.image(
        "https://thrust-aviation.com/wp-content/uploads/2024/02/Logo-White-500-2-e1710003051285.png",
        use_container_width=True
    )

# CLEAN MANAGEMENT SUB-HEADER
st.markdown("##  **BEACON**")
st.caption("Flight Support Central Command Hub")
st.divider()

# 2. CHRONOMETER SUITE (GLOBAL OPERATIONS MATRIX)
st.write("⏱️ **GLOBAL DEPARTURE TIMES**")
now_utc = datetime.utcnow()
edt = now_utc - timedelta(hours=4)
cdt = now_utc - timedelta(hours=5)
mdt = now_utc - timedelta(hours=6)
pdt = now_utc - timedelta(hours=7)

# Render Clocks Layout inside a clean metric ribbon
clock_cols = st.columns(5)
zones = [
    ("GMT / UTC", f"{now_utc.strftime('%H:%M')} Z", "Global Basis"),
    ("Eastern (EDT)", edt.strftime("%H:%M"), "New York / Miami"),
    ("Central (CDT)", cdt.strftime("%H:%M"), "Houston / Chicago"),
    ("Mountain (MDT)", mdt.strftime("%H:%M"), "Denver"),
    ("Pacific (PDT)", pdt.strftime("%H:%M"), "Los Angeles / Seattle")
]

for col, (label, value, delta) in zip(clock_cols, zones):
    with col:
        st.metric(label=label, value=value, delta=delta, delta_color="off")

st.divider()

# --- INSTANT DISPATCH DISCOVERY AIRPORT SEARCH ---
st.write("🔍 **RAPID DISPATCH ROUTING MAP**")
icao_input = st.text_input(
    "Global ICAO Identifier Search", 
    placeholder="Type ICAO Airport Code (e.g., KJFK, MMUN, LEMD)...",
    label_visibility="collapsed"
).upper().strip()

if icao_input:
    if len(icao_input) >= 3:
        with st.container(border=True):
            st.markdown(f"📡 **Operational Airfield Interface Matrix: {icao_input}**")
            st.write("Direct external routing paths compiled for active flight logging:")
            
            link_col1, link_col2, link_col3, link_col4 = st.columns(4)
            with link_col1:
                st.link_button("📑 METAR & TAF Flight Weather", f"https://metar-taf.com/{icao_input}", use_container_width=True, type="primary")
            with link_col2:
                st.link_button("🛬 FlightAware Live Portal", f"https://www.flightaware.com/resources/airport/{icao_input}", use_container_width=True)
            with link_col3:
                st.link_button("🗺️ SkyVector Route Charts", f"https://skyvector.com/airport/{icao_input}", use_container_width=True)
            with link_col4:
                st.link_button("📡 FlightRadar24 Ground Tracking", f"https://www.flightradar24.com/data/airports/{icao_input.lower()}", use_container_width=True)
    else:
        st.warning("Systems require a standard 3 or 4 letter validation code.")

st.write("##")

# 3. EXECUTIVE UTILITY INTERFACE GRID
col_left, col_center, col_right = st.columns([1.1, 1, 1.2], gap="large")

# --- PROPRIETARY APPLICATIONS MATRIX ---
with col_left:
    st.markdown("### 🛠️ **Proprietary Ecosystem**")
    st.write("Secured internal workflow engines:")
    
    with st.container(border=True):
        st.markdown("🛡️ **Operational Mission Assessment**")
        st.caption("Active risk management profiles & route authorization rules.")
        st.link_button("Execute Risk Profile", "https://thrust-aviation-flightsupport-weather-assessment.streamlit.app/", type="primary", use_container_width=True)
    
    st.write("##")
    with st.container(border=True):
        st.markdown("✉️ **Client Communications Matrix**")
        st.caption("Centralized client broadcast configurations & scripts.")
        st.link_button("Launch Comms Portal", "https://thrust-aviation-flightsupport-scripts.streamlit.app/", use_container_width=True)
    
    st.write("##")
    with st.container(border=True):
        st.markdown("📄 **Contracts & Compliance Engine**")
        st.caption("Global regulatory parsing & contract safety matching.")
        st.link_button("Verify Documentation", "https://thrust-contract-compliance.streamlit.app/", use_container_width=True)

# --- NATIONAL AIRSPACE CONTROL PLATFORM ---
with col_center:
    st.markdown("### ✈️ **Airspace Infrastructure**")
    st.write("National civil control frameworks:")
    
    with st.container(border=True):
        st.write("🌐 **Federal Regulatory Links**")
        st.link_button("Graphic TFR Advisories (FAA)", "https://tfr.faa.gov/tfr3/?page=list", use_container_width=True)
        st.link_button("National Airspace System Status", "https://nasstatus.faa.gov/", use_container_width=True)
        st.link_button("FAA Official NOTAM Data Registry", "https://notams.aim.faa.gov/notamSearch/", use_container_width=True)
    
    st.write("##")
    with st.container(border=True):
        st.write("🛰️ **Live Operational Feeds**")
        st.link_button("FlightRadar24 Sector Tracker", "https://www.flightradar24.com/39.81,-75.86/8", use_container_width=True)
        st.link_button("FlightAware Primary Tracker", "https://www.flightaware.com/es-ES", use_container_width=True)
        st.link_button("AOPA Flight Destination Profiles", "https://aopa.org/destinations/?t=airports&_gl=1*6m0wou*_gcl_au*MTI4MDE3NzQzNC4xNzc3OTg3Nzk3*_ga*MjgxMDY5NjQ4LjE3Nzc5ODc3ODA.*_ga_SM42H3BVW5*czE3Nzc5ODc3ODAkbzEkZzEkdDE3Nzc5ODc5NzEkajYwJGwwJGgxMTMyNjg1NTQz", use_container_width=True)

# --- REAL-TIME ENVIRONMENTAL ANALYSIS COLUMN ---
with col_right:
    st.markdown("### ⛈️ **Meteorological Suite**")
    st.write("Real-time live environmental mapping:")
    
    with st.container(border=True):
        st.markdown("🛰️ **Weather Underground Infrared**")
        st.link_button("🚀 Open Fullscreen Infrared Matrix", "https://www.wunderground.com/maps/satellite/regional-infrared", type="primary", use_container_width=True)
    
    st.write("##")
    # Interactive Base Map Loop
    st.components.v1.iframe(
        src="https://embed.windy.com/embed2.html?lat=39.50&lon=-98.35&zoom=4&level=surface&overlay=radar&menu=&message=&marker=&calendar=&pressure=&type=map&location=coordinates&detail=&metricWind=kt&metricTemp=%C2%B0F&radarRange=-1",
        height=280,
        scrolling=False
    )
    
    st.write("##")
    with st.container(border=True):
        st.write("📊 **Tactical Weather References**")
        st.link_button("📑 Regional METAR / TAF Map Search", "https://metar-taf.com/?c=158495.-809033.4#google_vignette", use_container_width=True)
        st.link_button("🌀 National Hurricane Center Radar (NHC)", "https://www.nhc.noaa.gov/", use_container_width=True)
        st.link_button("🗺️ NOAA/NWS National Forecast Charts", "https://www.weather.gov/forecastmaps/", use_container_width=True)

st.write("##")
st.divider()
st.write("##")

# --- ARGUS PREMIUM COMPLIANCE CERTIFICATION ---
bottom_logo_col1, bottom_logo_col2, bottom_logo_col3 = st.columns([1, 0.4, 1])
with bottom_logo_col2:
    st.image(
        "https://static.wixstatic.com/media/5f5db0_d7471efb590b4734a38048043fb3b2c1~mv2.png/v1/fill/w_300,h_300,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/FBO%20Audit%20Logo%20Silver.png",
        caption="ARGUS Platinum Certified Operational Center",
        use_container_width=True
    )
