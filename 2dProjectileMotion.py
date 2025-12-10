import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation

gravity = -9.81
timestep = 0.02

class Projectile:
    def __init__(self, velocity, angle):
        self.velocity = velocity
        self.angle = math.radians(angle)

        # velocity components
        self.xv = self.velocity * math.cos(self.angle)
        self.yv = self.velocity * math.sin(self.angle)

        # position list
        self.position = [[0, 0]]

    def move(self):
        x = self.position[-1][0] + self.xv * timestep
        y = self.position[-1][1] + self.yv * timestep
        self.position.append([x, y])

    def apply_gravity(self):
        self.yv += gravity * timestep


p1 = Projectile(22, 43)

fig, ax = plt.subplots()
ax.set_xlim(0, 60)
ax.set_ylim(0, 30)

line, = ax.plot([], [], 'r-')

def init():
    line.set_data([], [])
    return line,

def update(frame):
    if p1.position[-1][1] < 0:
        return line

    p1.move()
    p1.apply_gravity()

    Xlist = [pos[0] for pos in p1.position]
    Ylist = [pos[1] for pos in p1.position]

    line.set_data(Xlist, Ylist)
    return line,


ani = FuncAnimation(fig, update, frames=1, init_func=init,
                    blit=True, interval=5, repeat = True)

plt.show()
