import streamlit as st
from datetime import date

from services.task_service import TaskService


def show_home():

    st.title("🌸 برنامه روزانه هلیا")

    selected_date = st.date_input(
        "📅 تاریخ",
        value=date.today()
    )

    tasks = TaskService.get_tasks_by_date(selected_date)

    score = TaskService.get_total_score(selected_date)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "⭐ امتیاز امروز",
            score
        )

    with col2:
        st.metric(
            "📋 تعداد کارها",
            len(tasks)
        )

    st.divider()

    st.subheader("کارهای امروز")

    for task in tasks:

        col1, col2 = st.columns([6, 1])

        with col1:

            checked = st.checkbox(
                task.title,
                value=task.is_completed,
                key=f"task_{task.id}"
            )

            if checked != task.is_completed:

                TaskService.update_task_status(
                    task.id,
                    checked
                )

                st.rerun()

        with col2:

            st.write(f"⭐ {task.score}")

    st.divider()

    st.success("🌈 هر روز یک قدم بهتر از دیروز")