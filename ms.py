#!/usr/bin/env python3

import numpy as np
from pulp import *

n = 7
magic_sum = (n ** 3 + n) / 2
squares = values = range(1, n**2 + 1)
template = np.array(values).reshape(n, n)

model = LpProblem(name="Magic Square")

x = LpVariable.dicts("x", (squares, values), cat="Binary")

for i in squares:
     model += lpSum([x[i][j] for j in values]) == 1

for j in values:
     model += lpSum([x[i][j] for i in squares]) == 1

for k in range(n):
     line = template[k]
     column = template[:, k]
     model += lpSum([x[i][j]*j for i in line for j in values]) == magic_sum
     model += lpSum([x[i][j]*j for i in column for j in values]) == magic_sum

model += lpSum([x[i][j]*j for i in template.diagonal() for j in values]) == magic_sum
model += lpSum([x[i][j]*j for i in np.fliplr(template).diagonal() for j in values]) == magic_sum

print(model)

solution = model.solve()

for i in squares:
     for j in values:
          if value(x[i][j]) == 1:
               print(j, end=' ')
     if i % n == 0:
          print()
