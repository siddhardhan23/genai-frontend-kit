import streamlit as st
from utils.config import app_config  # loads env variables & get the app_config data
from utils.logger import logger
from services.test_server_health import test_health
from services.get_llms_list import get_llms

st.set_page_config(
    page_title="Test App",
    page_icon="🌐",
    layout="centered"
)

st.title("Boilerplate App for Generative AI Applications")

col1, col2 = st.columns(2)

if col1.button("Check Server Health"):
    logger.info("Button clicked: Check Server Health")
    result = test_health()
    logger.info(f"Health Check Result: {result}")
    st.json(result)

if col2.button("List LLMs"):
    logger.info("Button clicked: List LLMs")
    list_of_llms = get_llms()
    logger.info(f"LLMs Fetched: {list_of_llms}")
    st.json(list_of_llms)
