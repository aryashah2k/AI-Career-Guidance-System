# Streamlit Template

This is a template for streamlit projects. You can modify it at will.

# Customize

Edit `/streamlit_app.py`, `/public/*.py` and  `/private/*.py` to customize this app.

# Online demo

To see an online demo, use this link:

[https://stbook-template.streamlitapp.com/](https://stbook-template.streamlitapp.com/)

## Local run

To locally run the app:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Authentication

Don't forget to add a `.streamlit/secrets.toml` with the desired credentials like this:

```
USER = "my_username"
PASSWORD = "my_password"
```

(Or edit the settings on share.streamlit.io, if deployed there.)

