import streamlit as st
from datetime import date

from services.task_service import TaskService
from utils.date_utils import to_jalali
from datetime import date, timedelta
from utils.date_utils import (
    to_jalali,
    get_weekday_name
)



def motivational_message(progress):

    if progress == 1:

        return "🏆 فوق‌العاده بود هلیا!"

    if progress >= .7:

        return "🌸 فقط کمی دیگر مانده."

    if progress >= .4:

        return "💪 داری عالی پیش میری."

    return "🚀 شروع کن، تو می‌توانی."


def show_home():
    

    if "selected_date" not in st.session_state:
        st.session_state.selected_date = date.today()

    st.markdown(
        """
    # 🌸 Helia Planner

        ### سلام هلیا 🌷
    """)
    
    today = date.today()

    

    st.info(
    "🎯 تنها راه موفقیت تعین هدف است"
    )
    col1, col2, col3 = st.columns([1, 4, 1])

    with col1:
        if st.button("⬅️"):
            st.session_state.selected_date -= timedelta(days=1)
            st.rerun()

    with col2:
        st.markdown(
            f"### 📅 {to_jalali(st.session_state.selected_date)}"
        )
        st.caption(
            get_weekday_name(st.session_state.selected_date)
        )

    with col3:
        if st.button("➡️"):
            st.session_state.selected_date += timedelta(days=1)
            st.rerun()
    selected_date = st.session_state.selected_date


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

            "📋 کارها",

            len(tasks)

        )

    st.divider()

    st.subheader("کارهای امروز")

    completed = sum(

    task.is_completed

    for task in tasks

    )

    progress = 0

    st.caption(

    f"{completed} از {len(tasks)} کار انجام شده است."

    )

    if tasks:

        progress = completed / len(tasks)

    st.progress(progress)

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

   



    st.success(

        motivational_message(progress)

        )
    st.caption(
    "ساخته شده با ❤️ توسط بابا"
    )