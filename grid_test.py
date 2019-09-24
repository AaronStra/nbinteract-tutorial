from ipywidgets import *
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import cm
import numpy as np
def plot():
    
    def spacial_grid(Lx,Nx,Ly,Ny):
        dx, dy = Lx/Nx, Ly/Ny
        x_array = np.arange(-Lx/2,Lx/2,dx)
        y_array = np.arange(-Ly/2,Ly/2,dy)
        xx, yy = np.meshgrid(x_array,y_array)
        return xx, yy
    
    xx,yy = spacial_grid(16,10,16,10)
    zz = 1/2*(xx**2+yy**2)
    fig = plt.figure(dpi=70)
    ax = p3.Axes3D(fig)
    line = ax.plot_surface(xx,yy,zz,cmap=cm.coolwarm)

    
    def update(Nx, Ny):
        xx,yy = spacial_grid(16,Nx,16,Ny)
        zz = 1/2*(xx**2+yy**2)
        ax.clear()
        ax.set_xlabel("x", fontsize = 16)
        ax.set_ylabel("y", fontsize = 16)
        ax.set_zlabel("z", fontsize = 16)
        line = ax.plot_surface(xx,yy,zz,cmap=cm.coolwarm)
       
    
    # Defining Sliders
    
    inter = interact(update,
                     Nx=widgets.IntSlider(min=2,max=64,step=4,value=10),
                     Ny=widgets.IntSlider(min=2,max=64,step=4,value=10));
    
    return inter