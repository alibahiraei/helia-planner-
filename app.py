import streamlit as st

from database.database import Base, engine
from database.models import Task

from ui.home import show_home
from ui.parent import show_parent_panel

from database.init_db import init_database

init_database()



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