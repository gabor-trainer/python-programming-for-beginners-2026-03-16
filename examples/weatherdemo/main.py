import streamlit as st
import requests
import pandas as pd
from datetime import date, timedelta

st.set_page_config(page_title="Weather Trends", page_icon="🌤️", layout="wide")

st.title("🌤️ Historical Weather Trends")
st.caption("Powered by Open-Meteo · No API key required")

# --- Sidebar inputs ---
with st.sidebar:
    st.header("Settings")

    city = st.text_input("City name", value="London")

    col1, col2 = st.columns(2)
    default_end = date.today() - timedelta(days=6)
    default_start = default_end - timedelta(days=365)
    start_date = col1.date_input(
        "From", value=default_start, max_value=default_end)
    end_date = col2.date_input("To", value=default_end, max_value=default_end)

    variables = st.multiselect(
        "Variables to plot",
        options=[
            "Temperature (min/max/mean)",
            "Precipitation",
            "Wind speed",
            "Humidity",
        ],
        default=["Temperature (min/max/mean)"],
    )

    fetch = st.button("Fetch data", type="primary", use_container_width=True)

# --- Variable mapping ---
VARIABLE_MAP = {
    "Temperature (min/max/mean)": {
        "params": ["temperature_2m_max", "temperature_2m_min", "temperature_2m_mean"],
        "labels": ["Max °C", "Min °C", "Mean °C"],
        "title": "Temperature",
    },
    "Precipitation": {
        "params": ["precipitation_sum"],
        "labels": ["Precipitation (mm)"],
        "title": "Precipitation",
    },
    "Wind speed": {
        "params": ["wind_speed_10m_max"],
        "labels": ["Max wind speed (km/h)"],
        "title": "Wind Speed",
    },
    "Humidity": {
        "params": ["relative_humidity_2m_mean"],
        "labels": ["Mean humidity (%)"],
        "title": "Relative Humidity",
    },
}


def geocode(city_name: str) -> tuple[float, float, str]:
    """Return (lat, lon, display_name) for a city using Open-Meteo geocoding."""
    resp = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city_name, "count": 1, "language": "en"},
        timeout=10,
    )
    resp.raise_for_status()
    results = resp.json().get("results")
    if not results:
        return None, None, None
    r = results[0]
    display = f"{r['name']}, {r.get('admin1', '')}, {r.get('country', '')}".strip(
        ", ")
    return r["latitude"], r["longitude"], display


def fetch_weather(lat: float, lon: float, start: str, end: str, params: list[str]) -> pd.DataFrame:
    """Fetch daily historical weather from Open-Meteo archive API."""
    resp = requests.get(
        "https://archive-api.open-meteo.com/v1/archive",
        params={
            "latitude": lat,
            "longitude": lon,
            "start_date": start,
            "end_date": end,
            "daily": ",".join(params),
            "timezone": "auto",
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json().get("daily", {})
    df = pd.DataFrame(data)
    if "time" in df.columns:
        df["time"] = pd.to_datetime(df["time"])
        df = df.set_index("time")
    return df


# --- Main area ---
if fetch and city:
    lat, lon, display_name = geocode(city)

    if lat is None:
        st.error(f"Could not find **{city}**. Try a different spelling.")
        st.stop()

    st.subheader(f"📍 {display_name}")

    if start_date >= end_date:
        st.error("Start date must be before end date.")
        st.stop()

    # Collect all params needed
    all_params = []
    for v in variables:
        all_params.extend(VARIABLE_MAP[v]["params"])

    with st.spinner("Fetching historical data…"):
        df = fetch_weather(lat, lon, str(start_date),
                           str(end_date), all_params)

    if df.empty:
        st.warning("No data returned for this range. Try different dates.")
        st.stop()

    # Plot each variable group in its own chart
    for v in variables:
        mapping = VARIABLE_MAP[v]
        cols_present = [c for c in mapping["params"] if c in df.columns]
        if not cols_present:
            continue
        chart_df = df[cols_present].copy()
        chart_df.columns = [
            mapping["labels"][mapping["params"].index(c)] for c in cols_present
        ]
        st.markdown(f"### {mapping['title']}")
        st.line_chart(chart_df)

    # Show raw data in expander
    with st.expander("Raw data"):
        st.dataframe(df, use_container_width=True)

elif not fetch:
    st.info("Choose a city, date range, and variables in the sidebar, then click **Fetch data**.")
