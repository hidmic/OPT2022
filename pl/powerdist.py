#!/usr/bin/env python3

import numpy as np
import picos as pc

power_distribution_cost = pc.Problem()

s = np.array([[35, 50, 40]]).T
d = np.array([[45, 20, 30, 30]]).T
C = np.array([[8, 6, 10, 9],
              [9, 12, 13, 7],
              [14, 9, 16, 5]])
P = pc.RealVariable('P', (3, 4))

power_distribution_cost.minimize = pc.trace(C * P.T)
power_distribution_cost.add_constraint(P * np.ones(4)[np.newaxis].T <= s)
power_distribution_cost.add_constraint(P.T * np.ones(3)[np.newaxis].T == d)
power_distribution_cost.add_constraint(P >= 0)

print(power_distribution_cost)

power_distribution_cost.solve()
print(P.value)
