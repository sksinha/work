import streamlit as st
import datetime
import re
st.set_page_config(page_title='NIC Retired portal', layout='centered')

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
# get the pages on nav


# user interaction 
st.sidebar.title('Navigation')
option = st.selectbox(
    'Select you options',
    ('About', 'View', 'Entry')



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
if submit_button:
    isValid(email)
