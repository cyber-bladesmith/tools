#!/usr/bin/python3


import base64
import urllib.parse

iv="uJuNtbjjen0%3D"
auth="YmRtaW5pc3RyYXRvci0tqnLS3JaGN4g%3D"


decoded_iv = base64.urlsafe_b64decode(bytes(urllib.parse.unquote(iv), encoding='utf-8'))
decoded_auth = base64.urlsafe_b64decode(bytes(urllib.parse.unquote(auth), encoding='ISO-8859-1'))

decoded_auth = decoded_auth.decode('ISO-8859-1')
decoded_auth = decoded_auth.replace("b","a",1)

first_char = 61
second_char = 62
decoded_iv = decoded_iv.hex()
decoded_iv_char = int((decoded_iv[0]) + (decoded_iv[1]),16)


new_iv_char = hex(first_char^second_char^decoded_iv_char)
new_iv_char= (int(first_char)^int(second_char)^int(decoded_iv_char))


decoded_iv = decoded_iv.replace(str(hex(decoded_iv_char)).strip("0x"),str(hex(new_iv_char).strip("0x")),1)
new_iv = urllib.parse.quote(base64.urlsafe_b64encode(bytes.fromhex(decoded_iv)))
new_auth = urllib.parse.quote(base64.urlsafe_b64encode(bytes(decoded_auth, encoding='ISO-8859-1')))
print(new_iv)
print(new_auth)

#01100001
#01100010

#00000011
#00111101
#00111110