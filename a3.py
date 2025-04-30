import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("Medical College AEBAS LOG & Lat Viewer")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV with 'Medical College', 'Latitude', and 'Longitude' columns,location,cat", type="csv")

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Validate required columns
    required_cols = {'Medical College', 'Latitude', 'Longitude'}
    if not required_cols.issubset(df.columns):
        st.error(f"CSV must contain the following columns: {required_cols}")
    else:
        st.success("File uploaded successfully!")
        
        # Dropdown to select college
        college_selected = st.selectbox("Select a Medical College", df['Medical College'])

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
            zoom=8,
            pitch=0
        )

        # Tooltip
        tooltip = {
            "html": "<b>{Medical College}</b><br/>Location: {location}</br><br/> Cat : {cat}</b><br/>>Lat: {Latitude}<br/>Lon: {Longitude}",
            "style": {
                "backgroundColor": "navy",
                "color": "white"
            }
        }

        # Display map
        st.subheader("Map View")
        st.pydeck_chart(pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            tooltip=tooltip
        ) )
                     

else:
    st.info("Please upload a CSV file to begin.")
