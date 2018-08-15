#coding:utf-8
import hashlib
clientKey = '''-----BEGIN RSA PRIVATE KEY-----
MIICWwIBAAKBgQCmMXdis1fksa9acLR1fB6m2F/HvvFhzDR9Bbi6W89AHZiYTSZ5
zPi8qbzm4kh21N+pWVXvUzHdbXEsue/yP5J1pqveHg76btEc5Q73SYZnHnmVEPuJ
sQBAfl0hr4rmGRjET1j4OXCjwX4odS+t/bBB6KATPj+s1rnu7GWe+9A9TQIDAQAB
AoGAc3C63+l5rRarmmPdRhpgZD66UVJV8zvYXduilHh/fqbQP0Kf7k0tnkc9OxeF
hF2butOeOK6OXaPO0GWbwabdARN1NkU/zs0sqvVygiwvTKwpZnMi5Q2inb8DCS7a
DWxrFnh3GjIFlb2o7OoVxTw2PtIxcodPWMT9mweBzOpMHhUCQQDV750/7iPJWN+W
mqpyqPuV1SGQ6jkZ5Y3M6o2t0iAIbw4fSehmCtUek5WCaXRrC8E8xa2oBiQ1ZXBS
1DfUxdlTAkEAxt69CFxNKCE50Eg5nTt5cwwwzVsClsHqzRxm7duu2qhEXUZAyJW6
A3aEmkdRHl+WCFpiY22XHVDIa1lhAtSa3wJAIQdbWbFkaQOFkXTTd9xK6zj6c6sV
ob/lAov7z6gvNd4fagk5DfgCKzRR0s6BIL2x2bYTN2urT2sXylHlRL4+7QJAZuF0
CY82mzwVHJtAswbBnbMAzDv46uUHA3VeCk9L9fJ264ocmahbws7darLaVEw+4bNg
ku9u7cuM43wpo705IQJAXZARwt5wSM282XIcZjAIVazdI1efFYFkLubV66XDBbHh
Sms3VcYPxZnA3HuC+jyzLL4qYRO3UdMA9hHteXJO5Q==
-----END RSA PRIVATE KEY-----'''
platform = "iPhone".lower()
clientV = "2.9.2"
md5 = hashlib.md5(clientKey + clientV + platform).hexdigest()
header = {
              "ScreenSize":"640x960",
              "AppForm":"lord",
              "Platform": platform,
              "Project":platform,
              "ClientVer": clientV,
              "Udid": "123456",
              "DeviceId": "654321",
              "MD5": md5,
              }
