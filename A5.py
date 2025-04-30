import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("Medical College Locator with Category Colors & Zoom Control")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV with columns: 'Medical College', 'Latitude', 'Longitude', 'location', 'cat'", type="csv")

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Standardize column names
    df.columns = df.columns.str.strip().str.title()
    required_cols = {'Medical College', 'Latitude', 'Longitude', 'Location', 'Cat'}
    
    if not required_cols.issubset(df.columns):
        st.error(f"CSV must contain the following columns: {required_cols}")
    else:
        st.success("File uploaded successfully!")

        # Dropdown to select college
        college_selected = st.selectbox("Select a Medical College", df['Medical College'].unique())

        # Filter the DataFrame
        selected_df = df[df['Medical College'] == college_selected]

        # Show selected data
        st.subheader("Selected Medical College")
        st.dataframe(selected_df)

        # Color mapping based on category
        unique_cats = df['Cat'].unique()
        color_map = {cat: [int(hash(cat + str(i)) % 255) for i in range(3)] + [160] for cat in unique_cats}

        df['color'] = df['Cat'].apply(lambda x: color_map.get(x, [0, 150, 200, 160]))

        # Zoom slider
        zoom_level = st.slider("Map Zoom Level", 2, 16, 6)

        # Define Pydeck layer with all colleges shown, but highlight selection
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=df,
            get_position='[Longitude, Latitude]',
            get_color='color',
            get_radius=40000,
            pickable=True
        )

        # View centered on selected college
        if not selected_df[['Latitude', 'Longitude']].isnull().any().any():
            view_state = pdk.ViewState(
                latitude=selected_df['Latitude'].values[0],
                longitude=selected_df['Longitude'].values[0],
                zoom=zoom_level,
                pitch=0
            )

            tooltip = {
                "html": """
                    <b>{Medical College}</b><br/>
                    Location: {Location}<br/>
                    Category: {Cat}<br/>
                    Lat: {Latitude}<br/>
                    Lon: {Longitude}
                """,
                "style": {"backgroundColor": "navy", "color": "white"}
            }

            # Display map
            st.subheader("Colleges on Map")
            st.pydeck_chart(pdk.Deck(
                layers=[layer],
                initial_view_state=view_state,
                tooltip=tooltip
            ))
        else:
            st.warning("Selected college does not have valid coordinates.")
else:
    st.info("Please upload a CSV file to begin.")
