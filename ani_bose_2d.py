import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc, cm
from IPython.display import HTML
import mpl_toolkits.mplot3d.axes3d as p3

def animate(xx, yy, u):
    
    mpl.rcParams['figure.dpi']= 120 # Animation Size
    rc('animation', html='html5')
    z_max = np.max(np.max(u))
    def update_lines(num, u, N, frames):

        print("%i / 50 Frames loaded" %(num+1), end='\r')
        ax.clear()
        ax.set_zlim3d([0.0, z_max])
        line = ax.plot_surface(xx,yy,u[int(N/frames)*num], cmap=cm.coolwarm)
        return line,
    
    fig = plt.figure()
    ax = p3.Axes3D(fig)
    plt.close()
    line = ax.plot_surface(xx,yy,u[0])
    
    # Animation Parameters
    N = np.size(u[:,0,0]) # Number of Timesteps
    T = 5
    if N<50:
        frames = N
    else:
        frames = 50 # Number of Frames
        
    interval = T/frames*1000 # Time between Frames in ms
    
    ax.set_zlim3d([0.0, z_max])
    anim = animation.FuncAnimation(fig, update_lines,fargs = (u, N, frames),
                                   frames=frames, interval=interval, blit=True)
    return anim
