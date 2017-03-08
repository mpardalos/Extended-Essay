from fractions import gcd

import matplotlib.pyplot as plt

def phi(n):
    result = 0
    for i in range(1, n+1):
        if gcd(n, i) == 1:
            result += 1
    return result

x = list(range(10000))
y = [phi(n) for n in x]

plt.scatter(x, y, s=0.6, marker='.', c=(0, 0, 1, 1))

plt.xlabel('n')
plt.ylabel('$\phi(n)$', rotation='horizontal')
plt.show()

