import sys

mines = int(input('mines: '))
rows = int(input('rows: '))
columns = int(input('columns: '))
x = int(rows * columns)

m = []
m.append(mines)

r = []
r.append(rows)

c = []
c.append(columns)

matrix = [r, c, m]
print(matrix)