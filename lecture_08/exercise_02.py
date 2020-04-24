import matplotlib.pyplot as plt
import numpy as np
import csv

if __name__ == "__main__":
    # Open CSV File
    csv_file = open('./assets/data1.csv', 'r', encoding='utf8');
    csv_data = csv.DictReader(csv_file)

    x = []
    y = []

    # Read All Line from CSV Data
    for line in csv_data:
        x.append(line['x:English Score'])
        y.append(line['y:Math Score'])

    # Convert into Numpy Array
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    n = len(x)

    # Least-Squares Method
    A = np.array([
        [n, np.sum(x)],
        [np.sum(x), np.sum(x**2)]
    ])
    A_inv = np.linalg.inv(A)

    v = np.array([np.sum(y), np.sum(x*y)])

    a0, a1 = np.dot(A_inv, v)


    # Plot Data
    plt.scatter(x, y, color = 'b')

    # Draw Fit Line
    x1 = 0.0
    y1 = a1 * x1 + a0

    x2 = 100.0
    y2 = a1 * x2 + a0
    plt.plot([x1, x2], [y1, y2], color = 'r')

    plt.show()
