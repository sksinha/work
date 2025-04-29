import streamlit as st
import pandas as pd

st.title("Map from Latitude and Longitude (DataFrame)")

# Sample data - replace or upload your own
data = {
    'Place': ['Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Bengaluru'],
    'Latitude': [28.6139, 19.0760, 22.5726, 13.0827, 12.9716],
    'Longitude': [77.2090, 72.8777, 88.3639, 80.2707, 77.5946]
}

# Convert to DataFrame
df = pd.DataFrame(data)

st.subheader("Data Preview")
st.dataframe(df)

# Convert to format required by st.map()
map_data = df.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})[['lat', 'lon']]

st.subheader("Map View")
st.map(map_data, zoom=4)
