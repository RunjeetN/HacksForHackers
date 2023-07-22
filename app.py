import streamlit as st

st.title(':spades: Welcome to :blue[Poker Night] :clubs:')
st.divider() # line dividing title



col1, col2, col3 = st.columns(3)

with col1:
    st.header("What Is It?")
    st.write("Are you tired of tracking who owes what when trying to play a fun game of poker with the boys(TM)? Well no need to worry because Poker Night has got you covered! Poker Night is a web app that allows you to create and join ranked games of poker with your friends, set the buy-in, and automatically disburse the winnings based on the results of the game!")

with col2:
    st.header("How to use it?")
    st.write("You can choose between creating a game or joining one that already exists. Creating a game will allow you to set the buy-in and automatically generate an access code that you can send to your friends. When joining a game, users will input the access code and select their display name. This is what will show up on the leaderboards after the game is over! Lastly, if you are joining a game you can pay the buy-in using Venmo/Circle. [TBD]")

with col3: 
    st.header("Under the Hood")
    st.write("Poker Night was coded entirely in python using Streamlit. User data is stored in a local SQL server which is natively supported by Streamlit and hosted on Microsoft Cloud. All payments are processed with the Circle/Venmo API. ")


st.warning("Please Register to Continue")

