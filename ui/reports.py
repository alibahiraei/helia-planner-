import streamlit as st

from services.report_service import ReportService


def show_reports():

    st.title("📊 گزارش عملکرد")

    score = ReportService.get_today_score()

    total = ReportService.get_today_total()

    completed = ReportService.get_today_completed()

    progress = 0

    if total:

        progress = completed / total

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(

            "⭐ امتیاز",

            score

        )

    with c2:

        st.metric(

            "✅ انجام شده",

            completed

        )

    with c3:

        st.metric(

            "📋 کل کارها",

            total

        )

    st.divider()

    st.progress(progress)

    st.caption(

        f"{completed} از {total} کار انجام شده است."
    )