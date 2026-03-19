import math

timestep = float(input("Enter timestep: "))

class Projectile:
    def __init__(self, velocity, angle, gravity):
        self.velocity = velocity
        self.angle = math.radians(angle)
        self.gravity = gravity
        self.xv = self.velocity * math.cos(self.angle)
        self.yv = self.velocity * math.sin(self.angle)
        self.position = [[0, 0]]

    def move(self):
        x = self.position[-1][0] + self.xv * timestep
        y = self.position[-1][1] + self.yv * timestep
        roundedX = round(x, 2)
        roundedY = round(y, 2)
        self.position.append([roundedX, roundedY])
        self.predY = self.position[-1][1] + self.yv * timestep



    def applyGravity(self):
        self.yv += self.gravity * timestep


p1 = Projectile(25, 45, -9.81)
x = int(input('Enter how many iterations you would like to run: '))

for i in range(x):
    p1.applyGravity()
    p1.move()
    if p1.predY > 0:
        print(f"The position of the projectile is {p1.position[-1]}, Its velocity is {math.sqrt(p1.xv ** 2 + p1.yv ** 2):.2f}")
    if p1.predY <= 0:
        print(f"it has hit the ground on iteration {i+1}")
        break
