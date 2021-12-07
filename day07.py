import os
import sys

import numpy as np

# test input.
#y = [16,1,2,0,4,2,7,1,2,14]
# real input.
#y = np.loadtxt("day07.txt")
with open("day07.txt") as f:
    y = f.read().strip().split(',')
y = np.array(y).astype(int)
#print(y)

def fuel_required(i):
    return np.sum(np.abs(y - i))
def fuel_required2(i):
    y_ = [np.abs(x - i) for x in y]
    fuel = [x * (x+1) / 2 for x in y_]
    return np.sum(fuel)

#x = np.linalg.norm(y)

x = [fuel_required2(i) for i in range(np.min(y), np.max(y)+1)]
fuel_total = np.min(x)
print(fuel_total)