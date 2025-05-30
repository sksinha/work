import streamlit as st
import pandas as pd
import pydeck as pdk

# File uploader
uploaded_file = st.file_uploader("Upload a CSV with 'Medical College', 'Latitude', 'Longitude', 'location', 'cat'", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Validate required columns
    required_cols = {'Medical College', 'Latitude', 'Longitude', 'location', 'cat'}
    missing_cols = required_cols - set(df.columns)
    if missing_cols:
        st.error(f"CSV is missing required columns: {missing_cols}")
        st.stop()
    
    st.success("File uploaded successfully!")

    # Dropdown to select college
    college_selected = st.selectbox("Select a Medical College", df['Medical College'].unique())

    # Filter the DataFrame
    selected_df = df[df['Medical College'] == college_selected]

    # Show selected data
    st.subheader("Selected Medical College")
    st.dataframe(selected_df)

    # Define Pydeck layer
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=selected_df,
        get_position='[Longitude, Latitude]',
        get_color='[0, 150, 200, 160]',
        get_radius=50000,
        pickable=True
    )

    # Center map on selected location
    view_state = pdk.ViewState(
        latitude=selected_df['Latitude'].values[0],
        longitude=selected_df['Longitude'].values[0],
        zoom=4,
        pitch=0
    )

    # Tooltip
    tooltip = {
        "html": "<b>{Medical College}</b><br/>Location: {location}</br>Cat: {cat}</b><br/>Lat: {Latitude}<br/>Lon: {Longitude}",
        "style": {
            "backgroundColor": "navy",
            "color": "white"
        }
    }

    # Display map
    st.subheader("Lat & Long View")
    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip=tooltip
    ))

else:
    st.info("Please upload a CSV file to begin.")
