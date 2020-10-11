import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib import rcParams
import matplotlib

def update_plot(frame_number, zarray, plot):
    plot[0].remove()
    plot[0] = ax.plot_surface(x, y, zarray[:,:,frame_number], cmap="magma")

fps = 3 # frame per sec
frn = 30 # frame number of the animation
zarray = np.zeros((6,6,frn))
x = np.linspace(1, 6, 6)
x, y = np.meshgrid(x, x)
arr = np.zeros((30, 6, 6))
#Initial task data
c  = 2
p = 100
l = 20
u_cp = 100
h = 0.2
s = 0.1 
n = 5
a = 50
for i in range(6):
    for j in range(6):
        arr[0][i][j] = 20

for d in range(1,frn):
    for i in range(1, 5):
        for j in range(1, 5):
            arr[d][i][j] = l*s/c/p/h**2*(arr[d-1][i+1][j] + arr[d-1][i-1][j] + arr[d-1][i][j-1]+ arr[d-1][i][j+1] - 4*arr[d-1][i][j]) + arr[d-1][i][j]
    for i in [0,5]:
        for j in range(6):
            arr[d][i][j] = (a*h/l*u_cp+arr[d][abs(i-1)][j])/(1+a*h/l)
    for i in range(6):
        for j in [0,5]:
            arr[d][i][j] = (a*h/l*u_cp+arr[d][i][abs(j-1)])/(1+a*h/l)

for i in range(frn):
    zarray[:,:,i] = arr[i]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plot = [ax.plot_surface(x, y, zarray[:,:,0], color='0.75', rstride=1, cstride=1)]
ax.set_zlim(0,100)
ani = animation.FuncAnimation(fig, update_plot, frn, fargs=(zarray, plot), interval=1000/fps)

fn = 'plot_surface_animation_funcanimation'
ani.save(fn+'.mp4',writer='ffmpeg',fps=fps)
ani.save(fn+'.gif',writer='imagemagick',fps=fps)


