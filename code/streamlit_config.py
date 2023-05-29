import os
import streamlit as st
current_dir = os.path.dirname(os.path.abspath(__file__))
def configure_page():
    # Page configuration

    st.set_page_config(
        page_title="Docucontext",
        page_icon=os.path.join(current_dir, "images/home.png"),
        layout="centered",
        initial_sidebar_state="collapsed"
    )
def remove_footer_menu():
    
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)   
