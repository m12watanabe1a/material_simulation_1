import matplotlib.pyplot as plt
import numpy as np
import csv

alpha = 0.005

w0 = 12.0
w1 = 1.0
w2 = -2.0

 # w0 = -6.0
 # w1 = 1.0
 # w2 = -2.0

def func(x,y):
    global w0, w1, w2
    return w0 + w1 * x + w2 * y

def logistic(x):
    return 1 / (1 + np.exp(-x))

# Function for Draw Line
def func_line(x):
    global w0, w1, w2
    return - ( w0 + w1 * x ) / w2

if __name__ == "__main__":
    # Open CSV File
    csv_file = open('./assets/data2.csv', 'r', encoding='utf8');
    csv_data = csv.DictReader(csv_file)

    x = []
    y = []
    t = []

    y0 = []
    x0 = []

    y1 = []
    x1 = []

    # Read All Line from CSV Data
    for line in csv_data:
        x.append(line['x'])
        y.append(line['y0'] if line['y0'] else line['y1'])
        t.append(line['type'])

        if line['y0']:
            y0.append(line['y0'])
            x0.append(line['x'])
        elif line['y1']:
            y1.append(line['y1'])
            x1.append(line['x'])

    # Convert into Numpy Array
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    t = np.array(t, dtype=float)

    y0 = np.array(y0, dtype=float)
    x0 = np.array(x0, dtype=float)
    y1 = np.array(y1, dtype=float)
    x1 = np.array(x1, dtype=float)

    # Plot Input Data ( change color by type )
    plt.scatter(x0, y0, color='b')
    plt.scatter(x1, y1, color='r')

    sum_e = 0.0
    sum_e_pre = 0.0
    for i in range(100):

        # Calculate Error (Changed)
        f = func(x, y)
        P = logistic(f)
        Pn = P**t * (1.0 - P)**(1-t)

        sum_P_n = np.sum(Pn)
        sum_e = - np.log(sum_P_n)

        dE_dw0 = P - t
        dE_dw1 = (P - t) * x
        dE_dw2 = (P - t) * y

        sum_dE_dw0 = np.sum(dE_dw0)
        sum_dE_dw1 = np.sum(dE_dw1)
        sum_dE_dw2 = np.sum(dE_dw2)

        laplacian_E = np.array([sum_dE_dw0, sum_dE_dw1, sum_dE_dw2])
        W = np.array([w0, w1, w2])
        w0_new, w1_new, w2_new = W + alpha * (- laplacian_E)

        # Swap
        w0, w1, w2 = w0_new, w1_new, w2_new

        # If Error Converges then Break the Loop
        if(abs(sum_e_pre - sum_e) < 1e-3):
            break
        sum_e_pre = sum_e

    plt.plot(x, func_line(x), color='gray')
    plt.xlim([0,11])
    plt.ylim([0,11])
    plt.show()
