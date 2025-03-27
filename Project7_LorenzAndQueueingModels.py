# Joshua Simpson
# CST 305 – Project 7: Lorenz System and Queueing Models
# This file includes:
# - Part 1: Lorenz Attractor Visualization
# - Part 2: Single-server queue simulation
# - Part 3: System performance metrics and scaling analysis

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

# ---------------------- Part 1: Lorenz Attractor ----------------------
def lorenz(x, y, z, r, s=10, b=2.667):
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot

def runCode(r):
    dt = 0.01
    num_steps = 10000
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)
    xs[0], ys[0], zs[0] = (7.5, 22.5, 35)

    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], r)
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, lw=0.5)
    ax.set_title(f"Lorenz Attractor: r = {r}")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")

    fig, (ax_x, ax_y, ax_z) = plt.subplots(3, 1, figsize=(8, 12))
    time = np.arange(0, num_steps + 1) * dt

    ax_x.plot(time, xs)
    ax_x.set_ylabel("X: txt")
    ax_x.set_title(f"Lorenz Attractor Components: r = {r}")
    ax_x.set_xlim(-1, 100)

    ax_y.plot(time, ys)
    ax_y.set_ylabel("Y: rtf")
    ax_y.set_xlim(-1, 100)

    ax_z.plot(time, zs)
    ax_z.set_xlabel("t - Time")
    ax_z.set_ylabel("Z: docx")
    ax_z.set_xlim(-1, 100)

    plt.tight_layout()
    plt.show()

def start():
    try:
        r = int(input("Enter a value for 'r' (0 to skip Part 1): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        start()
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        if r != 0:
            runCode(r)
start()

# ---------------------- Part 2: Queue Simulation ----------------------
arrival_times = list(range(1, 16))
service_durations = [2.22, 1.76, 2.13, 0.14, 0.76, 0.7, 0.47, 0.22, 0.18, 2.41, 0.41, 0.46, 1.37, 0.27, 0.27]

exit_times = []
service_start_times = []
time_in_queue = []
system_customers = [0, 1, 2, 2, 2, 3, 4, 3, 2, 0, 1, 2, 1, 1, 0]
queue_customers = [0, 0, 1, 1, 1, 2, 3, 2, 1, 0, 0, 1, 0, 0, 0]

current_time = 0
for arrival, service in zip(arrival_times, service_durations):
    service_start = max(current_time, arrival)
    service_start_times.append(service_start)
    exit_time = service_start + service
    exit_times.append(exit_time)
    time_in_queue.append(service_start - arrival)
    current_time = exit_time

L_q = sum(time_in_queue) / current_time
L_q_A = sum(queue_customers) / len(queue_customers)

print("\n--- Part 2 ---")
print("L_q: " + str(L_q))
print("L_q^((A)): " + str(L_q_A))

plt.figure(figsize=(10, 5))
plt.subplot(321)
plt.plot(arrival_times, service_start_times)
plt.title('Arrival Time vs. Service Start Time')

plt.subplot(322)
plt.plot(arrival_times, exit_times)
plt.title('Arrival Time vs. Exit Time')

plt.subplot(323)
plt.plot(arrival_times, time_in_queue)
plt.title('Arrival Time vs. Time in Queue')

plt.subplot(324)
plt.plot(arrival_times, system_customers)
plt.title('Arrival Time vs. Customers in System')

plt.subplot(325)
plt.plot(arrival_times, queue_customers)
plt.title('Arrival Time vs. Customers in Queue')

plt.tight_layout()
plt.show()

input("\nPress Enter to continue to Part 3 (System Metrics Scaling)...")

# ---------------------- Part 3: System Metrics Scaling ----------------------
k = np.linspace(1, 1000)
theta = 10
mu = 5

p = (k * theta) / (k * mu)
estimated_wait = p * (1 / (k * mu)) / (1 - p)
estimated_service = (1 / (k * mu)) / (1 - p)
estimated_number = p / (1 - p)
estimated_time = estimated_service + estimated_wait
X = estimated_number / estimated_time

plt.figure(figsize=(10, 15))
plt.subplot(221)
plt.plot(k, p, label='Utilization (p)')
plt.title('Utilization vs. k')
plt.xlabel('k')
plt.ylabel('Utilization (p)')
plt.legend()

plt.subplot(222)
plt.plot(k, X, label='Throughput (X)')
plt.title('Throughput vs. k')
plt.xlabel('k')
plt.ylabel('Throughput (X)')
plt.legend()

plt.subplot(223)
plt.plot(k, estimated_number, label='E[N]')
plt.title('Mean Number in System vs. k')
plt.xlabel('k')
plt.ylabel('E[N]')
plt.legend()

plt.subplot(224)
plt.plot(k, estimated_time, label='E[T]')
plt.title('Mean Time in System vs. k')
plt.xlabel('k')
plt.ylabel('E[T]')
plt.legend()

plt.tight_layout()
plt.show()
