import json
import subprocess
from sseclient import SSEClient


_pizza = "179"
_email = ""
_access_token = ""

def notify():
    subprocess.run(["curl",
                    "--header", "Access-Token: %s" % _access_token,
                    "--header", "Content-Type: application/json",
                    "--request", "POST",
                    "--data-binary", "{\"body\":\"PIZZA\",\"title\":\"PIZZA\",\"type\":\"note\",\"email\":\"%s\"}" % _email,
                    "https://api.pushbullet.com/v2/pushes"])


messages = SSEClient("http://pizza.onoc.eu/events")
for msg in messages:
    if "pizza_list" in msg.data:
        l = json.loads(msg.data)
        print(l)
        for k, v in l["pizza_list"].items():
            if _pizza in v:
                notify()
