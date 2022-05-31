import Crypto
import random
import hashlib
import pyaes
import os


def pad_and_sep(bytes):
    length = len(bytes)
    for i in range(0, length, 16): 
        if length - i < 16:
            temp = bytes[i:i + 16]
            pad = 16 - len(temp)
            for x in range(0, pad):
                temp.append(pad)
            yield temp
        else:
            yield (bytes[i:i + 16])
            
def xor_hex(string1, hex2):
    #Input: A string and a list of hex values, without the 0x part
    #Output: List of hex values xor'd
    if len(string1) != len(hex2):
        print("ERROR: INEQUAL LENGTH")
        return
    length = len(string1)
    ans = []
    for x in range(0, length):
        letter1 = ord(string1[x])
        letter2 = int(hex2[x], 16)
        temp = hex(letter1 ^ letter2)[2:]
        if len(temp) < 2:
            temp = "0" + temp
        ans.append(temp)
    return ans  


""" p = int("B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371", 16)
g = int("A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28AD662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5", 16) """

p = 37
g = 5


a = random.randint(0, p)
b = random.randint(0, p)

A = pow(g, a, p) 
B = pow(g, b, p)

s1 = pow(B, a, p)
s2 = pow(A, b, p)


#Initializing AES 
key = hashlib.sha256(bytes(s1)).hexdigest()
key = bytes.fromhex(key[0:32])

iv = "InitializationVe"
aes = pyaes.AES(key)


#Turning into ASCII, message 1
message1 = "Hi Bob!"
message1bytes = []
for character in message1:
    message1bytes.append(ord(character))

#Padding
padded1 = list(pad_and_sep(message1bytes))

#XOR'ing and encrypting
encrypted1 = []
for x in padded1:
    temp = []
    for y in x:
        temp.append(hex(y)[2:])
    temp = xor_hex(iv, temp)
    for y in range(len(temp)):
        temp[y] = int(temp[y], 16)
        
    temp = aes.encrypt(temp)
    for y in temp:
        encrypted1.append(hex(y)[2:])
        
        
        
#Turning into ASCII, message 2
message2 = "Hi Alice!"
message2bytes = []
for character in message2:
    message2bytes.append(ord(character))

#Padding
padded2 = list(pad_and_sep(message2bytes))

#XOR'ing and encrypting
encrypted2 = []
for x in padded2:
    temp = []
    for y in x:
        temp.append(hex(y)[2:])
    temp = xor_hex(iv, temp)
    for y in range(len(temp)):
        temp[y] = int(temp[y], 16)
        
    temp = aes.encrypt(temp)
    for y in temp:
        encrypted2.append(hex(y)[2:])        

print(encrypted1)
print(encrypted2)