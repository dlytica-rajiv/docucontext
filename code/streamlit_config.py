import base64
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
            footer:after {
                content:'© Dlytica Inc.'; 
                visibility: visible;
                display: block;
                position: relative;
                color: black;
                padding: 5px;
                top: 2px;
            }
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)   

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache(allow_output_mutation=True)
def get_img_with_href(local_img_path, target_url):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}">
            <img width="200px" src="data:image/{img_format};base64,{bin_str}" />
        </a>'''
    return html_code
