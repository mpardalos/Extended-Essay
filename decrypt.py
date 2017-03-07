d = 47
n = 143

ciphertext = [83, 125, 12, 12, 20]

def decrypt(c):
    return pow(c, d, n)

for i in ciphertext:
    print(decrypt(i), end=' ')
print()

