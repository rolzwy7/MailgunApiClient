from mgapi.mgapi import Api as MailgunApi

api = MailgunApi(config_file="C:\\Users\\Account\Desktop\\config.json")

des, ser = api.get_tag_aggregates("DevTest", "devices")

print(ser)
