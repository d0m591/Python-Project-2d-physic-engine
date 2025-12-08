import matplotlib.pyplot as plt
import numpy as np
import math

timestep = 0.2

class projectile:
    def __init__(self, velocity, angle):
        self.velocity = velocity
        self.angle = math.radians(angle)

        # Converting velocity into components
        self.xv = self.velocity * math.cos(self.angle)
        self.yv = self.velocity * math.sin(self.angle)

        #Arrays for storing positions
        self.xpos = [0]
        self.ypos = [0]

    def move(self):
        #updating xPosition
        newX = self.xpos[-1] + self.xv * timestep
        self.xpos.append(newX)

        #updating yPosition
        newY = self.ypos[-1] + self.yv * timestep
        self.ypos.append(newY)


p1 = projectile(20, 15)

for i in range(5):
    print(f"This is x {p1.xpos} and this is y {p1.ypos}")
    p1.move()
