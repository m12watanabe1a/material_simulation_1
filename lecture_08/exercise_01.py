import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    A = np.array([
        [3, 6, 1],
        [4, 9, 2],
        [2, 3, 4]
    ])
    A_inv = np.linalg.inv(A)

    v = np.array([4, 3, 9])

    xyz = np.dot(A_inv, v)

    print("x = {:.2g}".format(xyz[0]))
    print("y = {:.2g}".format(xyz[1]))
    print("z = {:.2g}".format(xyz[2]))



