from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import traceback
from utilities.helper import LLMHelper
from streamlit_config import configure_page,remove_footer_menu

import logging
logger = logging.getLogger('azure.core.pipeline.policies.http_logging_policy').setLevel(logging.WARNING)

import streamlit as st
import pandas as pd

import streamlit as st
from PIL import Image

configure_page()
remove_footer_menu()

# Load and display the logo image

col1, col2, col3 = st.columns([1,1,1])
with col1:
    st.image(os.path.join('images','dlytica.jpeg'))

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
        "What we use": "Powered by GPT!"
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

styled_text = f'<div style="background-color: rgba(28, 131, 225, 0.1); padding: 20px; border-radius: 10px;">{bullet_text}</div>'

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


# st.markdown(
#     """
#     <style>
#         @keyframes bounce {
#             0% { transform: translateY(0); }
#             5% { transform: translateY(-10px); }
#             25% { transform: translateY(0); }
#             45% { transform: translateY(-5px); }
#             65% { transform: translateY(0); }
#             100% { transform: translateY(0); }
#         }

#         .custom-button-container {
#             position: fixed;
#             bottom: 20px;
#             right: 20px;
#             z-index: 9999;
#             animation: bounce 1s;
#         }

#         .custom-button {
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             background-color:rgba(28, 131, 225, 0.1);
#             border: none;
#             cursor: pointer;
#             padding: 10px;
#             border-radius: 50%;
#             width: 80px;
#             height: 80px;
#             box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.25);
#             position: relative;
#             transition: transform 0.3s ease-in-out;
#         }

#         .custom-button:hover {
#             transform: scale(1.1);
#         }

#         .custom-button img {
#             width: 60px;
#             height: 60px;
#             object-fit: contain;
#         }

#         .custom-button span {
#             position: absolute;
#             top: 50%;
#             left: 50%;
#             transform: translate(-50%, -50%);
#             font-weight: bold;
#             font-size: 14px;
#             color: black;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.markdown(
#     """
#     <div class="custom-button-container">
#         <a href="/Chat">
#             <div class="custom-button">
#                 <img src="https://api.dicebear.com/5.x/bottts/svg?seed=88" alt="Custom Image">
#                 <span>Chat</span>
#             </div>
#         </a>
#     </div>
#     """,
#     unsafe_allow_html=True
# )








# def check_deployment():
#     # Check if the deployment is working
#     #\ 1. Check if the llm is working
#     try:
#         llm_helper = LLMHelper()
#         llm_helper.get_completion("Generate a joke!")
#         st.success("LLM is working!")
#     except Exception as e:
#         st.error(f"""LLM is not working.  
#             Please check you have a deployment name {llm_helper.deployment_name} in your Azure OpenAI resource {llm_helper.api_base}.  
#             If you are using an Instructions based deployment (text-davinci-003), please check you have an environment variable OPENAI_DEPLOYMENT_TYPE=Text or delete the environment variable OPENAI_DEPLOYMENT_TYPE.  
#             If you are using a Chat based deployment (gpt-35-turbo or gpt-4-32k or gpt-4), please check you have an environment variable OPENAI_DEPLOYMENT_TYPE=Chat.  
#             Then restart your application.
#             """)
#         st.error(traceback.format_exc())
#     #\ 2. Check if the embedding is working
#     try:
#         llm_helper = LLMHelper()
#         llm_helper.embeddings.embed_documents(texts=["This is a test"])
#         st.success("Embedding is working!")
#     except Exception as e:
#         st.error(f"""Embedding model is not working.  
#             Please check you have a deployment named "text-embedding-ada-002" for "text-embedding-ada-002" model in your Azure OpenAI resource {llm_helper.api_base}.  
#             Then restart your application.
#             """)
#         st.error(traceback.format_exc())
#     #\ 3. Check if the translation is working
#     try:
#         llm_helper = LLMHelper()
#         llm_helper.translator.translate("This is a test", "it")
#         st.success("Translation is working!")
#     except Exception as e:
#         st.error(f"""Translation model is not working.  
#             Please check your Azure Translator key in the App Settings.  
#             Then restart your application.  
#             """)
#         st.error(traceback.format_exc())
#     #\ 4. Check if the Redis is working with previous version of data
#     try:
#         llm_helper = LLMHelper()
#         if llm_helper.vector_store_type != "AzureSearch":
#             if llm_helper.vector_store.check_existing_index("embeddings-index"):
#                 st.warning("""Seems like you're using a Redis with an old data structure.  
#                 If you want to use the new data structure, you can start using the app and go to "Add Document" -> "Add documents in Batch" and click on "Convert all files and add embeddings" to reprocess your documents.  
#                 To remove this working, please delete the index "embeddings-index" from your Redis.  
#                 If you prefer to use the old data structure, please change your Web App container image to point to the docker image: fruocco/oai-embeddings:2023-03-27_25. 
#                 """)
#             else:
#                 st.success("Redis is working!")
#         else:
#             try:
#                 llm_helper.vector_store.index_exists()
#                 st.success("Azure Cognitive Search is working!")
#             except Exception as e:
#                 st.error("""Azure Cognitive Search is not working.  
#                     Please check your Azure Cognitive Search service name and service key in the App Settings.  
#                     Then restart your application.  
#                     """)
#                 st.error(traceback.format_exc())
#     except Exception as e:
#         st.error(f"""Redis is not working. 
#             Please check your Redis connection string in the App Settings.  
#             Then restart your application.
#             """)
#         st.error(traceback.format_exc())


