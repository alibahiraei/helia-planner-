import jdatetime


def to_jalali(gregorian_date):

    jalali = jdatetime.date.fromgregorian(
        date=gregorian_date
    )

    return jalali.strftime("%Y/%m/%d")