# Python SleentO

## installation

```sh
pip install sleento
```

### Usage

```py
from sleento.service import Client, Message

client = Client(
    cid='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', # replace with your cid
    auth_token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # your auth_token
)

message = Message(
    client=client,
    to_phone_number="+243xxxxxxxxx",
    body="Hello World"
)

res = message.send() # send the message

print(res.status_code, res.text)
```