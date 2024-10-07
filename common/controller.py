import streamlit as st
from streamlit import session_state as ss
from common.model import Views
from common.genai import Provider, LLM, init_transcript_analysis_chain
from common.utils import get_all_data_as_dataframe
import time


class Controller:
    """
    Handles the logic of the quiz and completes 3 main methods: 
    1. Generate request input
    2. Process response
    3. Handle user interactions with quiz
    
    Has utility functions to help accomplish logic by calling the view with parameters
    """
    def __init__(self):
        pass
    
    def set_page(self, page):
        # interface to interact with session state variables
        ss.current_page = page
    
    def set_client_id(self, client_id):
        # interface to interact with session state variables
        ss.client_id = client_id
    
    def analyze_video(self, yt_url):
        chain = init_transcript_analysis_chain()
        analysis = chain.invoke(yt_url)
        # Write to Supabase
        # Swap to view
        ss.current_page = self.view
        ss.client_id = '12345'


    def pull_clients_overview(self):
        # Pull from supabase
        df = get_all_data_as_dataframe(ss.supabase_client)
        return df