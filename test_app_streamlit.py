import streamlit as st

#Basic Hello World command
st.write("Hello world")

#Large centered My Dashboard command
st.markdown("<h1 style='text-align: center; color: black;'>My Dashboard</h1>", unsafe_allow_html=True)

#Columns
buffer, col2, col3, col4 = st.columns([1,4,4,2])
with col2:
    st.write("This is in column 2")
with col3:
    st.write("And column 3")
with col4:
    st.write("This column is half the size of 2 and 3")
    