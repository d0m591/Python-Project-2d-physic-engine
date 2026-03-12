import matplotlib.pyplot as plt
import math
from tkinter import messagebox
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button


timestep = 0.01
air_resistance = False
Cd = 0.47          #drag coefficient (sphere)
rho = 1.225        #air density
A = 0.01           #cross sectional area
mass = 1.0         #mass

def showInfo(event):
    info = (
        f"Time of flight: {p1.timeElapsed:.2f} s\n"
        f"Range: {p1.position[-1][0]:.2f} m\n"
        f"Maximum height: {p1.MaxHeight:.2f} m\n"
        f"Current velocity: {math.hypot(p1.xv, p1.yv):.2f} m/s\n"
        f"Gravity: {p1.gravity:.2f} m/s²\n"
        f"Air resistance: {'ON' if air_resistance else 'OFF'}"
    )

    messagebox.showinfo("Projectile Data", info)

def changestr():
    if air_resistance:
        bairRes.label.set_text(f'Air Resistance \nON')
    else:
        bairRes.label.set_text('Air Resistance \nOFF')
    fig.canvas.draw_idle()

def reset(val):
    global p1

    velocity = s_velocity.val
    angle = s_angle.val
    gravity = -s_gravity.val

    p1 = Projectile(velocity,angle,gravity)

    #Update Previous hard coded elements
    maxX,maxY = p1.discover()
    ax.set_xlim(0,maxX)
    ax.set_ylim(0,maxY)

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
        self.initialxv = self.xv
        #with no air resistance
        self.tpeak = -self.initialyv / self.gravity # works when gravity is negative
        self.timetaken = 2 * self.tpeak
        self.dtravelled = self.initialxv * self.timetaken
        self.mheight = self.initialyv * self.tpeak + 0.5 * self.gravity * self.tpeak **2

        self.timeElapsed = 0
        self.MaxHeight = 0
        self.MaxDistance = 0

    def move(self):
        if self.is_airborne:
            x = self.position[-1][0] + self.xv * timestep
            y = self.position[-1][1] + self.yv * timestep

            self.timeElapsed += timestep

            if y > self.MaxHeight:
                self.MaxHeight = y

            if y <= 0:
                self.MaxDistance = x
                self.is_airborne = False

            self.position.append([x, y])

    def apply_forces(self):
        if self.angle == 90:
            self.xv = 0

        if self.is_airborne:

            if air_resistance:
                drag = (0.5 * Cd * rho * A * current_v ** 2) / mass #Drag force magnitude

                #Direction opposite velocity
                ax_drag = -drag * (self.xv / current_v)
                ay_drag = -drag * (self.yv / current_v)

                #Total acceleration
                ax = ax_drag
                ay = self.gravity + ay_drag
            else:
                ax = 0
                ay = self.gravity

            # Update velocities (Euler step)
            self.xv += ax * timestep
            self.yv += ay * timestep

    def discover(self):
        maxY = (self.initialyv * self.tpeak + 1 / 2 * self.gravity * (self.tpeak ** 2))
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

def airRes(val):
    global air_resistance

    air_resistance = not air_resistance
    reset(val)
    changestr()

def init():
    line.set_data([], [])
    return line,

def update(frame):
    global current_v

    p1.apply_forces()
    p1.move()

    Xlist = [pos[0] for pos in p1.position]
    Ylist = [pos[1] for pos in p1.position]
    line.set_data(Xlist, Ylist)

    #fetches particles current pos
    current_x, current_y = p1.position[-1]
    current_v = math.sqrt(p1.xv **2 + p1.yv **2)

    position_text.set_text(
        f"x = {current_x:.2f} m\n"
        f"y = {current_y:.2f} m\n"
        f"velocity = {current_v:.2f} m/s\n"
        f"time = {p1.timeElapsed:.2f} /s"
    )

    return line, position_text

#text
props = dict(boxstyle='round', facecolor='wheat', alpha =0.5)

position_text = ax.text(
    0.05, 0.95, "",
    transform=ax.transAxes,
    fontsize=12,
    verticalalignment='top',
    bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5)
)

#buttons
ax_stat = plt.axes([0.85, 0.9, 0.1, 0.05])
bstat = Button(ax_stat, 'Stats')
bstat.on_clicked(showInfo)

ax_airRes = plt.axes([0.85, 0.05, 0.1, 0.075])
bairRes = Button(ax_airRes, 'Air Resistance OFF')
bairRes.on_clicked(airRes)
#slider section
ax_velocity = plt.axes([0.15,0.1,0.65,0.03])
ax_angle = plt.axes([0.15,0.05,0.65,0.03])
ax_gravity = plt.axes([0.15,0.15,0.65,0.03])

s_velocity = Slider(ax_velocity, "Velocity", 5, 50, valinit=25)
s_angle = Slider(ax_angle, "Angle", 1, 90, valinit=45)
s_gravity = Slider(ax_gravity, "Gravity", 1, 100, valinit= 9.81)

s_velocity.on_changed(reset)
s_angle.on_changed(reset)
s_gravity.on_changed(reset)

ani = FuncAnimation(fig, update, init_func=init, blit=False, interval=0)

plt.show()
