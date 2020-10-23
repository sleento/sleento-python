# Python SleentO

## installation

```sh
pip install sleento
```

### Usage

```py
from sleento import Client, Message

client = Client(
            cid='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    auth_token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
)

message = Message(
    client=client,
    to_phone_number="+243xxxxxxxxx",
    body="Hello World"
)

res = message.send()

print(res.status_code, res.text)
```