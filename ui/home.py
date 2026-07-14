import streamlit as st
from datetime import date

from services.task_service import TaskService
from utils.date_utils import to_jalali



def motivational_message(progress):

    if progress == 1:

        return "🏆 فوق‌العاده بود هلیا!"

    if progress >= .7:

        return "🌸 فقط کمی دیگر مانده."

    if progress >= .4:

        return "💪 داری عالی پیش میری."

    return "🚀 شروع کن، تو می‌توانی."


def show_home():

    st.markdown(
        """
    # 🌸 Helia Planner

        ### سلام هلیا 🌷
    """)
    
    today = date.today()

    st.caption(
        f"📅 {to_jalali(today)}"
    )

    st.info(
    "🎯 امروز هم با انرژی شروع کنیم."
    )

    tasks = TaskService.get_tasks_by_date(today)

    score = TaskService.get_total_score(today)

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