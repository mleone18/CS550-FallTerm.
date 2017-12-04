import sys

f = 0
g = 1
for i in range(0, 16):
    f = f + g
    g = f - g
    print(f)

