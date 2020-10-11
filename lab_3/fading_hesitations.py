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

iterations = int(input('Input number of iterations: '))
while True:
    mode = input(f'Choose mode of program:\n 1 - without fading\n 2 - with fading\n')
    if mode == "1" or mode == "2":
        break
    else:
        print('Wrong mode')
        continue