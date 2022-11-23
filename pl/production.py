#!/usr/bin/env python3

import numpy as np
import picos as pc

production_cost = pc.Problem()

p = pc.RealVariable('p', 4)
e = pc.RealVariable('e', 4)
i = pc.RealVariable('i', 4)

d = np.array([[40, 60, 75, 25]]).T
production_cost.add_constraint(
    i[0] == p[0] + e[0] + 10 - d[0])
for k in range(1, 4):
    production_cost.add_constraint(
        i[k] == p[k] + e[k] + i[k - 1] - d[k])
production_cost.add_constraint(p + e + i >= d)
production_cost.add_constraint(p <= 40)
production_cost.add_constraint(p >= 0)
production_cost.add_constraint(e >= 0)
production_cost.add_constraint(i >= 0)

production_cost.minimize = pc.sum(400 * p + 450 * e + 20 * i)

print(production_cost)
production_cost.solve()

print("P " + ", ".join(map(str, map(int, p.value))))
print("E " + ", ".join(map(str, map(int, e.value))))
print("I " + ", ".join(map(str, map(int, i.value))))
