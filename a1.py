import streamlit as st
with st.form(key='my_form'):
	name = st.text_input(label='Name')
  	d = st.date_input(  "When's your birthday", datetime.date(2019, 7, 6))
  
	submit_button = st.form_submit_button(label='Submit')
