import base64
import os
import streamlit as st
import warnings

# Suppress warnings
warnings.simplefilter("ignore", category=DeprecationWarning)
current_dir = os.path.dirname(os.path.abspath(__file__))
def configure_page():
    # Page configuration

    st.set_page_config(
        page_title="Docucontext",
        page_icon=os.path.join(current_dir, "images/home.png"),
        layout="centered",
        initial_sidebar_state="expanded"
    )
def remove_footer_menu():
    
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
                content:'© 2023 | Dlytica Inc.'; 
                visibility: visible;
                display: block;
                position: relative;
                color: black;
                padding: 5px;
                top: 2px;
            }
            .feedback-form-url {color:rgb(12, 90, 219) !important}
            .e1fqkh3o9{max-height:80vh!important;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)   

@st.cache_data()
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache_data()
def get_img_with_href(local_img_path, target_url):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}">
            <img width="150px" src="data:image/{img_format};base64,{bin_str}" />
        </a>'''
    return html_code

def sidebar_content():
    with st.sidebar:
        logo_html = get_img_with_href(os.path.join('images','dlytica.png'), 'https://dlytica.com')
        st.markdown(logo_html, unsafe_allow_html=True)
        st.markdown("<b>Here to deliver data driven AI and cloud solutions.</b><br>",unsafe_allow_html=True)
        st.markdown("")
        st.markdown("")
        feedback = """ We value your feedback! Help us shape the final product by sharing your thoughts.
                <a class="feedback-form-url" target="_blank" href='https://www.dlytica.com/product/feedback-form'>Feedback Form</a>"""
        styled_text = f'<div style="margin-top:15px; margin-bottom:15px; padding: 10px; border-radius: 2px;">{feedback} </div>'

        st.markdown(styled_text, unsafe_allow_html=True)

        # st.markdown(
        #     """
        #     <div>
        #         <a target="_blank" href="https://forms.office.com/pages/responsepage.aspx?id=PsAfr2kbCUyPmtCeXh2-nxX71AiW0GVAvMIjaiJQpoxUOEkzTkVMS0E2NlVSUzJWSUc0SDZGTjlDUC4u">
        #             <button type="button" class="btn btn-primary">Feedback Form</button>
        #         </a>
        #     </div>
        #     """,
        #     unsafe_allow_html=True
        # )

       

        

         