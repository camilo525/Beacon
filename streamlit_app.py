# --- RIGHT COLUMN: METEOROLOGY & FORECASTS ---
with col_right:
    st.subheader("⛈️ Real-Time Weather Center")
    
    with st.container(border=True):
        st.markdown("#### 🛰️ Weather Underground Radar")
        st.caption("Access the Regional Infrared Tracking Matrix directly.")
        st.link_button("🚀 Launch Regional Infrared Map", "https://www.wunderground.com/maps/satellite/regional-infrared", type="primary", use_container_width=True)
    
    st.write("##")
    st.markdown("**Live National Base Radar Loop**")
    st.components.v1.iframe(
        src="https://embed.windy.com/embed2.html?lat=39.50&lon=-98.35&zoom=4&level=surface&overlay=radar&menu=&message=&marker=&calendar=&pressure=&type=map&location=coordinates&detail=&metricWind=kt&metricTemp=%C2%B0F&radarRange=-1",
        height=300,
        scrolling=False
    )
    
    st.write("##")
    st.markdown("**Meteorological Dashboards**")
    # Added your missing dispatch links below:
    st.link_button("📑 TAF / METAR Regional Search", "https://metar-taf.com/?c=158495.-809033.4#google_vignette", use_container_width=True)
    st.link_button("🌀 National Hurricane Center (NHC)", "https://www.nhc.noaa.gov/", use_container_width=True)
    st.link_button("🗺️ NWS National Forecast Maps", "https://www.weather.gov/forecastmaps/", use_container_width=True)
