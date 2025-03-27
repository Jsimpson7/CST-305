# Joshua Simpson
# CST 305 – Project 5: Lorenz Attractor Simulation
# This project visualizes the Lorenz Attractor using numerical integration.
# It shows chaotic motion in 3D space and time series plots for each variable.

# ---------------------- Import Required Libraries ----------------------
import numpy as np                  # For numerical arrays and calculations
import matplotlib.pyplot as plt     # For plotting graphs (2D & 3D)
# -----------------------------------------------------------------------


# ------------------------ Lorenz Function ------------------------------
# Calculates the derivatives for the Lorenz system at each step
def lorenz(x, y, z, r, s=10, b=2.667):
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot
# -----------------------------------------------------------------------


# ------------------------ Run Simulation -------------------------------
# Solves and plots the Lorenz attractor for a given r value
def runCode(r):
    dt = 0.01         # Time step size
    num_steps = 10000 # Number of time steps (total simulation time = 100s)

    # Initialize arrays to store x, y, z values
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)

    # Initial conditions
    xs[0], ys[0], zs[0] = 7.5, 22.5, 35

    # Compute values using Euler’s method
    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], r)
        xs[i + 1] = xs[i] + x_dot * dt
        ys[i + 1] = ys[i] + y_dot * dt
        zs[i + 1] = zs[i] + z_dot * dt

    # ---------------------- Plot 3D Graph -----------------------
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, lw=0.5)
    ax.set_title(f"Lorenz Attractor: r = {r}")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")

    # ------------------ Plot Time Series Graphs ----------------
    fig, (ax_x, ax_y, ax_z) = plt.subplots(3, 1, figsize=(8, 12))
    time = np.arange(0, num_steps + 1) * dt

    ax_x.plot(time, xs, color='blue')
    ax_x.set_ylabel("X: txt")
    ax_x.set_title(f"Lorenz Time Series: r = {r}")
    ax_x.set_xlim(-1, 100)

    ax_y.plot(time, ys, color='orange')
    ax_y.set_ylabel("Y: rtf")
    ax_y.set_xlim(-1, 100)

    ax_z.plot(time, zs, color='green')
    ax_z.set_xlabel("t - Time")
    ax_z.set_ylabel("Z: docx")
    ax_z.set_xlim(-1, 100)

    # Layout and show both figures
    plt.tight_layout()
    plt.show()
# -----------------------------------------------------------------------


# ---------------------- Input and Program Start ------------------------
def start():
    try:
        r = int(input("Enter a value for 'r' (enter 0 to stop): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        start()
    except KeyboardInterrupt:
        print()  # Graceful exit if user presses Ctrl+C
    else:
        if r != 0:
            runCode(r)
            start()  # Loop again for new input
# -----------------------------------------------------------------------


# ---------------------------- Run Program ------------------------------
start()
# -----------------------------------------------------------------------
