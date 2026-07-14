import streamlit as st

from database.database import Base, engine
from database.models import Task

from ui.home import show_home
from ui.parent import show_parent_panel

from database.init_db import init_database

def load_css():

    with open("assets/style.css", encoding="utf-8") as f:

        st.markdown(

            f"<style>{f.read()}</style>",

            unsafe_allow_html=True
        )


load_css()




init_database()

st.set_page_config(

    page_title="Helia Planner",

    page_icon="🌸",

    layout="centered"
)

page = st.sidebar.selectbox(
    "انتخاب صفحه",
    [
        "👧 هلیا",
        "👨 والدین"
    ]
)

if page == "👧 هلیا":
    show_home()
else:
    show_parent_panel()