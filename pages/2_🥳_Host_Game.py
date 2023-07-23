import streamlit as st
import random
import string

def generateCode():
    letters = string.ascii_lowercase
    length = 10
    code = ''.join(random.choice(letters) for i in range(length))
    return code

col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.number_input(label = 'Number of Players', value=1, min_value=1)
    st.number_input(label = 'Minimum Buy In', value=1, min_value=0)
    table = st.button('Generate Table')
    
    if table:
        #Implement TableID generator with connection to backend database
        TableID = generateCode()
        st.text('Copy Invite Link:')
        st.text(TableID)