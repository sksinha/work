import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("📍 Medical College Locator with Tooltips")

# File uploader
uploaded_file = st.sidebar.file_uploader(
    "Upload a CSV or Excel file with 'Medical College', 'Latitude', 'Longitude', 'location', 'cat' columns",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:
    # Read file based on extension
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
 # Select Map Style
        map_styles = {
            "Light": "mapbox://styles/mapbox/light-v9",
            "Dark": "mapbox://styles/mapbox/dark-v9",
            "Streets": "mapbox://styles/mapbox/streets-v11",
            "Outdoors": "mapbox://styles/mapbox/outdoors-v11",
            "Satellite": "mapbox://styles/mapbox/satellite-v9",
            "Satellite Streets": "mapbox://styles/mapbox/satellite-streets-v11"
        }
        selected_style = st.selectbox("Choose Mapbox Style", list(map_styles.keys()))
    # Dropdown to select college
    college_selected = st.selectbox("Select a Medical College", df['Medical College'].unique())

    # Filter the DataFrame
    selected_df = df[df['Medical College'] == college_selected]

    # Show selected data
    st.subheader("Selected Medical College Details")
    df.reset_index(drop=True, inplace=True)
    df.insert(0, "Sl. No.", range(1, len(df) + 1))
    st.dataframe(selected_df)

    # Center map on selected location
    view_state = pdk.ViewState(
        latitude=selected_df['Latitude'].values[0],
        longitude=selected_df['Longitude'].values[0],
        zoom=5,
        pitch=0
    )

    # Tooltip
    tooltip = {
        "html": "<b>{Medical College}</b><br/>Location: {location}<br/>Location1: {location1}<br/>Lat: {Latitude}<br/>Lon: {Longitude}",
        "style": {
            "backgroundColor": "navy",
            "color": "white"
        }
    }

    # Pydeck chart
    st.subheader("🗺️ Map View")
    st.pydeck_chart(pdk.Deck(
        #map_style='mapbox://styles/mapbox/light-v9',
        #map_style='mapbox://styles/mapbox/streets-v11',
        #map_style='mapbox://styles/mapbox/satellite-streets-v11',
        map_style=map_styles[selected_style],
        initial_view_state=view_state,
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=selected_df,
                get_position='[Longitude, Latitude]',
                get_color='[255, 0, 0, 160]',
                get_radius=9000,
                pickable=True
            )
        ],
        tooltip=tooltip
    ))
else:
    st.info("Please upload a CSV or Excel file to begin.")
