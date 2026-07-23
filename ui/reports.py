import streamlit as st

from services.report_service import ReportService
from datetime import date
from utils.date_utils import (
    to_jalali,
    get_weekday_name
)


def show_reports():

    st.title("📊 گزارش عملکرد")

    


    col1, col2 = st.columns(2)

    with col1:

        start_date = st.date_input(

            "از تاریخ",

            value=date.today()

        )

    with col2:

        end_date = st.date_input(

            "تا تاریخ",

            value=date.today()

        )
        
    st.caption(
    f"از {to_jalali(start_date)} تا {to_jalali(end_date)}"
    )

    tasks = ReportService.get_tasks_between(

            start_date,

            end_date

        )
    score = ReportService.get_total_score(tasks)

    possible_score = ReportService.get_possible_score(tasks)

    completed = ReportService.get_completed_count(tasks)

    progress = 0

    if possible_score:

        progress = score / possible_score

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(

            "⭐ امتیاز",

            f"{score} / {possible_score}"

    )

    with c2:

        st.metric(

            "✅ انجام شده",

            completed

        )

    with c3:

        st.metric(

            "📋 کل کارها",

            len(tasks)

        )
    st.progress(progress)

    completed_tasks = ReportService.get_completed_tasks(tasks)
    remaining_tasks = ReportService.get_remaining_tasks(tasks)


    st.subheader("✅ انجام شده")

    for task in completed_tasks:

        st.success(
            f"""✅ {task.title}

    📅 {get_weekday_name(task.task_date)}

    🗓 {to_jalali(task.task_date)}

    ⭐ {task.score}
    """
        )

    st.subheader("⏳ انجام نشده")

    for task in remaining_tasks:

        st.error(
            f"""❌ {task.title}

    📅 {get_weekday_name(task.task_date)}

    🗓 {to_jalali(task.task_date)}

    ⭐ {task.score}
    """
        )

    if not remaining_tasks and tasks:

        st.balloons()

        st.success("🎉 تمام کارهای این بازه انجام شده‌اند.")

