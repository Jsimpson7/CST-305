# Joshua Simpson
# CST 305 – Project 2: Comparing Runge-Kutta Method vs SciPy's ODE Solver
# This project solves the differential equation: dy/dx = -y + ln(x)

# Import required libraries
import math
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# ---------------------- Runge-Kutta Method Implementation ----------------------
class Runge:

    # Counter to track how many computation steps Runge-Kutta takes
    runge_steps = 0

    # Define the differential equation: dy/dx = -y + ln(x)
    def diffEq(y, x):
        return -y + math.log(x)

    # Implement the Runge-Kutta 4th-order method
    def rungeKutta(x0, y0, h):
        k1 = Runge.diffEq(y0, x0)
        Runge.runge_steps += 1

        k2 = Runge.diffEq(y0 + (h / 2) * k1, x0 + (h / 2))
        Runge.runge_steps += 2

        k3 = Runge.diffEq(y0 + (h / 2) * k2, x0 + (h / 2))
        Runge.runge_steps += 2

        k4 = Runge.diffEq(y0 + h * k3, x0 + h)
        Runge.runge_steps += 2

        t4 = (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        Runge.runge_steps += 5

        y1 = y0 + h * t4
        Runge.runge_steps += 2

        x1 = x0 + h
        Runge.runge_steps += 1

        return (x1, y1)

    # Runs the RK4 method for 'runs' number of steps
    def runCode(x_values, y_values, h, runs):
        for i in range(runs):
            x1, y1 = Runge.rungeKutta(x_values[i], y_values[i], h)
            x_values.append(x1)
            y_values.append(y1)

    # Prints the computed x and y values (optional)
    def printResults(x_values, y_values, runs):
        for i in range(runs + 1):
            print(f"x{i} = {round(x_values[i], 4)}, \ty{i} = {round(y_values[i], 4)}")


# -------------------------- SciPy's ODE Method --------------------------------
class ODE:

    # Counter to track computation steps used by odeint
    ode_steps = 0

    # Define the same differential equation
    def diffEq(y, x):
        return -y + math.log(x)

    # Use odeint to solve the equation
    def runCode(x0, y0, h, runs):
        x_values = np.linspace(x0, x0 + h * runs, runs + 1)
        y_values = odeint(ODE.diffEq, y0, x_values)
        ODE.ode_steps += len(x_values)
        return x_values, y_values

    # Print results (optional)
    def printResults(x_values, y_values):
        for i, (x, y) in enumerate(zip(x_values, y_values)):
            print(f"x{i} = {round(x, 4)}, \ty{i} = {round(y[0], 4)}")


# ------------------------ Initial Setup & Parameters -------------------------
x0 = 2.0      # initial x value
y0 = 1.0      # initial y value
h = 0.3       # step size
runs = 1000   # how many steps to compute

# Initialize value lists for Runge-Kutta
x_values = [x0]
y_values = [y0]

# ----------------------- Run both methods & time them ------------------------
runge_start_time = time.time()
Runge.runCode(x_values, y_values, h, runs)
runge_end_time = time.time()

ode_start_time = time.time()
x_valuesODE, y_valuesODE = ODE.runCode(x0, y0, h, runs)
ode_end_time = time.time()

# --------------------- Timing Comparison Output ------------------------------
runge_elapsed_time = runge_end_time - runge_start_time
ode_elapsed_time = ode_end_time - ode_start_time

print("\nRunge-Kutta Elapsed Time: \t", runge_elapsed_time, "seconds")
print("ODE Elapsed Time: \t\t\t", ode_elapsed_time, "seconds")

if ode_elapsed_time > runge_elapsed_time:
    print("Runge-Kutta is faster by:", ode_elapsed_time - runge_elapsed_time, "seconds")
elif runge_elapsed_time > ode_elapsed_time:
    print("ODE is faster by:", runge_elapsed_time - ode_elapsed_time, "seconds")
else:
    print("Both methods took the same amount of time.")

# --------------------- Computational Step Count Output -----------------------
print("\nRunge-Kutta Computational Step Count: \t", Runge.runge_steps, "steps")
print("ODE Computational Step Count: \t\t\t", ODE.ode_steps, "steps")

# -------------------------- Graphing Results ----------------------------------
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Runge-Kutta graph
axs[0].plot(x_values, y_values, linestyle="-", color="darkorange", label="Runge-Kutta")

# ODE graph
axs[1].plot(x_valuesODE, y_valuesODE, linestyle=(0, (10, 15)), color="blue", label="ODE")

# Comparison graph
axs[2].plot(x_values, y_values, linestyle="-", color="darkorange", label="Runge-Kutta")
axs[2].plot(x_valuesODE, y_valuesODE, linestyle=(0, (10, 15)), color="blue", label="ODE")

# Label all graphs
for ax in axs:
    ax.set_xlabel("X Vals")
    ax.set_ylabel("Y Vals")
    ax.grid(True)
    ax.legend()

# Give each graph a title
axs[0].set_title("Runge-Kutta")
axs[1].set_title("ODE (odeint)")
axs[2].set_title("Runge-Kutta vs ODE")

# Layout adjustment
plt.tight_layout()
plt.show()
