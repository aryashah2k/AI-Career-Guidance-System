import streamlit as st

# Auxiliary functions for autentication
def on_click():
    import time
    if st.session_state["correct_password"]:
        st.session_state["admin_view"] = True
        time.sleep(.25)
        query_dict = {}
        st.experimental_set_query_params(**query_dict)        
    else:
        st.warning("Wrong username or password")

st.title("Login")
c1, c2, c3 = st.columns([2,2,1])
user = c1.text_input("Username:", "")
pswd = c2.text_input("Password:", "", type="password")

try:
    USER = st.secrets["USER"]
    PASSWORD = st.secrets["PASSWORD"]
    if user==USER and pswd==PASSWORD:
        st.session_state["correct_password"] = True
    else:
        st.session_state["correct_password"] = False
    c3.markdown("")
    c3.markdown("")
    c3.button("Check", on_click=on_click)
except Exception as e:
    st.exception(e)
    mkd = """Please set the user and password. Add 2 lines like this to your secrets.toml file (with a stronger configuration):\n
USER = "admin"\n
PASSWORD = "1234"
"""
    st.error(mkd)

st.markdown("---")
st.markdown("This is an optional page. You can remove this page from streamlit_app.py, and the app will still work.")
st.markdown("You can also access this page by appending '?view=admin' to the [URL](https://stbook-template.streamlitapp.com/?view=admin)")

st.markdown("Use the following EXTREMELY WEAK credentials to login: **admin** / **4321**")
st.markdown("""You should set up variables USER and PASSWORD on .streamlit/secrets.toml 
and/or the app properties (as suggested on 
[streamlit's secrets](https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)
)""")
