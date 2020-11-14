#!/usr/bin/python3

#JWT - Tool to create and sign a JWT based on a key or file.

import base64
import hmac
import hashlib

pub = open("public.pem")
pub2 = pub.read()
key = "key"

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ"

signature = base64.urlsafe_b64encode(hmac.new(bytes(key, encoding='utf8'),token.encode('utf-8'), hashlib.sha256).digest()).decode('utf-8').rstrip('=')

print(token+ '.' + signature)



pub.close()