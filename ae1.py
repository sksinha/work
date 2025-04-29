import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("Map of Medical Colleges in India with Tooltips")

# Sample medical college data
data = {
    'Medical College': [
        'AIIMS New Delhi', 
        'CMC Vellore', 
        'KGMU Lucknow', 
        'AFMC Pune', 
        'BJMC Ahmedabad'
    ],
    'Latitude': [
        28.5672,
        12.9260,
        26.8643,
        18.5164,
        23.0300
    ],
    'Longitude': [
        77.2100,
        79.1325,
        80.9490,
        73.8567,
        72.5800
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

st.subheader("Medical College Data")
st.dataframe(df)

# Define Pydeck layer
layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position='[Longitude, Latitude]',
    get_color='[200, 30, 0, 160]',
    get_radius=50000,
    pickable=True
)

# Set the view
view_state = pdk.ViewState(
    latitude=22.9734,
    longitude=78.6569,
    zoom=4,
    pitch=0
)

# Tooltip
tooltip = {
    "html": "<b>{Medical College}</b><br/>Lat: {Latitude}<br/>Lon: {Longitude}",
    "style": {
        "backgroundColor": "steelblue",
        "color": "white"
    }
}

# Show pydeck chart
st.subheader("Map with Tooltips")
st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip=tooltip
))
