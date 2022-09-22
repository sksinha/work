import streamlit as st
import datetime
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
      print("Valid email")
    else:
      print("Invalid email")

with st.form(key='my_form'):
	name = st.text_input(label='Name')
	emp = st.text_input(label='EMP Code')
	empcode=st.text_input(label='Emp Code')
	email=st.text_input(label='E mail')
	#empcode = st.text_input(label='EMP Code')
	mobile = st.text_input(label='mobile no')
	db= st.date_input("When's your birthday", datetime.date(2019, 7, 6))
	dr= st.date_input("When's your Retirement", datetime.date(1950, 7, 6))
	CurOption=st.selectbox('Current Occupatio', ['Retired Happy Life', 'Business','Inforation Technology', 'Social Service'], key=2)
	InA=st.selectbox('Select Intrest Area', ['Sports', 'Politics','Inforation Technology', 'Social Service'], key=1)
	submit_button = st.form_submit_button(label='Submit')
	isValid(email)
