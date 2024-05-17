import streamlit as st
from msal_streamlit_authentication import msal_authentication

   
def authenticate_user():
    authority_template = "https://{tenant}.b2clogin.com/{tenant}.onmicrosoft.com/{user_flow}"
    b2c_tenant = "axioenergy"
    signupsignin_user_flow = "B2C_1_signup_signin"
    AUTHORITY = authority_template.format(
    tenant=b2c_tenant, user_flow=signupsignin_user_flow)
    print(AUTHORITY)

    client_id = "5abc2de9-a633-47b8-9f47-b098fe850784"
    redirect_uri = "http://localhost:8051"
    b2c_policy = "B2C_1_singnup-signin"
    scopes = ["openid"]

    # https://axioenergy.b2clogin.com/axioenergy.onmicrosoft.com/b2c_1_signup_signin/oauth2/v2.0/authorize?client_id=5abc2de9-a633-47b8-9f47-b098fe850784&scope=email%20openid%20profile%20offline_access&redirect_uri=http%3A%2F%2Flocalhost%3A8501&client-request-id=a419b694-5385-4757-bd58-2ee1192607ef&response_mode=fragment&response_type=code&x-client-SKU=msal.js.browser&x-client-VER=2.36.0&client_info=1&code_challenge=EgVO3e0Fgva2xL0m8EPubf10fLR5hzNdyzjVemjE1LA&code_challenge_method=S256&nonce=d922c3ad-b281-41e7-85f4-2d8afcb652c7&state=eyJpZCI6ImEyNzU5YmVmLWM3ZmUtNGQ2OC04YjU3LWJhYjZiOGM0NzAyZiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicG9wdXAifX0%3D

    # https://axioenergy.b2clogin.com/axioenergy.onmicrosoft.com/b2c_1_signup_signin/oauth2/v2.0/authorize?client_id=5abc2de9-a633-47b8-9f47-b098fe850784&scope=email%20openid%20profile%20offline_access&redirect_uri=http%3A%2F%2Flocalhost%3A8501&client-request-id=8f65b9de-ee4b-4420-ae87-f78b6d1353aa&response_mode=fragment&response_type=code&x-client-SKU=msal.js.browser&x-client-VER=2.36.0&client_info=1&code_challenge=T_3YyOgpPSFBjU5a77wuYrvXgcy5LEqFMiL-911nc24&code_challenge_method=S256&nonce=10c10287-a2e3-45b8-8273-d09e781be287&state=eyJpZCI6IjhlNWZiZGM0LTc3OWEtNGRkZS1iYTdlLWViYzM1OTA0OTRlZCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicG9wdXAifX0%3D
    
    # https://axioenergy.b2clogin.com/axioenergy.onmicrosoft.com/oauth2/v2.0/authorize?p=B2C_1_signup_signin&client_id=5abc2de9-a633-47b8-9f47-b098fe850784&nonce=defaultNonce&redirect_uri=http%3A%2F%2Flocalhost%3A8051%2F&scope=openid&response_type=code&prompt=login


    login_token = msal_authentication(
            auth={
                "authority": "https://axioenergy.b2clogin.com/axioenergy.onmicrosoft.com/B2C_1_signup_signin",
                "clientId": "485be2c3-e1a1-40a1-bd9a-c44a1e1c59e0",
                "knownAuthorities": ["https://axioenergy.b2clogin.com/axioenergy.onmicrosoft.com"],
                "redirectUri": "http://localhost:5173",
            },
            cache={
                'cacheLocation': 'sessionStorage',
                'storeAuthStateInCookie': False
            },
            key=1
    )

    # http://localhost:5173/#state=   


    st.write("Recevied login token:", login_token)

    # login_token = msal_authentication(
    #     auth={
    #         "client_id": "5abc2de9-a633-47b8-9f47-b098fe850784",
    #         "authority": "https://axioenergy.b2clogin.com/axioenergy.onmicrosoft.com/oauth2/v2.0/authorize?p=B2C_1_singnup-signin",
    #         "redirectUri": "http://localhost:8501/",
    #         "postLogoutRedirectUri": "http://localhost:8501/",
    #         "knownAuthorities": ["https://axioenergy.b2clogin.com/axioenergy.onmicrosoft.com"],  # Add your tenant-specific authority URL here
    #     }, # Corresponds to the 'auth' configuration for an MSAL Instance
    #     cache={
    #         "cacheLocation": "sessionStorage",
    #         "storeAuthStateInCookie": False
    #     }, # Corresponds to the 'cache' configuration for an MSAL Instance
    #     login_request={
    #         "scopes": ["5abc2de9-a633-47b8-9f47-b098fe850784/.default"]
    #     }, # Optional
    #     logout_request={}, # Optional
    #     login_button_text="Login", # Optional, defaults to "Login"
    #     logout_button_text="Logout", # Optional, defaults to "Logout"
    #     class_name="css_button_class_selector", # Optional, defaults to None. Corresponds to HTML class.
    #     html_id="html_id_for_button", # Optional, defaults to None. Corresponds to HTML id.
    #     key=1 # Optional if only a single instance is needed
    # )
    # st.write("Recevied login token:", login_token)


    # # https://axioenergy.b2clogin.com/axioenergy.onmicrosoft.com/oauth2/v2.0/authorize?p=B2C_1_singnup-signin&client_id=5abc2de9-a633-47b8-9f47-b098fe850784&nonce=defaultNonce&redirect_uri=http%3A%2F%2Flocalhost%3A8051&scope=openid&response_type=code&prompt=login


    # # Define your Azure B2C configuration
    # config = {
    #     "clientId": "5abc2de9-a633-47b8-9f47-b098fe850784",
    #     "authority": "https://axioenergy.b2clogin.com/axioenergy.onmicrosoft.com/B2C_1_singnup-signin",
    #     "knownAuthorities": ["https://axioenergy.b2clogin.com/axioenergy.onmicrosoft.com"],  # Add your tenant-specific authority URL here
    # }


    # # Define your cache configuration
    # cache_config = {
    #     "cacheLocation": "sessionStorage",
    #     "storeAuthStateInCookie": False
    # }

    # # Define the login request
    # login_request = {
    #     "scopes": ["openid"]
    # }

    # # Initialize OIDC authentication
    # login_token = msal_authentication(
    #     auth=config,
    #     cache=cache_config,
    #     login_request=login_request,
    #     logout_request={},
    #     login_button_text="Login",
    #     logout_button_text="Logout",
    # )

    # # Display the received login token
    # st.write("Received login token:", login_token)




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