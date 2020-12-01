#!/usr/bin/ruby

iv = "uJuNtbjjen0%3D"
auth = "YmRtaW5pc3RyYXRvci0tqnLS3JaGN4g%3D"

require 'uri'
require 'base64'


#decoded_iv = URI.unescape(iv)
decoded_iv = Base64.decode64(URI.unescape(iv))
decoded_auth = Base64.decode64(URI.unescape(auth))


decoded_iv[0]=('a'.ord^'b'.ord^decoded_iv[0].ord).chr
decoded_auth[0]='a'

new_iv = URI.escape(Base64.strict_encode64(decoded_iv),"+=/")
new_auth = URI.escape(Base64.strict_encode64(decoded_auth),"+=/")

puts new_iv
puts new_auth
