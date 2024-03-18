import streamlit as st
from msal_streamlit_authentication import msal_authentication

# def creds_entered():
    
    


def authenticate_user():
    if "authenticated" not in st.session_state or st.session_state["authenticated"] == False:
        # st.button("Login with Azure", on_click=creds_entered)
        st.subheader("Please login using Single Sign On")
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
            return True  
        else:
            st.session_state["authenticated"] = False
            st.error("Unable to login")
    else:     
        return False
    
    
    # else:
    #     if st.session_state["authenticated"]:
    #         return True
    #     else:
    #         st.button("Login with Azure", on_click=creds_entered)
    #         return False
    