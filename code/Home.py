import base64
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import traceback
from utilities.helper import LLMHelper
from streamlit_config import configure_page,remove_footer_menu, get_img_with_href

import logging
logger = logging.getLogger('azure.core.pipeline.policies.http_logging_policy').setLevel(logging.WARNING)

import streamlit as st
import pandas as pd

import streamlit as st
from PIL import Image

configure_page()
remove_footer_menu()

# Load and display the logo image
logo_html = get_img_with_href(os.path.join('images','dlytica.jpeg'), 'https://dlytica.com')

col1, col2 = st.columns([1,1])
with col1:
    # st.image(os.path.join('images','dlytica.jpeg'),"",200)
    st.markdown(logo_html, unsafe_allow_html=True)
    st.markdown("<b>Here to deliver data driven AI and cloud solutions.</b><br>",unsafe_allow_html=True)
    # st.text("")

def add_bullet_points(text):
    lines = text.split('\n')  # Split the text into lines

    # Add bullet points to each line
    bullet_lines = ['• ' + line.strip() for line in lines]

    # Join the lines back together
    bullet_text = '\n'.join(bullet_lines)

    return bullet_text

def get_message(option):
    messages = {
        "What is Docucontext":"""
            DocuContext (An Intelligent Document Processing).
            A Cloud-native AI-powered document processing solution.
            Automates the Extraction and Analysis of unstructured data from various types of documents.
            Powered by Generative AI ChatGPT.
        """,
        "Why we use Docucontext":"""
            Eliminate manual data entry and transcription errors.
            Lack of standardization in document formats and layouts.
            Insufficient search and retrieval capabilities to find and access specific information within them.
            Challenges in integrating with other software applications and systems.
            High cost of customer acquisition and retention with limited ability to personalize customer experience.
        
        """,
        "What we use": "Powered by GPT 4 and Azure Cloud."
    }
    return messages.get(option, "")

# Set title and options for the dropdown menu
dropdown_title = "**EXPLORE**"
dropdown_options = ["What is Docucontext", "Why we use Docucontext", "What we use"]

# Create the dropdown component
selected_option = st.selectbox(dropdown_title, dropdown_options)

# Display the selected option and the message
if selected_option:
    message = get_message(selected_option)


def add_bullet_points(text):
    filter=text.lstrip().rstrip()
    lines = filter.split('\n')  # Split the text into lines
    # Add bullet points to each line and insert line break tags
    bullet_lines = ['• ' + line.strip() + '<br>' for line in lines]
    # Join the lines back together
    bullet_text = ''.join(bullet_lines)

    return bullet_text


# Example usage
original_text = message
bullet_text = add_bullet_points(original_text)

styled_text = f'<div style="background-color: rgb(240, 242, 246); padding: 20px; border-radius: 10px;">{bullet_text}</div>'

st.markdown(styled_text, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .btn-primary {
        -webkit-box-align: center;
        align-items: center;
        -webkit-box-pack: center;
        justify-content: center;
        font-weight: 400;
        padding: 0.25rem 0.75rem;
        border-radius: 0.25rem;
        margin: 0px;
        line-height: 1.6;
        color: inherit;
        width: auto;
        user-select: none;
        background-color: rgb(255, 255, 255);
        border: 1px solid rgba(49, 51, 63, 0.2);
        display: inline-block;
        margin-right: 10px;
    }
    .btn-primary:hover {
        border: 1px solid rgb(255, 80, 80);;
        color: black;
    }
    a {
        color: black !important;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div>
        <a href="/Add_Document">
            <button type="button" class="btn btn-primary">Add Document</button>
        </a>
        <a href="/Document_Viewer">
            <button type="button" class="btn btn-primary">View Document</button>
        </a>
        <a href="/Chat">
            <button type="button" class="btn btn-primary">Chat</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

feedback = 'We value your feedback! Help us shape the final product by sharing your thoughts.'

styled_text = f'<div style="background-color: rgb(240, 242, 246); margin-top:15px; margin-bottom:15px; padding: 10px; border-radius: 2px;">{feedback} </div>'

st.markdown(styled_text, unsafe_allow_html=True)

st.markdown(
    """
    <div>
        <a target="_blank" href="https://forms.office.com/pages/responsepage.aspx?id=PsAfr2kbCUyPmtCeXh2-nxX71AiW0GVAvMIjaiJQpoxUOEkzTkVMS0E2NlVSUzJWSUc0SDZGTjlDUC4u">
            <button type="button" class="btn btn-primary">Feedback Form</button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
