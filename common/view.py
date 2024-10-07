from common.model import Views
from streamlit import session_state as ss
import streamlit as st
from loguru import logger


class View:
    """
    Primary responsibility to handle streamlit rendering and pass interactions to the controller from the user. Utilizes the models to help render outputs like the quiz. 
    
    Functions as exposing API to the controller to render and handle user interactions.
    """
    def __init__(self):
        """
        The self.pc is a multi-element container holding two elements: A title and the canvas. We utilize an empty container (a streamlit single element container) to 'clear' the container and can update the canvas with new content. When calling changes to the primary container, use the update canvas method to pass a single parent element to the canvas and optionally update the title.
        """
        if 'current_page' not in ss: ss.current_page = Views.OVERVIEW
        if 'client_id' not in ss: ss.client_id = '12345'
        self.canvas = st.container(border=True)
        self.canvas.empty()
    
    
    def render(self, controller):
        view_methods = {
            Views.OVERVIEW: self.render_overview_view
        }
        view_method = view_methods.get(ss.current_page)
        if view_method:
            logger.debug(f"Rendering view: {ss.current_page}")
            view_method(controller)
        else:
            raise ValueError(f"Unknown view type: {ss.current_page}")
    
    
    def render_overview_view(self, controller):
        container = self.canvas.empty().container()
        
        if ss.current_page == Views.OVERVIEW:
            container.title('Overview Page')
            
            # Pull from Supabase, create a list of all of the clients as a Dataframe
            df = controller.pull_clients_overview()
            container.table(df)
            # On button click, switch the ss.client and ss.current_page to pass onto ingress / detail
            view_ingress = container.button("View Ingress")
            if view_ingress:
                self.
            # On client click, switch the ss.client and ss.current_page to pass onto detailed
    
    
    def render_ingress_view(self, controller):
        container = self.canvas.empty()
        
        form = container.form(key="ingress_form")
        
        if ss.current_page == Views.INGRESS:
            container.title('Ingress Page')
            
            yt_url = form.text_input("YouTube URL")
            
            submit = form.form_submit_button("Submit")
            
            if submit:
                controller.analyze_video(yt_url)
    
    
    # Callback Functions
    def on_switch_to_ingress(self, controller):
        controller.set_page(Views.INGRESS)
        controller.set_client_id(ss.client_id)