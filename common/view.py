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
            Views.OVERVIEW: self.render_overview_view,
            Views.INGRESS: self.render_ingress_view,
            Views.DETAILED: self.render_detailed_view
        }
        view_method = view_methods.get(ss.current_page)
        if view_method:
            logger.debug(f"Rendering view: {ss.current_page}")
            view_method(controller)
        else:
            raise ValueError(f"Unknown view type: {ss.current_page}")
    
    
    def render_overview_view(self, controller):
        container = self.canvas.empty()
        
        if ss.current_page == Views.OVERVIEW:
            
            # Pull from Supabase, create a list of all of the clients as a Dataframe
            df = controller.pull_clients_overview()

            # Create a button for each client
            for index, row in df.iterrows():
                col1, col2, col3, col4 = container.columns([1, 1, 1, 1])
                col1.write(row['client_name']) 
                col2.write(row['health_float'])
                view_details = col3.button("View Details")
                add_analysis = col4.button("Add New Analysis")
            
            
            if view_details:
                container.empty()
                self.on_client_selected(controller, row['client_id'])
            
            if add_analysis:
                container.empty()
                self.on_switch_to_ingress(controller, row['client_id'])
    
    def render_ingress_view(self, controller):
        container = self.canvas.empty()
        
        form = container.form(key="ingress_form")
        
        if ss.current_page == Views.INGRESS:
            container.title('Ingress Page')
            
            yt_url = form.text_input("YouTube URL")
            
            submit = form.form_submit_button("Submit")
            
            if submit:
                controller.analyze_video(yt_url)
    
    
    def render_detailed_view(self, controller):
        container = self.canvas.empty()
        container.title('Detailed View')
    
    
    
    # Callback Functions
    def on_client_selected(self, controller, client_id):
        ss.client_id = client_id
        ss.current_page = Views.DETAILED
        self.render(controller)

    def on_switch_to_ingress(self, controller, client_id):
        self.canvas.empty()
        ss.client_id = client_id
        ss.current_page = Views.INGRESS
        self.render(controller)