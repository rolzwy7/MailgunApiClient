# Mailgun API Client
---
[Mailgun][mailgunhome] API client supporting sending and most GET endpoints for custom reporting.
## Usage
---
#### 1.) Creating object ( configuration )
There are three ways of creating Api object
```python
from mgapi.mgapi import Api as MailgunApi

# With json config file (see config_example.json)
api = MailgunApi(
    config_file="C:\\Users\\Account\\Desktop\\config.json",
    debug=False
)

# Through parameters
api = MailgunApi(
    base_url="https://api.mailgun.net/v3",
    domain="<your_domain>",
    api_user="api",
    private_key="<your_private_key>"
)

# With configuration inherited from 'MGApiConfiguration' class in mgapi.py
# See 'MGApiConfiguration' class constructor
api = MailgunApi()
```
#### 2.) Making request ( example )
```python
from mgapi.mgapi import Api as MailgunApi
api = MailgunApi(config_file="C:\\Users\\Account\\Desktop\\config.json")

### Get stats for all event types
for event in api._EVENTS:
    print("-"*15, event.upper(), "-"*15)
    deserialized, serialized = api.get_stats_total(event=event)
    print(serialized)

### Send email 8 hours from now
# Set additional sending options
sending_options = api.ret_additional_sending_options()
sending_options["o:tag"] = ["MyTag"]
sending_options["o:deliverytime"] = api.nowRFC2822(hours=8)
# Send email
deserialized, serialized = api.send_single_message(
    From="YourNameHere <email@domain.io>",
    to="receiver@example.io",
    subject="Your Subject Here",
    html="<b>Test mail</b>",
    text="Test mail",
    additional_sending_options=sending_options
)
# print response
print(serialized)
```
## Deserialized & Serialized
---
All methods that serve API endpoints return two values:
`deserialized` - deserialized JSON response (json object)
`serialized` - serialized JSON response (json string)

## Justification
---
All request results come with additional key: `justify`
```python
"justify": {
    "msg": "Operation succeeded.", # Message for user
    "reason": "",                  # justification of failure
    "success": true                # indicator of success or failure
}
```
## Examples
---
For more examples check out [examples][mgapiexamples] directory.

## Supported endpoints
---
For more information visit: [Mailgun API Reference][mailgunapiref]

| Endpoint                                                  | Api Method          |
| :---------------------------------------------------------| :-------------------|
| POST /lists                                               | add_list            |
| POST /{domain}/messages                                   | send_single_message |
| POST /lists/{address}/members.json                        | bulk_add_members    |
| GET /domains/{domain}                                     | get_domains         |
| GET /domains                                              | get_domains         |
| GET /{domain}/bounces                                     | get_bounces         |
| GET /{domain}/bounces/{address}                           | get_bounces         |
| GET /{domain}/unsubscribes                                | get_unsubscribes    |
| GET /{domain}/unsubscribes/{address}                      | get_unsubscribes    |
| GET /{domain}/complaints                                  | get_complaints      |
| GET /{domain}/complaints/{address}                        | get_complaints      |
| GET /lists/{address}                                      | get_lists           |
| GET /lists/pages                                          | get_lists           |
| GET /lists/{address}/members/{member_address}             | get_members         |
| GET /lists/{address}/members/pages                        | get_members         |
| GET /{domain}/events                                      | get_events          |
| GET /{domain}/stats/total                                 | get_stats_total     |
| GET /<domain>/tags/<tag>/stats/aggregates/countries       | get_tag_aggregates  |
| GET /<domain>/tags/<tag>/stats/aggregates/providers       | get_tag_aggregates  |
| GET /<domain>/tags/<tag>/stats/aggregates/devices         | get_tag_aggregates  |
| GET /<domain>/tags/<tag>/stats                            | get_tag_stats       |
| GET /<domain>/tags                                        | get_tags            |
| GET /<domain>/tags/<tag>                                  | get_tags            |

[githubmy]: https://github.com/rolzwy7
[mailgunhome]: https://www.mailgun.com/
[mailgunapiref]: https://documentation.mailgun.com/en/latest/api_reference.html
[mgapiexamples]: https://github.com/rolzwy7/MailgunApiClient/tree/master/contrib/examples
