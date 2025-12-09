import matplotlib.pyplot as plt
import numpy as np
import math
gravity = -9.81
timestep = 0.02

class projectile:
    def __init__(self, velocity, angle):
        self.velocity = velocity
        self.angle = math.radians(angle)

        # Converting velocity into components
        self.xv = self.velocity * math.cos(self.angle)
        self.yv = self.velocity * math.sin(self.angle)

        #Arrays for storing positions in form [x,y]
        self.position = [[0,0]]
        self.newX = 0
        self.newY = 0


    def move(self):
        self.newX = self.position[-1][0] + self.xv * timestep
        self.newY = self.position[-1][1] + self.yv * timestep
        self.position.append([self.newX,self.newY])
        return self.newX,self.newY

    def gravity(self):
        self.yv = self.yv + gravity * timestep

p1 = projectile(22, 43)




while p1.newY >= 0:
    p1.move()
    p1.gravity()
    
    
fig, ax = plt.subplots()
Xlist = [pos[0] for pos in p1.position]
Ylist = [pos[1] for pos in p1.position]
plt.plot(Xlist, Ylist, '-')
plt.show()
