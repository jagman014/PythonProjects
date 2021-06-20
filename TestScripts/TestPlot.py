# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:50:01 2019

@author: jagma
"""

import math  # Importing Maths Packages

import matplotlib.pyplot as plt  # Importing Ploting Package
import numpy as np

x = np.linspace(0, 2, 100)  # Defining x-array
y, y1 = [], []  # Defining Empty y-arrays

for i in range(len(x)):  # For Loops to calculate y-values
    y.append(math.sin(np.pi * x[i]))

for i in range(len(x)):
    y1.append(math.cos(np.pi * x[i]))

plt.figure(1)  # New Figure
plt.subplot(211)  # Subplot 2x1 plot 1
plt.plot(x, y, 'kx-')  # Plot x vs y
plt.title('Maths Functions')  # Plot Title
plt.xlabel('x/$\pi$')  # x-axis Label
plt.ylabel('y')  # y-axis Label
plt.subplot(212)  # Subplot 2x1 plot 2
plt.plot(x, y1, color='red', marker='o')  # Plot x vs y1
plt.xlabel('x/$\pi$')
plt.ylabel('y')
plt.show()
# %%
from matplotlib import cm  # Import Colour-mapping

fig = plt.figure(2)
ax = fig.add_subplot(1, 2, 1, projection='3d')  # Sets 1x2 Subplot to 3D

x = np.arange(-2, 2, 0.1)
y = np.arange(-2, 2, 0.1)
X, Y = np.meshgrid(x, y)  # Meshgrid x and y Values
R = np.sqrt((np.pi * X) ** 2 + (np.pi * Y) ** 2)  # Function of x and y
Z = np.sin(R)  # Function on R

surf = ax.plot_surface(X, Y, Z, cmap=cm.winter, antialiased=False)  # 3D Surface Ploy

ax.set_zlim(-1.01, 1.01)  # Limit z-axis
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('$\sin({\sqrt{x^2 + y^2}})$')

fig.colorbar(surf, shrink=0.5, aspect=5)  # Sets Colour-bar on Figure

ax = fig.add_subplot(1, 2, 2, projection='3d')

r = np.linspace(0, 1.25, 50)
p = np.linspace(0, 2 * np.pi, 50)
R, P = np.meshgrid(r, p)
Z = ((R ** 2 - 1) ** 2)

X, Y = R * np.cos(P), R * np.sin(P)

surf = ax.plot_surface(X, Y, Z, cmap=cm.YlGnBu_r)

ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')
plt.show()
