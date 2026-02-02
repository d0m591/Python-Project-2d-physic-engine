import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button

gravity = -9.81
timestep = 0.01

class Projectile:
    def __init__(self, velocity, angle, gravity):
        self.velocity = velocity
        self.angle = math.radians(angle)
        self.gravity = gravity
        self.xv = self.velocity * math.cos(self.angle)
        self.yv = self.velocity * math.sin(self.angle)
        self.position = [[0, 0]]
        self.is_airborne = True

    def move(self):
        if self.is_airborne:
            x = self.position[-1][0] + self.xv * timestep
            y = self.position[-1][1] + self.yv * timestep
            if y < 0:
                y = 0
                self.is_airborne = False
            self.position.append([x, y])

    def apply_gravity(self):
        if self.is_airborne:
            self.yv += self.gravity * timestep

    def discover(self):
        timetaken = (-(self.yv) / gravity) * 2
        t_peak = timetaken * 1 / 2
        maxY = (self.yv * t_peak + 1 / 2 * gravity * (t_peak ** 2))
        maxX = (self.xv * timetaken)
        return maxX * 1.1 , maxY * 1.1       # I multiply each value to give a buffer so it doesnt go off screen

p1 = Projectile(22, 43, -9.81)

#discovering x-limits and y-limtits



maxX, maxY = p1.discover()

#Ui
fig, ax = plt.subplots(figsize=(10, 7))
fig.subplots_adjust(bottom=0.25) #Makes 25% of the bottom of the screen for sliders to customise
ax.set_xlim(0, maxX)
ax.set_ylim(0, maxY)


ax.set_title('Projectile Motion')
ax.set_xlabel('Height [m]')
ax.set_ylabel('Distance [m]')




line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    p1.move()
    p1.apply_gravity()

    Xlist = [pos[0] for pos in p1.position]
    Ylist = [pos[1] for pos in p1.position]

    line.set_data(Xlist, Ylist)
    return line,


ani = FuncAnimation(fig, update, init_func=init,blit=True, interval=5, repeat=True, frames=1)


plt.show()
