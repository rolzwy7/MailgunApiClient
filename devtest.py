# from mgapi.mgapi import Api as MailgunApi
#
#
#
# def getReportData(tag):
#     api = MailgunApi(config_file="C:\\Users\\Account\Desktop\\config.json")
#     des, ser = api.get_tags(tag=tag)
#     print(ser)
#
#
# ISO8601()
#
#
from email import utils
import datetime
import time

def toRFC2822(_datetime, days=0, hours=0, minutes=0, return_timestamp=False):
    timedelta_shift = datetime.timedelta(days=days, hours=hours, minutes=minutes)
    now_datetime = _datetime + timedelta_shift
    now_timestamp = time.mktime(now_datetime.timetuple())
    # localtime=True (Sets local timezone)
    result = utils.formatdate(now_timestamp, localtime=True)
    # self.print_debug("timedelta_shift:", timedelta_shift)
    # self.print_debug("now_datetime:", now_datetime)
    # self.print_debug("now_timestamp:", now_timestamp)
    # self.print_debug("result:", result)
    if return_timestamp:
        return result, now_timestamp
    return result

def ISO8601(iso8601_string):
    # Date
    try:
        date_part = iso8601_string.split("T")[0]
        year, month, day = date_part.split("-")
        year, month, day = int(year), int(month), int(day)
    except Exception as e:
        print("Exception:", e)
        return False
    # Time
    try:
        time_part = iso8601_string.split("T")[1].strip("Z")
        time_part = time_part.split(".")[0] if "." in time_part else time_part
        hour, minute, second = time_part.split(":")
        hour, minute, second = int(hour), int(minute), int(second)
    except Exception as e:
        print("Exception:", e)
        hour, minute, second = 0, 0, 0
    result = datetime.datetime(
        year=year     , month=month   , day=day,
        hour=hour     , minute=minute , second=second,
        microsecond=0 , tzinfo=None
    )
    return result

print(toRFC2822(ISO8601("2018-08-02T14:16:47.688Z")))


# result = datetime.datetime(
#     year=2018,
#     month=3,
#     day=19,
#     hour=0,
#     minute=0,
#     second=0,
#     microsecond=0,
#     tzinfo=None
# )
#
# print(result)

# getReportData(tag="MyTag")
