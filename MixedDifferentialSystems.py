# Joshua Simpson
# CST 305 – Project 6: Mixed Differential Systems
# This project includes:
# - Part 1a: Plotting an analytical solution to a nonlinear DE
# - Part 1b: Plotting another DE's analytical solution
# - Part 2: Recursively calculating series coefficients using fractions
# - Part 3: Newton's Law of Cooling using odeint

# ------------------ Import Required Libraries ------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from fractions import Fraction
# ---------------------------------------------------------------


# ------------------ Part 1a: Polynomial Solution ------------------
# Define the analytical solution to a differential equation
def part1a(x):
    return 1 - x - (1/3) * x**3 - (1/12) * x**4

# Create x values from 0 to 5
x_values = np.linspace(0, 5, 100)
y_values = part1a(x_values)

# Plot the function
plt.plot(x_values, y_values, label='y\" - 2xy\' + x^2y')
plt.title('Part 1a')

# Plot a vertical line at x = 3.5
plt.plot([3.5, 3.5], [-100, part1a(3.5)], 'r--', label='x = 3.5')
# Plot a horizontal line at y(3.5)
plt.plot([0, 3.5], [part1a(3.5), part1a(3.5)], 'g--', label='y = -29.297')

plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0, 5)
plt.ylim(-100, 10)
plt.grid(True)
plt.legend()
plt.show()
# ---------------------------------------------------------------


# ------------------ Part 1b: Quadratic Solution -----------------
def part1b(x):
    return 6 + (x - 3) - (11/2) * ((x - 3)**2)

x_values = np.linspace(0, 5, 100)
y_values = part1b(x_values)

plt.plot(x_values, y_values, label='y\" - (x - 2)y\' + 2y')
plt.title('Part 1b')

# Plot vertical line at x = 3, horizontal line at y = 6
plt.plot([3, 3], [-50, part1b(3)], 'r--', label='x = 3')
plt.plot([0, 3], [part1b(3), part1b(3)], 'g--', label='y = 6')

plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0, 5)
plt.ylim(-50, 10)
plt.grid(True)
plt.legend()
plt.show()
# ---------------------------------------------------------------


# ---------------- Part 2: Series Coefficient Generator ----------
def part2(n):
    a_values = [Fraction(0) for _ in range(n + 2)]
    a_values[0] = Fraction(1)
    a_values[1] = Fraction(1)

    for i in range(2, n + 2):
        factor = -((i - 2) * (i - 3) + 1) * Fraction(1, 4 * i * (i - 1))
        a_values[i] = factor * a_values[i - 2]

    return a_values[2:]

# Calculate the coefficients for n=8
a_values = part2(8)

# Print the results
def printAVals():
    for i, a in enumerate(a_values, start=2):
        tag = 'a0' if i % 2 == 0 else 'a1'
        print(f'a_{i} = {a} {tag}')

printAVals()

# Plot coefficients vs. index
plt.plot(range(len(a_values)), [float(a) for a in a_values], marker='o')
plt.title('Series Coefficients a(n+2)')
plt.xlabel('n')
plt.ylabel('a(n+2)')
plt.grid(True)
plt.show()
# ---------------------------------------------------------------


# ---------------- Part 3: Newton’s Law of Cooling ---------------
def part3(T, t, k, s):
    return -k * (T - s)

# Parameters
k = 0.5         # Cooling rate constant
T = 80          # Initial temperature
s = [50, 60, 70, 80, 90]  # Different ambient temperatures
t = np.linspace(0, 10)    # Time array from 0 to 10

# Solve and plot for each surrounding temp
for temp in s:
    solution = odeint(part3, T, t, args=(k, temp))
    plt.plot(t, solution, label=f"Surrounding Temp: {temp}")

plt.xlabel('Time (Seconds)')
plt.ylabel('Temperature (Celsius)')
plt.title("Computer Cooling (Newton's Law)")
plt.legend()
plt.grid(True)
plt.show()
# ---------------------------------------------------------------
