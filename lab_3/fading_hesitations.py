import matplotlib.pyplot as plt
import numpy as np

m = 5
k1 = 3
k2 = 3
x = 4
y = 0
x1 = 2
y1 = 3
t = 0
p = 0.3
s = 0.5
x2 = 0
y2 = 0
array = [
    [0, 0, 0, 2, 3, 4, 0]
]

def count_values(mode, t, x1, y1, x, y, p):
    if mode == "1":
        x2 = -k1 / m * x
        y2 = -k2 / m * y
    else:
        x2 = -k1 / m * x - p * x1
        y2 = -k2 / m * y - p * y1
    t = t + s
    x1 = x1 + x2 * s
    y1 = y1 + y2 * s
    x = x + x1 * s
    y = y + y1 * s
    return [t, x2, y2, x1, y1, x, y]

iterations = int(input('Input number of iterations: '))
while True:
    mode = input(f'Choose mode of program:\n 1 - without fading\n 2 - with fading\n')
    if mode == "1" or mode == "2":
        break
    else:
        print('Wrong mode')
        continue

for i in range(iterations):
    array.append(count_values(mode, t, x1, y1, x, y, p))
    t,x2,y2,x1,y1,x,y = count_values(mode, t, x1, y1, x, y, p)