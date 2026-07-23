import jdatetime
from datetime import date

def to_jalali(g_date:date)->str :
    '''
    تبدیل تاریخ میلادی به شمسی
    '''

    j_date = jdatetime.date.fromgregorian(date=g_date)

    return j_date.strftime("%Y/%m/%d")

def get_weekday_name(g_date: date) -> str:
    """
    نام روز هفته به فارسی
    """

    weekdays = [

        "دوشنبه",

        "سه‌شنبه",

        "چهارشنبه",

        "پنجشنبه",

        "جمعه",

        "شنبه",

        "یکشنبه"

    ]

    return weekdays[g_date.weekday()]