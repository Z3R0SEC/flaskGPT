import os
import sys
import time
from requests import get

def get_response(incoming_msg):
    name = "Friend"
    api = "https://mota-dev.x10.bz/lwandle"
    dat = { "name": name, "prompt": incoming_msg }
    try:
      send = get(api, params=dat)
      res = send.json()
      if res.reply:
         return res.reply
      if res.error:
         return res.error
    except Exception as e:
        return f"Error: {send.text} ? e ? {e}"
