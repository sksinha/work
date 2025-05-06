import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("📍 Medical College Locator with Tooltips")

# File uploader
uploaded_file = st.file_uploader(
    "Upload a CSV file with 'Medical College', 'Latitude', 'Longitude', 'location', 'cat' columns",
    type="csv"
)

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Validate required columns
    required_cols = {'Medical College', 'Latitude', 'Longitude', 'location', 'cat'}
    if not required_cols.issubset(df.columns):
        st.error(f"CSV must contain the following columns: {required_cols}")
    else:
        st.success("✅ File uploaded successfully!")

        # Dropdown to select college
        college_selected = st.selectbox("Select a Medical College", df['Medical College'].unique())

        # Filter the DataFrame
        selected_df = df[df['Medical College'] == college_selected]

        # Show selected data
        st.subheader("Selected Medical College Details")
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
            "html": "<b>{Medical College}</b><br/>Location: {location}<br/>Category: {cat}<br/>Lat: {Latitude}<br/>Lon: {Longitude}",
            "style": {
                "backgroundColor": "navy",
                "color": "white"
            }
        }

        # Pydeck chart
        st.subheader("🗺️ Map View")
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=view_state,
            layers=[
                pdk.Layer(
                    'ScatterplotLayer',
                    data=selected_df,
                    get_position='[Longitude, Latitude]',
                    get_color='[255, 0, 0, 160]',
                    get_radius=50000,
                    pickable=True
                )
            ],
            tooltip=tooltip
        ))

else:
    st.info("Please upload a CSV file to begin.")
