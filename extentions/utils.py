import jdatetime
import requests
import json

def covert_to_jalali(gdate):
    month_list = ['فروردین', 'اردیبهشت',  'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان',  'آذر', 'دی', 'بهمن',  'اسفند']
    date = jdatetime.date.fromgregorian(year=gdate.year, month=gdate.month, day=gdate.day)
    return f"{date.day} {month_list[date.month-1]} {date.year}"

def send_sms(message, mobile):
    url = "https://api2.ippanel.com/api/v1/sms/send/webservice/single"
    print(mobile)
    payload = json.dumps(
        {
            "recipient": [
                mobile,
            ],
            "sender": "+983000505",
            "message": message
        }
    )
    headers = {
    'apikey': '8LyA7G0OVGgSTGosxdqaDHDYa1zD57s6Gl3OG6vOFpc=',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response)