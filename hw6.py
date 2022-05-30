import Crypto
import random
p = 37
g = 5

a = random.randint(0, p)
b = random.randint(0, p)

A = pow(g, a) % p
B = pow(g, b) % p

s1 = pow(B, a) % p
s2 = pow(A, b) % p

print(s1)
print(s2)