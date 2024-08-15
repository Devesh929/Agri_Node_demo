import streamlit as st

# Enhanced CSS to hide the toolbar and other components
hide_streamlit_style = """
    <style>
    /* Hide the top menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Hide the toolbar with test id 'stToolbar' */
    div[data-testid="stToolbar"] {visibility: hidden;}
    </style>
    """

# Inject the CSS into the app
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Display a warning message
st.warning("To run this app, please enable blockchain wallet transactions in your browser as you are running this on an organization's network.")
