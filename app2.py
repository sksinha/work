import streamlit as st

import pandas as pd
data=pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2019/2019-10-29/nyc_squirrels.csv")
st.set_page_config(page_title=" Banking  Score card g ", page_icon="🐿")
st.title("The Central Park Squirrel Census🐿")
col1, col2, col3 = st.columns(3)


col1.metric("Number of recorded squirrels", len(data), len(data) - 2373)
col2.metric(
    "Squirrels per hectare",
    round(len(data) / 350, 2),
    round((len(data) - 2373) / 350, 2))
col3.metric("Number of primary colors", 3)

st.markdown("# Alan Jones")
st.markdown("## Writer and Developer")
st.markdown("""
    I write articles about Data Science, Python and related topics. 
    The articles are mostly written on the Medium platform.
    
    You can find my articles [here](https://alan-jones.medium.com)
    and if you would like to know when I publish new ones, you can 
    sign up for an email alert on my Medium 
    [page](https://alan-jones.medium.com/subscribe).
    Below are a few articles you might find interesting...
""")

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("https://cdn-images-1.medium.com/max/906/1*dVSDol9pouoO9IX_E_-35Q.png")

    with text_col:
        st.subheader("A Multi-page Interactive Dashboard with Streamlit and Plotly")
        st.write("""Beautiful interactive multipage dashboards are made easy with Streamlit
            """)
        st.markdown("[Read more...](https://towardsdatascience.com/a-multi-page-interactive-dashboard-with-streamlit-and-plotly-c3182443871a)")
        
        

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("https://cdn-images-1.medium.com/max/906/1*hjhCIWGgLzOznTFwDyeIeA.png")

    with text_col:
        st.subheader("Rational UI Design with Streamlit")
        st.write("""
            From one point of view Streamlit is a retrograde step in web development because 
            it lets you mix up the logic of your app with the way it is presented. But from 
            another it is very much simplifying web design.""")
        st.markdown("[Read more...](https://towardsdatascience.com/rational-ui-design-with-streamlit-61619f7a6ea4)")
        
        
import hydralit_components as hc

#can apply customisation to almost all the properties of the card, including the progress bar
theme_bad = {'bgcolor': '#FFF0F0','title_color': 'red','content_color': 'red','icon_color': 'red', 'icon': 'fa fa-times-circle'}
theme_neutral = {'bgcolor': '#f9f9f9','title_color': 'orange','content_color': 'orange','icon_color': 'orange', 'icon': 'fa fa-question-circle'}
theme_good = {'bgcolor': '#EFF8F7','title_color': 'green','content_color': 'green','icon_color': 'green', 'icon': 'fa fa-check-circle'}

cc = st.columns(4)

with cc[0]:
 # can just use 'good', 'bad', 'neutral' sentiment to auto color the card
 hc.info_card(title='Some heading GOOD', content='All good!', sentiment='good',bar_value=77)

with cc[1]:
 hc.info_card(title='Some BAD BAD', content='This is really bad',bar_value=12,theme_override=theme_bad)

with cc[2]:
 hc.info_card(title='Some NEURAL', content='Oh yeah, sure.', sentiment='neutral',bar_value=55)

with cc[3]:
 #customise the the theming for a neutral content
 hc.info_card(title='Some NEURAL',content='Maybe...',key='sec',bar_value=5,theme_override=theme_neutral)
