import streamlit as st
import datetime
with st.form(key='my_form'):
	text_input = st.text_input(label='Name')
	text1_input = st.text_input(label='EMP Code')
	text2_input = st.text_input(label='Date of Birth')
	d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
	#text3_input = st.text_input(label='Year of retirement')
	#d1 = st.date_input("Year of Requirement", datetime.year(1950))
	year = st.selectbox('Year', range(1990, 2021))
	#text4_input = st.text_input(label='Current Occupation')
	CurOption=st.selectbox('Current Occupatio', ['Retired Happy Life', 'Business','Inforation Technology', 'Social Service'], key=2)
	#text5_input = st.text_input(label='Intrest Area')
	IntrestArea=st.selectbox('Select Intrest Area', ['Sports', 'Politics','Inforation Technology', 'Social Service'], key=2)
	submit_button = st.form_submit_button(label='Submit')
