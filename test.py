import numpy as n

import random

m = int(input("m = "))
n = int(input("n = "))
y = int(input("y = "))
z = int(input("z = "))
a = [[random.randint(y, z) for i in range(n)] for j in range(m)]
print(a)
j = [min(a[b]) for b in range(len(a))]
print(j)
