import streamlit as st
import streamlit_book as stb
import numpy as np
import pandas as pd

st.title("My Public Page")

st.markdown("This is where you put your **private** content.")

st.subheader("Maybe cat pictures")
st.image("https://cataas.com/cat/cute")


st.subheader("Maybe some data")
st.markdown("Some data that you want to share with your collaborators but needs to remain private.")
N = 5
df = pd.DataFrame(100*np.random.randn(5, N), columns=('col%d' % i for i in range(N)))
st.dataframe(df)  # Same as st.write(df)
