import streamlit as st
from msal_streamlit_authentication import msal_authentication

def creds_entered():
    value = msal_authentication(
    auth={
        "clientId": "95d75130-08e9-4d56-935f-1cc063a81177",
        "authority": "https://login.microsoftonline.com/64dc69e4-d083-49fc-9569-ebece1dd1408",
        "redirectUri": "https://streamlit-auth-package-streamlit.apps.cluster-srkhk.dynamic.redhatworkshops.io",
        "postLogoutRedirectUri": "/"
    },
    cache={
        "cacheLocation": "sessionStorage",
        "storeAuthStateInCookie": False
    },
    )
    if value is not None:
        st.session_state["authenticated"] = True    
        st.write("Received", value)
    else:
        st.error("Invalid Username/Pass :face_with_raised_eyebrow: :man-shrugging: :yawning_face:")


def authenticate_user():
    if "authenticated" not in st.session_state:
        st.button("Login with Azure", on_click=creds_entered)
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.button("Login with Azure", on_click=creds_entered)
            return False
    