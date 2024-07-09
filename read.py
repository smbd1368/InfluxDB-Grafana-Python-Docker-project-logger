import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Open the file and read the data
with open("data.txt", "r") as file:
    lines = file.readlines()

# Initialize lists to store the data
x = []
y = []
z = [] 

# Parse the data from the file
for line in lines:
    values = [float(v) for v in line.strip().split(",")]
    x.append(values[0])
    y.append(values[1])
    z.append(values[2])

# Initialize the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the update function
def update(frame):
    global x, y, z
    ax.clear()
    ax.set_xlim(min(x), max(x))
    ax.set_ylim(min(y), max(y))
    ax.set_zlim(min(z), max(z))
    ax.scatter3D(x[frame:frame+10], y[frame:frame+10], z[frame:frame+10], c='r')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(x)//10, blit=False, interval=.01)

# Show the plot
plt.show()
