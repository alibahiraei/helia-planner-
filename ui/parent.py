from datetime import date

import streamlit as st

from services.task_service import TaskService
from utils.date_utils import to_jalali


def show_parent_panel():

    st.title("👨 پنل والدین")

    task_date = st.date_input(
        "📅 تاریخ",
        value=date.today()
    )

    st.caption(
        f"تاریخ شمسی: {to_jalali(task_date)}"
    )

    st.divider()

    with st.form("create_task"):

        title = st.text_input("عنوان کار")

        score = st.number_input(
            "امتیاز",
            min_value=1,
            max_value=100,
            value=10
        )
        start_date = st.date_input("از تاریخ")

        end_date = st.date_input("تا تاریخ")

        submitted = st.form_submit_button("ثبت ")
        
    if submitted:

        try:
            TaskService.create_tasks_between(
                title,
                score,
                start_date,
                end_date
            )

            st.success("برنامه ثبت شد.")
            st.rerun()

        except ValueError as e:
            st.error(str(e))

    if submitted:

        TaskService.create_task(
            title,
            score,
            task_date

        )

        st.success("کار جدید ثبت شد.")

        st.rerun()

    st.divider()

    st.subheader("📋 کارهای این روز")

    tasks = TaskService.get_tasks_by_date(task_date)

    for task in tasks:

        col1, col2, col3, col4 = st.columns([6, 1, 1, 1])

        with col1:
            st.write(task.title)

        with col2:
            st.write(f"⭐ {task.score}")

        with col3:
            st.button(
                "✏️",
                key=f"edit_{task.id}"
            )

        with col4:

            if st.button(
                "🗑️",
                key=f"delete_{task.id}"
            ):

                TaskService.delete_task(task.id)

                st.rerun()
    