import jdatetime

def covert_to_jalali(gdate):
    month_list = ['فروردین', 'اردیبهشت',  'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان',  'آذر', 'دی', 'بهمن',  'اسفند']
    date = jdatetime.date.fromgregorian(year=gdate.year, month=gdate.month, day=gdate.day)
    return f"{date.day} {month_list[date.month-1]} {date.year}"