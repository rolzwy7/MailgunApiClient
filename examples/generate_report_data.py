"""
    This example shows how to fetch data from mailgun api to generate json file with
    analytics data for single tag.
"""

import pprint as pp
try:
    from mgapi.mgapi import Api as MailgunApi
except:
    print("Can't find mgapi module. ")
    exit(0)


def getReportData(tag):
    """
        Generate mailing report data by single tag
    """
    # Connect to API
    api = MailgunApi(config_file="C:\\Users\\Account\Desktop\\config.json")
    # Return
    ret = {
        "tag_info": {},
        "tag_stats": {},
        "aggregates": {},
        "tag_events": {}
    }
    # validate, check tag
    des, ser = api.get_tags(tag=tag)
    if not des["justify"]["success"]:
        print(des["justify"]["reason"])
        return False
    ret["tag_info"] = des

    # Get aggregates
    for aggregate in api._AGGREGATES:
        des, ser = api.get_tag_aggregates(tag=tag, aggregate=aggregate)
        ret["aggregates"][aggregate] = des

    # Get tag stats
    for event in api._EVENTS:
        des, ser = api.get_tag_stats(tag, event, start=api.nowRFC2822(days=-30))
        ret["tag_stats"][event] = des

    # Get tag events
    filter_fields = api.ret_events_filter_fields()
    filter_fields["tags"] = [tag]
    for event in api._EVENTS:
        tmp_array = []
        filter_fields["event"] = event
        # Get events for tag
        des, ser = api.get_events(
            begin=api.nowRFC2822(days= -30),
            # we can set end parameter a little bit in the future
            # just in case
            end=api.nowRFC2822(minutes= 30),
            filter_fields=filter_fields,
            limit=290
        )
        tmp_array += des["items"]
        exhausted = False
        while not exhausted:
            exhausted, des, ser = api.follow_pagination(Next=des["paging"]["next"])
            tmp_array += des["items"]
        ret["tag_events"][event] = tmp_array

    ret_json = api.serialize_json(ret)
    return ret, ret_json

## Change tag to your tag
des, ser = getReportData(tag="MyTag")
print(ser)

with open("report_test.json", "wb") as source:
    source.write(ser.encode("utf8"))
    source.close()
