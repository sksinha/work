import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("Medical College Locator with Selection and Tooltips")

# Sample medical college data
data = {
    'Medical College': [
        'AIIMS New Delhi', 
        'AIIMS New Delhi',
        'CMC Vellore', 
        'KGMU Lucknow', 
        'AFMC Pune', 
        'BJMC Ahmedabad'
    ],
    'Latitude': [
        28.5672,
        28.5472,
        12.9260,
        26.8643,
        18.5164,
        23.0300
    ],
    'Longitude': [
        77.2100,
        77.2200,
        79.1325,
        80.9490,
        73.8567,
        72.5800
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Dropdown for college selection
college_selected = st.selectbox("Select a Medical College", options=df['Medical College'])

# Filter to selected college
selected_df = df[df['Medical College'] == college_selected]

# Display data
st.subheader("Selected Medical College Data")
st.dataframe(selected_df)

# Define Pydeck layer for the selected college
layer = pdk.Layer(
    "ScatterplotLayer",
    data=selected_df,
    get_position='[Longitude, Latitude]',
    get_color='[0, 100, 200, 160]',
    get_radius=50000,
    pickable=True
)

# Set view to selected college
view_state = pdk.ViewState(
    latitude=selected_df['Latitude'].values[0],
    longitude=selected_df['Longitude'].values[0],
    zoom=8,
    pitch=0
)

# Tooltip
tooltip = {
    "html": "<b>{Medical College}</b><br/>Lat: {Latitude}<br/>Lon: {Longitude}",
    "style": {
        "backgroundColor": "navy",
        "color": "white"
    }
}

# Show map
st.subheader("Map View")
st.pydeck_chart(pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip=tooltip
))
