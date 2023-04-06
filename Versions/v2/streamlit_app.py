import streamlit as st
import streamlit_book as stb

# Set wide display
st.set_page_config(layout="wide")

# Check if view is admin
if "admin_view" in st.session_state:
    admin_view = st.session_state["admin_view"]
else:
    admin_view = False

# Check if query param
query_params = st.experimental_get_query_params()
if "view" in query_params:
    if query_params["view"][0] == "admin":
        stb.render_file("public/login.py")
else:
    # Set private and public views
    if admin_view:
        stb.set_book_config(
                menu_title="Admin",
                menu_icon="public",
                options=[
                    "My Home",   
                    "Career Recommender", 
                    "Logout", 
                    ], 
                paths=[
                    "private/home.py", 
                    "private/my_private_page.py", 
                    "private/logout.py", 
                    ],
                save_answers=False,
                styles={
                    "nav-link": {"--hover-color": "#fde8ec"},
                    "nav-link-selected": {"background-color": "#DC143C"},
                }
                )
    else:
        stb.set_book_config(
                menu_title="Public View",
                menu_icon="private",
                options=[
                    "Home",   
                    "Explore Careers", 
                    "Login", 
                    ], 
                paths=[
                    "public/home.py", 
                    "public/my_public_page.py", 
                    "public/login.py", 
                    ],
                save_answers=False,
                styles={
                    "nav-link": {"--hover-color": "#e9f6fb"},
                    "nav-link-selected": {"background-color": "#87CEEB"},
                }
                )        

# Add floating button
stb.floating_button("https://forms.gle/r1VMgAVoYHVUSpH38", "chat-left-dots-fill", "white", "blue")