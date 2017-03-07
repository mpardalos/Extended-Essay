e = 23
n = 143

plaintext = [8, 5, 12, 12, 15]

def encrypt(p):
    return pow(p, e, n)

for i in plaintext:
    print(encrypt(i), end=' ')
print()

