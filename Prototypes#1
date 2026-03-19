import math
timestep = 1
airborne = True
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
        self.position.append([roundedX,roundedY])
        if y < 0:
            airborne = False
        
    def applyGravity(self):
        self.yv += self.gravity * timestep

p1 = Projectile(25,45,-9.81)


while True:
    if airborne:
        p1.applyGravity()
        p1.move()
        print(f"The position of the projectile is {p1.position[-1]}, Its velocity is {math.sqrt(p1.xv**2 + p1.yv**2):.2f}")
    
    else:
        print("its hit the ground")
        break
