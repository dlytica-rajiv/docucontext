import os
import streamlit as st
from streamlit_chat import message
from utilities.helper import LLMHelper
from streamlit_config import sidebar_content,configure_page,remove_footer_menu,get_img_with_href

configure_page()
remove_footer_menu()
sidebar_content()






def clear_text_input():
    st.session_state['question'] = st.session_state['input']
    st.session_state['input'] = ""

def clear_chat_data():
    st.session_state['input'] = ""
    st.session_state['chat_history'] = []
    st.session_state['source_documents'] = []

# Initialize chat history
if 'question' not in st.session_state:
    st.session_state['question'] = None
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'source_documents' not in st.session_state:
    st.session_state['source_documents'] = []

llm_helper = LLMHelper()

## Remove footer and setting option

logo_html = get_img_with_href(os.path.join('images','docucontext.png'), 'https://dlytica.com')

col1, col2 = st.columns([1,1])
with col1:
    # st.image(os.path.join('images','dlytica.jpeg'),"",200)
    st.markdown(logo_html, unsafe_allow_html=True)
    # st.markdown("<b>Here to deliver data driven AI and cloud solutions.</b><br>",unsafe_allow_html=True)
    # st.text("")

col1, col2, col3 = st.columns([2,2,2])
with col1:
    pass 
with col3:
    pass
    

st.text_input("Input: ", placeholder="type your question", key="input", on_change=clear_text_input)
clear_chat = st.button("Clear chat", key="clear_chat", on_click=clear_chat_data)

if st.session_state['question']:
    question, result, _, sources = llm_helper.get_semantic_answer_lang_chain(st.session_state['question'], st.session_state['chat_history'])
    st.session_state['chat_history'].append((question, result))
    st.session_state['source_documents'].append(sources)

if st.session_state['chat_history']:
    for i in range(len(st.session_state['chat_history'])-1, -1, -1):
        message(st.session_state['chat_history'][i][1], key=str(i))
        st.markdown(f'\n\nSources: {st.session_state["source_documents"][i]}')
        message(st.session_state['chat_history'][i][0], is_user=True, key=str(i) + '_user')