import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import LinAlgError
 

def plot_3D(X, y, B, B0):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(X[:, 0], X[:, 1], y, color='blue', marker='o', label='Data Points')

    x1_range = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
    x2_range = np.linspace(X[:, 1].min(), X[:, 1].max(), 100)
    x1_mesh, x2_mesh = np.meshgrid(x1_range, x2_range)
    regression_line = B[0] * x1_mesh + B[1] * x2_mesh + B0

    ax.plot_surface(x1_mesh, x2_mesh, regression_line, alpha=0.5, color='red', label='Regression Line')

    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('y')
    plt.show()


def plot2D(X, y, B, B0):
    plt.scatter(X, y, color='blue', marker='o', label='Data Points')
    plt.plot(X, B*X + B0, color='red', label='Regression Line')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.show()


def plot_2and_3D(X, y, B, B0):
    fig = plt.figure()
    ax = fig.add_subplot(121)
    ax2 = fig.add_subplot(122, projection='3d')

    ax.scatter(X[:, 0], y, color='blue', marker='o', label='Data Points')
    ax.plot(X[:, 0], B[0]*X[:, 0] + B0, color='red', label='Regression Line')
    ax.set_xlabel('X1')
    ax.set_ylabel('y')

    ax2.scatter(X[:, 0], X[:, 1], y, color='blue', marker='o', label='Data Points')

    x1_range = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
    x2_range = np.linspace(X[:, 1].min(), X[:, 1].max(), 100)
    x1_mesh, x2_mesh = np.meshgrid(x1_range, x2_range)
    regression_line = B[0] * x1_mesh + B[1] * x2_mesh + B0

    ax2.plot_surface(x1_mesh, x2_mesh, regression_line, alpha=0.5, color='red', label='Regression Line')

    ax2.set_xlabel('X1')
    ax2.set_ylabel('X2')
    ax2.set_zlabel('y')
    plt.show()
