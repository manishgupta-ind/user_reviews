from helper import *
import streamlit as st
import matplotlib.pyplot as plt
import time
import os
import seaborn as sns

sns.set_theme(style="darkgrid")
sns.set()
st.set_page_config(page_title='User Reviews Analysis', page_icon='🖖')

st.title('Detect Anomalies in User Reviews')

# User Authentication
def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():

    # Main app starts here
    uploaded_file = st.file_uploader('Upload csv file containing data')
    if uploaded_file is not None:

        # read csv
        df=pd.read_csv(uploaded_file)

        # get proccessed data by  model
        df_filtered = predictor(df)
        
        csv = df_filtered.to_csv(index=False).encode()

        st.download_button(
        "Press to Download",
        csv,
        "Reviews_filtered.csv",
        "text/csv",
        key='download-csv'
        )