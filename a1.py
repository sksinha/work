import streamlit as st
with st.form(key='my_form'):
	text_input = st.text_input(label='Enter some text')
	submit_button = st.form_submit_button(label='Submit')
if submit:
    st.write(f'hello {name}')
