import matplotlib.pyplot as plt
import numpy as np
import math

class projectile:
    def __init__(self, velocity, angle):
        self.velocity = velocity
        self.angle = math.radians(angle)

        # Converting velocity into components
        self.xv = self.velocity * math.cos(self.angle)
        self.yv = self.velocity * math.sin(self.angle)

rounded = 5
p1 = projectile(20, 15)

print(f"{p1.yv:.{rounded}f}")
