import matplotlib.pyplot as plt
import numpy as np


def func(x):
    # Convert Degree to Radian
    rad = np.deg2rad(x)

    y =  np.sin(rad) - np.cos(rad)
    return y

if __name__ == "__main__":
    x = np.linspace(-180, 180)
    y = func(x)

    plt.plot(x,y)
    plt.show()


