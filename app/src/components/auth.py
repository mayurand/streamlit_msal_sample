import streamlit as st
from msal_streamlit_authentication import msal_authentication
from loguru import logger

   
def authenticate_user():
    with st.sidebar:
        value = msal_authentication(
        auth={
            "clientId": "95d...",
            "authority": "https://login.microsoftonline.com/64dc...",
            # "redirectUri": "https://streamlit-auth-package-streamlit.apps.cluster-srkhk.dynamic.redhatworkshops.io",
            "redirectUri": "http://localhost:8501",
            "postLogoutRedirectUri": "/"
        },
        cache={
            "cacheLocation": "sessionStorage",
            "storeAuthStateInCookie": False
        },
        )
        if value is not None:
            # TODO: Check what value is if a user signs in, and they are not authorized
            st.session_state["authenticated"] = True



def authorize_user():
    if "authenticated" in st.session_state:
        if st.session_state["authenticated"] == True:
            return True
        else:
            st.subheader("Please login using Single Sign On")
            return False
    else:
        st.subheader("Please login using Single Sign On")
        return False