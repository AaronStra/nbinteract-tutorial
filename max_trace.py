#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 01:26:28 2019

@author: aaron
"""
from ipywidgets import *
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import cm
import numpy as np
from math import pi

def plot(gpe_solve):
    
    xx,yy,u = gpe_solve(16,32,16,32,10,0.1,-10,1)
    t = np.arange(0,9.9,0.1)
    u_max = np.max(u,axis=(1,2))
    fig = plt.figure(dpi=70)
    ax = fig.add_subplot(1, 1, 1)
    ax.set_ylim(0,4)
    ax.set_ylabel(r"Peak Value of $\psi^2$", fontsize = 16)
    ax.set_xlabel("Time", fontsize = 16)
    ax.grid()
    line, = ax.plot(t,u_max[:-1])

    def update(K,index):
        if index == "U = 0":
            xx,yy,u = gpe_solve(16,32,16,32,10,0.1,K,1)
        else:
            xx,yy,u = gpe_solve(16,32,16,32,10,0.1,K,2)
        u_max = np.max(u,axis=(1,2))
        line.set_ydata(u_max[:-1])

    
    # Defining Sliders
    
    inter = interact(update,
                     K=widgets.FloatSlider(min=-10,max=10,step=0.01,value=0),
                     index = widgets.RadioButtons(options=["U = 0","U = harmonic"],
                                                   description='Potential:',disabled=False));
    
    return inter

