#!python3
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

if __name__ == "__main__":
    # Parameters
    l = 20.0 # mm
    T_init = 300.0 # K
    T_heat = 500.0 # K
    T_left = 300.0 # K
    T_right = 300.0 # K
    alpha = 1.0 # mm^2 / s
    dt = 0.1 # s
    dx = 1.0 # mm
    t_stop = 5.0 # s

    # Initial Conditions
    t_list = np.arange(0.0, t_stop+dt, dt)
    x_list = np.arange(0.0, l+dx, dx)
    T_list = np.full(len(x_list), T_init)
    T_list[int(len(T_list)/2)] = T_heat

    fig = plt.figure()
    fig_list = []

    for t in t_list:
        T_next = np.copy(T_list)
        for x in range(len(x_list)):
            # B.C. Left
            if x == 0:
                T_next[x] = T_left
            # B.C. Right
            elif x == len(x_list) - 1:
                T_next[x] = T_right
            # Heat Equation
            else:
                T_next[x] = T_list[x] + alpha * dt / dx**2 * (T_list[x+1] - 2.0 * T_list[x] + T_list[x-1])

        # Set fot Animation
        plot = plt.plot(x_list, T_list)
        fig_list.append(plot)

        # Swap
        T_list = T_next


    # Figure Setup
    plt.title('1 Dim. Heat Equation')
    plt.ylabel('Tempelature [K]')
    plt.xlabel('Position [mm]')
    plt.grid()

    anime = animation.ArtistAnimation(fig, fig_list, interval=1000)
    plt.show()
