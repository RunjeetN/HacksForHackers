import streamlit as st
import User
def storeData(name, number, email, org):
    user = new User(name, number, email, org)

titleCol, formCol = st.columns([0.3, 0.7])

with titleCol:
    
    container = st.container()
    container.title("Sign Up")

with formCol:
    regForm = st.form("regForm")

    with regForm:
        name = st.text_input(label="Name", placeholder="Johnny Sins")
        number = st.text_input(label="Phone", placeholder="(999) 999-9999")
        email = st.text_input(label="Email", placeholder="AndrewTate@HustlersUniversity.edu")
        org = st.text_input(label="Fraternity/Sorority", placeholder="N/A")
        
        submitBtn = st.form_submit_button(label="Sign Up", on_click=storeData(), disabled=False, use_container_width=True)




