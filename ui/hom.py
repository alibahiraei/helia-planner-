import streamlit as st
from database.models import Task
from services.task_service import TaskService


def show_home(tasks: list[Task]):

    st.set_page_config(
        page_title="Helia Planner",
        page_icon="🌸",
        layout="centered"
    )

    st.title("🌸 برنامه روزانه هلیا")

    st.divider()
    #=====================================


    with st.form("new_task"):

        title = st.text_input("عنوان کار")

        score = st.number_input(
            "امتیاز",
            min_value=1,
            max_value=100,
            value=10
        )

        submitted = st.form_submit_button("➕ افزودن")

    if submitted:
        TaskService.create_task(title, score)
        st.success("کار جدید اضافه شد.")
        st.rerun()

    col1, col2 = st.columns(2)

    with col1:
        score = TaskService.get_total_score()
        st.metric(
           label="امتیاز امروز",
            value=f"{score} ⭐"
        )

    with col2:
        st.metric(
            label="کارهای امروز",
            value=len(tasks)
        )



    st.divider()
    
    st.subheader("📋 لیست کارها")

    for task in tasks:

        col1, col2, col3 = st.columns([6, 1, 1])

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

        with col3:
            if st.button("🗑️", key=f"delete_{task.id}"):
                TaskService.delete_task(task.id)
                st.rerun()

  
    st.divider()

    st.info("🌈 هر روز یک قدم بهتر از دیروز")