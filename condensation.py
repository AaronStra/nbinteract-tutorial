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
from mpmath import *

def plot():
    
    def calc_n(mu, T, d):
        V=1e16
        s = np.exp(mu/T)
        g = np.zeros_like(mu)
        for k in range(len(mu)):
            g[k]=polylog(d/2,s[k])
        n = 1/V*s/(1-s)+T**(3/2)*g
        return n
    
    x = -np.logspace(-15, 0, 50)
    y = np.arange(0.1, 5, 0.5)
    X, Y = np.meshgrid(x, y)
    zs = np.array(calc_n(np.ravel(X), np.ravel(Y),3))
    Z = zs.reshape(X.shape)
    
    fig = plt.figure(dpi=70)
    ax = p3.Axes3D(fig)
    
    line1 = ax.plot_wireframe(X, Y, Z, alpha = 0.3)
    line2 = ax.contour(X, Y, Z,6,linewidths = 5)
    ax.set_xlabel('Chemical Potential')
    ax.set_ylabel('Temperature')
    ax.set_zlabel('Particle Density')

    def update(index):
        zs = np.array(calc_n(np.ravel(X), np.ravel(Y),index))
        Z = zs.reshape(X.shape)
        ax.clear()
        ax.set_xlabel('Chemical Potential $\mu$', fontsize = 16)
        ax.set_ylabel('Temperature $T$', fontsize = 16)
        ax.set_zlabel('Particle Density $n$', fontsize = 16)
        line1=ax.plot_wireframe(X, Y, Z, alpha = 0.3)
        line2=ax.contour(X, Y, Z,6,linewidths = 5)

    
    # Defining Sliders
    
    inter = interact(update,
                     index = widgets.IntSlider(min=1,max=4,step=1,value=3,description='Dimensions:',disabled=False));
    
    return inter

