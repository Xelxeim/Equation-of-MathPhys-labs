import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import cm


def modify_last_arr(array, a, h, s):
    for j in range(1, 6):
        for k in range(1, 6):
            array[2][j][k] = (a ** 2) * (s ** 2) * (array[1][j][k + 1] + array[1][j][k - 1] + array[1][j + 1][k] + \
                                                    array[1][j - 1][k] - 4 * array[1][j][k]) / (h ** 2) + 2 * \
                             array[1][j][k] - array[0][j][k]
    return array


def swap_arr(array):
    for j in range(1, 6):
        for k in range(1, 6):
            array[0][j][k] = array[1][j][k]
            array[1][j][k] = array[2][j][k]
    return array


def make_graph(array):
    zgrid = np.array(array)
    xgrid = np.array([
        [0, 1, 2, 3, 4, 5, 6],
        [0, 1, 2, 3, 4, 5, 6],
        [0, 1, 2, 3, 4, 5, 6],
        [0, 1, 2, 3, 4, 5, 6],
        [0, 1, 2, 3, 4, 5, 6],
        [0, 1, 2, 3, 4, 5, 6],
        [0, 1, 2, 3, 4, 5, 6]
    ])
    ygrid = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5, 5, 5],
        [6, 6, 6, 6, 6, 6, 6]
    ])
    fig = pylab.figure()
    axes = Axes3D(fig)
    axes.plot_surface(xgrid, ygrid, zgrid, cmap=cm.viridis)
    axes.set_zlim(-5, 5)
    filename = f'graph{counter}'
    pylab.savefig(filename, bbox_inches='tight')


array = [
    [
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
        [0.00, 0.50, 1.50, 2.00, 1.50, 0.50, 0.00],
        [0.00, 1.50, 3.00, 4.00, 3.00, 1.50, 0.00],
        [0.00, 2.00, 4.00, 5.00, 4.00, 2.00, 0.00],
        [0.00, 1.50, 3.00, 4.00, 3.00, 1.50, 0.00],
        [0.00, 0.50, 1.50, 2.00, 1.50, 0.50, 0.00],
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
    ],
    [
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
        [0.00, 0.50, 1.50, 2.00, 1.50, 0.50, 0.00],
        [0.00, 1.50, 3.00, 4.00, 3.00, 1.50, 0.00],
        [0.00, 2.00, 4.00, 5.00, 4.00, 2.00, 0.00],
        [0.00, 1.50, 3.00, 4.00, 3.00, 1.50, 0.00],
        [0.00, 0.50, 1.50, 2.00, 1.50, 0.50, 0.00],
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
    ],
    [
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
        [0.00, 0.50, 1.50, 2.00, 1.50, 0.50, 0.00],
        [0.00, 1.50, 3.00, 4.00, 3.00, 1.50, 0.00],
        [0.00, 2.00, 4.00, 5.00, 4.00, 2.00, 0.00],
        [0.00, 1.50, 3.00, 4.00, 3.00, 1.50, 0.00],
        [0.00, 0.50, 1.50, 2.00, 1.50, 0.50, 0.00],
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
    ]
]

a = 10
s = 0.003
h = 0.1
counter = 0
flag = True
while flag:
    array = modify_last_arr(array, a, h, s)
    array = swap_arr(array)
    make_graph(array[2])
    counter += 1
    if counter >= 25:
        flag = False
