import streamlit as st
import os
import traceback
from utilities.helper import LLMHelper
from streamlit_config import sidebar_content,configure_page,remove_footer_menu

configure_page()
remove_footer_menu()
sidebar_content()
try:
    # Set page layout to wide screen and menu item
    menu_items = {
	'Get help': None,
	'Report a bug': None,
	'About': '''
	 ## Embeddings App

	Document Reader Sample Demo.
	'''
    }


    llm_helper = LLMHelper()

    col1, col2, col3 = st.columns([2,1,1])

    files_data = llm_helper.blob_client.get_all_files()

    st.dataframe(files_data, use_container_width=True)

except Exception as e:
    st.error(traceback.format_exc())
