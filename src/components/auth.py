import streamlit as st
from msal_streamlit_authentication import msal_authentication

def creds_entered():
    if st.session_state["user"].strip() == "admin" and st.session_state["passwd"].strip() == "admin":
        st.session_state["authenticated"] = True
        logger.info("admin successfully logged in.")
    else:
        st.session_state["authenticated"] = False
        if not st.session_state["passwd"]:
            st.warning("Please enter password")
        elif not st.session_state["user"]:
            st.warning["Please enter username"]
        else:
            st.error("Invalid Username/Pass :face_with_raised_eyebrow: :man-shrugging: :yawning_face:")


def authenticate_user():
    if "authenticated" not in st.session_state:
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
            # login_request={
            #     "scopes": ["aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee/.default"]
            # },
            # key=1
            )
        if value is not None:
            st.session_state["authenticated"] = True    
            st.write("Received", value)
            return True
        else:
            st.error("Invalid Username/Pass :face_with_raised_eyebrow: :man-shrugging: :yawning_face:")
            return False