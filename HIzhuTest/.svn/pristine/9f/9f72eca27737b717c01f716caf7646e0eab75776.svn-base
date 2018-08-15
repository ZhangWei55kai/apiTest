#coding:utf-8
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
key = RSA.generate(1024)
c = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDYagHoYrjcdl8cCxpEBO2eyGs
Feu44/atWuReFXhwl/EHqqTOfRna5HR56xv/R99Mt2zNFuig8spEoWlJkRv5Eg1M
CNvvAQKFFjlKReYhqgZ2g2yZCi7vLDVDqfg+BQKK+He45M7Jl9YRT1RS4SysNARJ
rPcyCk/GSaCsZkNJiwIDAQAB
-----END PUBLIC KEY-----"""

p = """-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----"""
def Decrypt(prikey,data):
        rsaKey = RSA.importKey(prikey)
        cipher = PKCS1_v1_5.new(rsaKey)
        decodeData = base64.b64decode(data)
        text=  cipher.decrypt(decodeData, key)
        return text

def Encrypt(pubkey,data):
        rsaKey = RSA.importKey(pubkey)
        cipher = PKCS1_v1_5.new(rsaKey)
        return base64.b64encode(cipher.encrypt(data))

if __name__ == "__main__":
    baseCode = Encrypt(c, '15216627457')
    print Decrypt(p,baseCode)
