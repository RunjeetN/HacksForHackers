import random
import string
from turtle import onclick
import streamlit as st

def joinGame():
    print("stuff happened")

title = st.title("Join Game")


container = st.container()

with container:
    code = st.text_input(label="Game Code", placeholder="123xyz...")
    name = st.text_input(label="Display Name", placeholder="Johnny Sins")
    join = st.button("Join Game!")

    if(join):
        joinGame()