import matplotlib.pyplot as plt
import numpy as np
import csv

if __name__ == "__main__":
    # Open CSV File for data2
    csv_file = open('./assets/data2.csv', 'r', encoding='utf8');
    csv_data = csv.DictReader(csv_file)

    x = []
    y = []

    # Read All Line from CSV Data
    for line in csv_data:
        x.append(line['x'])
        y.append(line['y_train'])

    # Convert into Numpy Array
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)

    # n-order fitting
    res1=np.polyfit(x, y, 1)
    res2=np.polyfit(x, y, 2)
    res3=np.polyfit(x, y, 3)
    res4=np.polyfit(x, y, 4)
    res5=np.polyfit(x, y, 5)

    x_fitting = np.linspace(min(x), max(x))
    y1 = np.poly1d(res1)(x_fitting)
    y2 = np.poly1d(res2)(x_fitting)
    y3 = np.poly1d(res3)(x_fitting)
    y4 = np.poly1d(res4)(x_fitting)
    y5 = np.poly1d(res5)(x_fitting)

    # Get Error
    err1 = np.sum(( np.poly1d(res1)(x) - y )**2)
    err2 = np.sum(( np.poly1d(res2)(x) - y )**2)
    err3 = np.sum(( np.poly1d(res3)(x) - y )**2)
    err4 = np.sum(( np.poly1d(res4)(x) - y )**2)
    err5 = np.sum(( np.poly1d(res5)(x) - y )**2)

    print("data2 Errors:")
    print("\t1st: {:.3f}".format(err1))
    print("\t2nd: {:.3f}".format(err2))
    print("\t3rd: {:.3f}".format(err3))
    print("\t4th: {:.3f}".format(err4))
    print("\t5th: {:.3f}".format(err5))
    print()

    # Plot Data
    plt.scatter(x, y, color = 'b')

    # Draw Fit Line
    plt.plot(x_fitting, y1, label='1st')
    plt.plot(x_fitting, y2, label='2nd')
    plt.plot(x_fitting, y3, label='3rd')
    plt.plot(x_fitting, y4, label='4th')
    plt.plot(x_fitting, y5, label='5th')

    plt.title('data2')
    plt.legend()
    plt.show()


    # Open CSV File for data3
    csv_file = open('./assets/data3.csv', 'r', encoding='utf8');
    csv_data = csv.DictReader(csv_file)

    x = []
    y = []

    # Read All Line from CSV Data
    for line in csv_data:
        x.append(line['x'])
        y.append(line['y_test'])

    # Convert into Numpy Array
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)

    x_fitting = np.linspace(min(x), max(x))
    y1 = np.poly1d(res1)(x_fitting)
    y2 = np.poly1d(res2)(x_fitting)
    y3 = np.poly1d(res3)(x_fitting)
    y4 = np.poly1d(res4)(x_fitting)
    y5 = np.poly1d(res5)(x_fitting)

    # Get Error
    err1 = np.sum(( np.poly1d(res1)(x) - y )**2)
    err2 = np.sum(( np.poly1d(res2)(x) - y )**2)
    err3 = np.sum(( np.poly1d(res3)(x) - y )**2)
    err4 = np.sum(( np.poly1d(res4)(x) - y )**2)
    err5 = np.sum(( np.poly1d(res5)(x) - y )**2)

    print("data3 Errors:")
    print("\t1st: {:.3f}".format(err1))
    print("\t2nd: {:.3f}".format(err2))
    print("\t3rd: {:.3f}".format(err3))
    print("\t4th: {:.3f}".format(err4))
    print("\t5th: {:.3f}".format(err5))
    print()

    # Plot Data
    plt.scatter(x, y, color = 'b')

    # Draw Fit Line
    plt.plot(x_fitting, y1, label='1st')
    plt.plot(x_fitting, y2, label='2nd')
    plt.plot(x_fitting, y3, label='3rd')
    plt.plot(x_fitting, y4, label='4th')
    plt.plot(x_fitting, y5, label='5th')

    plt.title('data3')
    plt.legend()
    plt.show()
