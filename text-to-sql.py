import streamlit as st
from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain



def generate_response(input_text,database_uri="postgres://default:GT4dg3OemzlA@ep-curly-violet-36509009.us-east-1.postgres.vercel-storage.com:5432/verceldb"):     
     db = SQLDatabase.from_uri(database_uri)
     llm = OpenAI(temperature=0, verbose=True, openai_api_key=openai_api_key)
     db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
     st.info(db_chain.run(input_text))




st.title('Run Sql queries on database using natural language via langchain & gpt3.5')
openai_api_key = st.sidebar.text_input('Please enter your OpenAI API Key')

with st.form('data_form'):
  question = st.text_area('Enter a question in natural language for the AI on the  omdb movies postgres database')
  database_uri = st.text_area("share a sqlachemy compatible uri for a remote db if you want to use another dataset, sample:postgres://default:GT4dg3OemzlA@ep-curly-violet-36509009.us-east-1.postgres.vercel-storage.com:5432/verceldb")
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(question,database_uri)