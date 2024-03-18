import streamlit as st
import pandas as pd
import datetime as date
from msal_streamlit_authentication import msal_authentication


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
st.write("Received", value)

st.title("Hello :red[streamlit] :100: :the_horns:")

st.header("Header :anchor:")
st.subheader("Sub Header :taurus:")
st.text("This is a trial of text")
st.latex(
    r"""
    a + ar + a r^2 + a r^3 """,
    help="This is latex function to display mathematical functions")

st.markdown(""" ### h3 tag :moon: :sunglasses: :cool: """)

df = pd.DataFrame.from_dict(
    {
        "name": ["Yoda", "John Wick", "Pikachu"],
        "country": ["Star", "USA", "Japan"],
        "dob": [
            date.today().strftime("%B %d, %Y"),
            date(2002, 5, 5),
            date(1992, 12, 12),
        ],
    }
)

st.write(df)
