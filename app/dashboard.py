import streamlit as st

from msal_streamlit_authentication import msal_authentication


value = msal_authentication(
    auth={
        "clientId": "95d75130-08e9-4d56-935f-1cc063a81177",
        "authority": "https://login.microsoftonline.com/64dc69e4-d083-49fc-9569-ebece1dd1408",
        "redirectUri": "/",
        "postLogoutRedirectUri": "/"
    },
    cache={
        "cacheLocation": "sessionStorage",
        "storeAuthStateInCookie": False
    },
    # login_request={
    #     "scopes": ["aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee/.default"]
    # },
    # key=1
    )
st.write("Received", value)
