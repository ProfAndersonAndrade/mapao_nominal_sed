import streamlit as st
from streamlit_lottie import st_lottie



def animation(json):    
    st.sidebar.empty()
    st_lottie(json)
    


