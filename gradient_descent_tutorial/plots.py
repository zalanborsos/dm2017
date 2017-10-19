import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D 

def initial_plot(f):
    matplotlib.rcParams['xtick.direction'] = 'out'
    matplotlib.rcParams['ytick.direction'] = 'out'

    delta = 0.025
    x = np.arange(-5.0, 5.0, delta)
    y = np.arange(-5.0, 5.0, delta)
    X, Y = np.meshgrid(x, y)
    Z = f([X, Y])

    fig = plt.figure(figsize=(20, 6))

    ax = fig.add_subplot(1, 2, 1, projection='3d')

    ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
    cset = ax.contour(X, Y, Z, zdir='z', offset=0, cmap=cm.coolwarm)

    ax.set_xlim3d(-5, 5)
    ax.set_ylim3d(-5, 5)
    ax.set_zlim3d(0, 10)

    ax2 = fig.add_subplot(1, 2, 2)
    levels = [5, 10, 15, 25, 50, 100, 150]
    CS = ax2.contour(X, Y, Z, levels)
    ax2.clabel(CS, inline=1, fontsize=10, cmap=cm.coolwarm)
    ax2.set_xlabel('$x_0$')
    ax2.set_ylabel('$x_1$')
    ax2.set_title('$f(\mathbf{x})$')

def trajectory_visualization(f, n_iter, trajectory):
    delta = 0.025
    x = np.arange(-5.0, 5.0, delta)
    y = np.arange(-5.0, 5.0, delta)
    X, Y = np.meshgrid(x, y)
    Z = f([X, Y])
    
    fig = plt.figure(figsize=(20, 5))
    ax = fig.add_subplot(1, 2, 2)
    
    levels = [5, 10, 15, 25, 50, 100, 150]
    CS = ax.contour(X, Y, Z, levels)
    ax.clabel(CS, inline=1, fontsize=10, cmap=cm.coolwarm)
    ax.set_xlabel('$x_0$')
    ax.set_ylabel('$x_1$')
    ax.set_title('{}'.format(n_iter))
    ax.plot(trajectory[:n_iter, 0], trajectory[:n_iter, 1], '-o', markersize=10, color='red')
   
    