# def check_variables_in_prompt():
#     # Check if "summaries" is present in the string custom_prompt
#     if "{summaries}" not in st.session_state.custom_prompt:
#         st.warning("""Your custom prompt doesn't contain the variable "{summaries}".  
#         This variable is used to add the content of the documents retrieved from the VectorStore to the prompt.  
#         Please add it to your custom prompt to use the app.  
#         Reverting to default prompt.
#         """)
#         st.session_state.custom_prompt = ""
#     if "{question}" not in st.session_state.custom_prompt:
#         st.warning("""Your custom prompt doesn't contain the variable "{question}".  
#         This variable is used to add the user's question to the prompt.  
#         Please add it to your custom prompt to use the app.  
#         Reverting to default prompt.  
#         """)
#         st.session_state.custom_prompt = ""
    

# @st.cache_data()
# def get_languages():
#     return llm_helper.translator.get_available_languages()

# try:

#     default_prompt = "" 
#     default_question = "" 
#     default_answer = ""

#     if 'question' not in st.session_state:
#         st.session_state['question'] = default_question
#     # if 'prompt' not in st.session_state:
#     #     st.session_state['prompt'] = os.getenv("QUESTION_PROMPT", "Please reply to the question using only the information present in the text above. If you can't find it, reply 'Not in the text'.\nQuestion: _QUESTION_\nAnswer:").replace(r'\n', '\n')
#     if 'response' not in st.session_state:
#         st.session_state['response'] = default_answer
#     if 'context' not in st.session_state:
#         st.session_state['context'] = ""
#     if 'custom_prompt' not in st.session_state:
#         st.session_state['custom_prompt'] = ""
#     if 'custom_temperature' not in st.session_state:
#         st.session_state['custom_temperature'] = float(os.getenv("OPENAI_TEMPERATURE", 0.7))

#     # Set page layout to wide screen and menu item
#     menu_items = {
# 	'Get help': None,
# 	'Report a bug': None,
# 	'About': '''
# 	 ## Embeddings App
# 	 Embedding testing application.
# 	'''
#     }
#     st.set_page_config(layout="wide", menu_items=menu_items)

#     llm_helper = LLMHelper(custom_prompt=st.session_state.custom_prompt, temperature=st.session_state.custom_temperature)

#     # Get available languages for translation
#     available_languages = get_languages()

#     # Custom prompt variables
#     custom_prompt_placeholder = """{summaries}  
#     Please reply to the question using only the text above.  
#     Question: {question}  
#     Answer:"""
#     custom_prompt_help = """You can configure a custom prompt by adding the variables {summaries} and {question} to the prompt.  
#     {summaries} will be replaced with the content of the documents retrieved from the VectorStore.  
#     {question} will be replaced with the user's question.
#         """

#     col1, col2, col3 = st.columns([1,2,1])
#     with col1:
#         st.image(os.path.join('images','dlytica.jpeg'))

#     col1, col2, col3 = st.columns([2,2,2])
#     with col1:
#         st.button("Check deployment", on_click=check_deployment)
#     with col3:
#         with st.expander("Settings"):
#             # model = st.selectbox(
#             #     "OpenAI GPT-3 Model",
#             #     [os.environ['OPENAI_ENGINE']]
#             # )
#             # st.tokens_response = st.slider("Tokens response length", 100, 500, 400)
#             st.slider("Temperature", min_value=0.0, max_value=1.0, step=0.1, key='custom_temperature')
#             st.text_area("Custom Prompt", key='custom_prompt', on_change=check_variables_in_prompt, placeholder= custom_prompt_placeholder,help=custom_prompt_help, height=150)
#             st.selectbox("Language", [None] + list(available_languages.keys()), key='translation_language')

#     question = st.text_input("OpenAI Semantic Answer", default_question)

#     if question != '':
#         st.session_state['question'] = question
#         st.session_state['question'], st.session_state['response'], st.session_state['context'], sources = llm_helper.get_semantic_answer_lang_chain(question, [])
#         st.markdown("Answer:" + st.session_state['response'])
#         st.markdown(f'\n\nSources: {sources}') 
#         with st.expander("Question and Answer Context"):
#             st.markdown(st.session_state['context'].replace('$', '\$'))
#             st.markdown(f"SOURCES: {sources}") 

#     if st.session_state['translation_language'] and st.session_state['translation_language'] != '':
#         st.write(f"Translation to other languages, 翻译成其他语言, النص باللغة العربية")
#         st.write(f"{llm_helper.translator.translate(st.session_state['response'], available_languages[st.session_state['translation_language']])}")		
		
# except Exception:
#     st.error(traceback.format_exc())
