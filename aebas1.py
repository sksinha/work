import streamlit as st
import pandas as pd

st.title("Map of Medical Colleges in India")

# Sample medical college data (add more as needed)
data = {
    'Medical College': [
        'AIIMS New Delhi', 
        'CMC Vellore', 
        'KGMU Lucknow', 
        'AFMC Pune', 
        'BJMC Ahmedabad'
    ],
    'Latitude': [
        28.5672,  # AIIMS Delhi
        12.9260,  # CMC Vellore
        26.8643,  # KGMU
        18.5164,  # AFMC Pune
        23.0300   # BJMC Ahmedabad
    ],
    'Longitude': [
        77.2100,
        79.1325,
        80.9490,
        73.8567,
        72.5800
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Show data
st.subheader("Medical Colleges Data")
st.dataframe(df)

# Rename columns for st.map
map_df = df.rename(columns={"Latitude": "lat", "Longitude": "lon"})[['lat', 'lon']]

# Show map
st.subheader("Location on Map")
st.map(map_df, zoom=5)
