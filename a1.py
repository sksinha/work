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


with st.form(key='my_form'):
	name = st.text_input(label='Name')
	des = st.text_input(label='Last Degination')
	empcode=st.text_input(label='Emp Code')
	email=st.text_input(label='E mail')
	#empcode = st.text_input(label='EMP Code')
	mobile = st.text_input(label='mobile no')
	db= st.date_input("When's your birthday", datetime.date(2019, 7, 6))
	dr= st.date_input("When's your Retirement", datetime.date(1950, 7, 6))
	CurOption=st.selectbox('Current Occupatio', ['Retired Happy Life', 'Business','Inforation Technology', 'Social Service'], key=2)
	InA=st.selectbox('Select Intrest Area', ['Sports', 'Politics','Inforation Technology', 'Social Service'], key=1)
	submit_button = st.form_submit_button(label='Submit')
d={'Name':[name],'Designaion':[des]}
if submit_button == True:
        st.markdown('<h3>Thank you for your feedback!</h3>', unsafe_allow_html=True)
        st.markdown('Submitted responses:')
	
	#d = {‘Name’: [name],‘Desigination’: [des],‘EmpCode’: [empCode],‘Email’: [email],‘Mobile’: [mobile]}
	#df = pd.DataFrame(data=d)
        st.write(d)
        #open('df.csv', 'w').write(df.to_csv())
        #else:
        #st.markdown("Click submit to save form responses.")
