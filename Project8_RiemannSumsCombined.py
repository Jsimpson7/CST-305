# Joshua Simpson
# CST 305 – Project 8: Riemann Sums & Approximations
# Sections:
# - 1A: Plotting Left, Mid, Right Rectangles
# - 1B: Symbolic Riemann Sum for f(x) = 3x + 2x²
# - 1C: Symbolic Riemann Sums for ln(x) and x² - x³
# - 2: Real Data + Interpolation + Trapezoidal Riemann Sum

# -------------------- Imports --------------------
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.interpolate import interp1d
# -------------------------------------------------

# -------------------- Part 1A --------------------
# Plotting Left, Midpoint, and Right Riemann rectangles

def function(x):
    return np.sin(x) + 1

t = np.linspace(-5, 5, 1000)
y = function(t)
x_start = -np.pi
x_end = np.pi
n_rectangles = 4
rectangle_width = (x_end - x_start) / n_rectangles

# LEFT
plt.plot(t, y, label='f(x) = sin(x) + 1')
plt.axvline(x=x_start, color='r', linestyle='--', label=f'x={x_start}')
plt.axvline(x=x_end, color='r', linestyle='--', label=f'x={x_end}')
for i in range(n_rectangles):
    x_rect = x_start + i * rectangle_width
    y_rect = function(x_rect)
    plt.fill_between([x_rect, x_rect + rectangle_width], 0, [y_rect, y_rect], alpha=0.2, color='purple')
plt.title(f'Left Endpoint Approximation')
plt.xlabel('x'); plt.ylabel('f(x)'); plt.legend(); plt.grid(); plt.show()

# MIDPOINT
plt.plot(t, y, label='f(x) = sin(x) + 1')
plt.axvline(x=x_start, color='r', linestyle='--', label=f'x={x_start}')
plt.axvline(x=x_end, color='r', linestyle='--', label=f'x={x_end}')
for i in range(n_rectangles):
    x_rect = x_start + i * rectangle_width
    y_rect = function(x_rect + rectangle_width/2)
    plt.fill_between([x_rect, x_rect + rectangle_width], 0, [y_rect, y_rect], alpha=0.2, color='purple')
plt.title(f'Midpoint Approximation')
plt.xlabel('x'); plt.ylabel('f(x)'); plt.legend(); plt.grid(); plt.show()

# RIGHT
plt.plot(t, y, label='f(x) = sin(x) + 1')
plt.axvline(x=x_start, color='r', linestyle='--', label=f'x={x_start}')
plt.axvline(x=x_end, color='r', linestyle='--', label=f'x={x_end}')
for i in range(n_rectangles):
    x_rect = x_start + i * rectangle_width
    y_rect = function(x_rect + rectangle_width)
    plt.fill_between([x_rect, x_rect + rectangle_width], 0, [y_rect, y_rect], alpha=0.2, color='purple')
plt.title(f'Right Endpoint Approximation')
plt.xlabel('x'); plt.ylabel('f(x)'); plt.legend(); plt.grid(); plt.show()

# -------------------- Part 1B --------------------
x = sp.symbols('x')
f = 3*x + 2*x**2
a, b = 0, 1
n, k = sp.symbols('n k')
delta_x = (b - a) / n
c_k = a + (k * delta_x)
riemann_sum = sp.summation(f.subs(x, c_k) * delta_x, (k, 1, n))
limit_riemann_sum = sp.limit(riemann_sum, n, sp.oo)
print("\n--- Part 1B ---")
print(f"Riemann Sum Formula: {riemann_sum}")
print(f"Limit as n -> infinity: {limit_riemann_sum}")

# ------------------ Part 1C-1 ---------------------
f = sp.log(x)
a = 1
b = sp.E
delta_x = (b - a) / n
c_k = a + (k * delta_x)
riemann_sum = sp.summation(f.subs(x, c_k) * delta_x, (k, 1, n))
print("\n--- Part 1C-1 ---")
print(f"Riemann Sum Formula: {riemann_sum}")

# ------------------ Part 1C-2 ---------------------
f = x**2 - x**3
a = -1
b = 0
delta_x = (b - a) / n
c_k = a + (k * delta_x)
riemann_sum = sp.summation(f.subs(x, c_k) * delta_x, (k, 1, n))
limit_riemann_sum = sp.limit(riemann_sum, n, sp.oo)
print("\n--- Part 1C-2 ---")
print(f"Riemann Sum Formula: {riemann_sum}")
print(f"Limit as n -> infinity: {limit_riemann_sum}")

# -------------------- Part 2 ----------------------
time_data = np.arange(1, 31)
download_rate_data = np.array([
    0.509, 0.324, 0.745, 0.420, 0.419,
    0.420, 0.420, 0.419, 0.420, 0.419,
    0.420, 0.417, 0.694, 0.833, 0.405,
    0.416, 0.420, 0.710, 0.870, 0.418,
    0.452, 0.372, 0.822, 0.806, 0.670,
    0.840, 0.694, 0.773, 0.758, 0.747
])

interpolation_function = interp1d(time_data, download_rate_data, kind='linear', fill_value='extrapolate')
time_values = np.linspace(0, 30, 1000)
download_rate_values = interpolation_function(time_values)

riemann_sum = np.trapezoid(download_rate_values, time_values)
print("\n--- Part 2 ---")
print(f"Riemann Sum (Trapezoidal Rule on Interpolated Data): {riemann_sum}")
