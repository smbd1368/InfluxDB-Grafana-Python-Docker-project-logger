import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import numpy as np
import time
import random
# Set up the figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initialize the x, y, and z lists
x = []
y = []
z = []

# Initialize the list of timestamps
timestamps = []

# Set up the plot
line, = ax.plot([], [], [], 'o')

# Set the limits of the plot
ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000)
ax.set_zlim(0, 1000)

# Set the maximum number of data points to display
max_points = 1000

# Define the update function
def update(frame):
    global x, y, z, timestamps

    # Generate random data
    x.append(frame)
    y.append(random.randint(1,1000))
    z.append(random.randint(1,1000))

    # Add the timestamp to the list
    timestamps.append(time.time())

    # Remove the oldest data points if the maximum is reached
    if len(x) > max_points:
        x.pop(0)
        y.pop(0)
        z.pop(0)
        timestamps.pop(0)

    # Remove data points that are older than 2 seconds
    for i in range(len(timestamps)):
        if timestamps[i] < time.time() - 2:
            x.pop(i)
            y.pop(i)
            z.pop(i)
            timestamps.pop(i)

            break
    # ax.scatter(x, y, z, c='r', marker='o')

    # Add the Doppler label
    


    # Clear the plot
    line.set_data(x, y)
    line.set_3d_properties(z)
    # ax.text(0, 0, 0, '', size=12, zorder=1, ha="center")
    # ax.text(str(x[0]), size=17, zorder=1, ha="center")
    # ax.scatter(x, y, z, c='r', marker='o')

    # Add the Doppler label
    # ax.text(0, 0, 0, f'x: {x[-1]}, y: {y[-1]}, z: {z[-1]}', size=20, zorder=1, ha="center")

    # Return the updated plot
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=1000, blit=True, interval=1000)

# Show the plot
plt.show()
