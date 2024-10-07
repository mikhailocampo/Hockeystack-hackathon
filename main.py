import os
import streamlit as st
from streamlit import session_state as ss
from common import Controller, View, Views
from common.utils import init_supabase_client
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

st.set_page_config(page_title="Hockeystack - Churn Controller", layout="wide")

# Init SS
if 'current_page' not in ss:
    ss.current_page = Views.OVERVIEW
if 'supabase_client' not in ss:
    ss.supabase_client = init_supabase_client()


# Init Controller with Current Quiz
controller = Controller()
view = View()


# Run Main app logic
view.render(controller)
st.write(ss)