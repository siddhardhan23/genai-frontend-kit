import streamlit as st
from utils.config import app_config  # loads env variables & get the app_config data
from services.test_server_health import test_health

# test health button & response
# llm options UI part alone for the frontend kit

