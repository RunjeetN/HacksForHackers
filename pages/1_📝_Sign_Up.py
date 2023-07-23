import streamlit as st
import User
import mysql.connector

# establish connection to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Netflix9722!",
    database="mydb"
)

myCursor = mydb.cursor()

def storeData(name, number, email, password, org):
    sql= "insert into users(name,number,email,password,org) values(%s,%s,%s,%s,%s)"
    val= (name,number,email,password,org)
    myCursor.execute(sql,val)
    mydb.commit()
    st.success("Record Created Successfully!!!")

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
        password = st.text_input(label="Password", placeholder="pass123...")
        org = st.text_input(label="Fraternity/Sorority", placeholder="N/A")
        
        submitBtn = st.form_submit_button(label="Sign Up", on_click=storeData(name, number, email, password, org), disabled=False, use_container_width=True) #TODO: SETUP STORE DATA FUNCTION TO CREATE AND STORE USER OBJECT




