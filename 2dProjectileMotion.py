import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button as wid

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

        self.initialyv = self.yv

        #with no air resistance
        self.t_peak = -self.initialyv / self.gravity # works when gravity is negative
        self.timetaken = 2 * self.t_peak





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
        maxY = (self.initialyv * self.t_peak + 1 / 2 * self.gravity * (self.t_peak ** 2))
        maxX = (self.xv * self.timetaken)
        return maxX * 1.1 , maxY * 1.1       # I multiply each value to give a buffer so it doesnt go off screen

p1 = Projectile(25, 45, -9.81)

#discovering x-limits and y-limtits
maxX, maxY = p1.discover()

#Ui
fig, ax = plt.subplots(figsize=(10, 7))
fig.subplots_adjust(bottom=0.25) #Makes 25% of the bottom of the screen for sliders to customise
ax.set_xlim(0, maxX)
ax.set_ylim(0, maxY)

ax.set_title('Projectile Motion')
ax.set_xlabel('Distance [m]')
ax.set_ylabel('Height [m]')


line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    Xlist = [pos[0] for pos in p1.position]
    Ylist = [pos[1] for pos in p1.position]
    line.set_data(Xlist, Ylist)
    p1.apply_gravity()
    p1.move()
    return line,

#text
props = dict(boxstyle='round', facecolor='wheat', alpha =0.5)
textstr = (f"t_flight = {p1.timetaken:.2f}"
           '\n'
           f"t_peak = {p1.t_peak:.2f}")

ax.text(0.05,0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)


#button

#slider section
ax_velocity = plt.axes([0.15,0.1,0.65,0.03])
ax_angle = plt.axes([0.15,0.05,0.65,0.03])

s_velocity = Slider(ax_velocity, "Velocity", 0, 50, valinit=25)
s_angle = Slider(ax_angle, "Angle", 0, 90, valinit=45)


ani = FuncAnimation(fig, update, init_func=init, blit=True, interval=20)


plt.show()
