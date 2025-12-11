from functools import total_ordering

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


p1 = Projectile(100, 15)

#Total time
totalTime = (2 * p1.yv) / -gravity
totalDistance = (p1.xv * totalTime)
totalHeight = (p1.yv * totalTime) + 0.5 * (-gravity * totalTime * totalTime)

fig, ax = plt.subplots()


line, = ax.plot([], [], 'r-')

def init():
    line.set_data([], [])

    ax.set_xlim([0, totalDistance])
    ax.set_ylim([0, totalHeight])
    return line,

blit = True
def update(Frame):
    # predict next y before moving
    next_y = p1.position[-1][1] + p1.yv * timestep

    # if next step would fall below ground, freeze at exactly y=0
    if next_y < 0:

        p1.position.append([p1.position[-1][0] + p1.xv * timestep, 0])

        Xlist = [pos[0] for pos in p1.position]
        Ylist = [pos[1] for pos in p1.position]

        line.set_data(Xlist, Ylist)

        ani.event_source.stop()
        return line,

    p1.move()
    p1.apply_gravity()

    Xlist = [pos[0] for pos in p1.position]
    Ylist = [pos[1] for pos in p1.position]

    line.set_data(Xlist, Ylist)
    return line,


ani = FuncAnimation(fig,
                    update,
                    frames=1,
                    init_func=init,
                    blit=False,
                    interval=1)

plt.show()
