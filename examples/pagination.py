# pagination example

try:
    from mgapi.mgapi import Api as MailgunApi
except:
    print("Can't find mgapi module. ")
    exit(0)

api = MailgunApi(config_file="C:\\Users\\Account\Desktop\\config.json")

# first request
all_events = []
des, ser = api.get_events(
    begin=api.nowRFC2822(days= -10),
    end=api.nowRFC2822(minutes= +15)
    )
all_events += des["items"]

# follow request pagination 'next' link
exhausted = False
while not exhausted:
    exhausted, des, ser = api.follow_pagination(Next=des["paging"]["next"])
    all_events += des["items"]

print("Number of events from last 10 days:", len(all_events))

# correct way of even polling is described here:
# https://documentation.mailgun.com/en/latest/api-events.html#event-polling
