import streamlit as st
with st.form(key='my_form'):
	text_input = st.text_input(label='Name')
	text1_input = st.text_input(label='EMP Code')
	text2_input = st.text_input(label='Date of Birth')
	text3_input = st.text_input(label='Year of retirement')
	text4_input = st.text_input(label='Current Occupation')
	text5_input = st.text_input(label='Intrest Area')
	st.selectbox('Select Intrest Area', ['Sports', 'Politics','Inforation Technology', 'Social Service'], key=2)
	submit_button = st.form_submit_button(label='Submit')
