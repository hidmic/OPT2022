#!/usr/bin/env python3

import numpy as np
import picos as pc

shipment_cost = pc.Problem()

C = np.array([[25, 24, 27, 28, 25, 29],
              [26, 31, 26, 25, 32, 28]])

s = np.array([[150, 200]]).T
P = pc.RealVariable('P', (2, 6))

shipment_cost.minimize = pc.trace(C * P.T)
shipment_cost.add_constraint(P * np.ones(6)[np.newaxis].T <= s)
shipment_cost.add_constraint(pc.sum(P[:,:3]) == 130)
shipment_cost.add_constraint(pc.sum(P[:,3:]) == 130)
shipment_cost.add_constraint(P >= 0)

print(shipment_cost)

shipment_cost.solve()
print(P.value)
