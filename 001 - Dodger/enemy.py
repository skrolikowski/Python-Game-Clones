import resources
import entity
import random

from pybox import math

class Enemy(entity.Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.vel = math.vec2d.Vec2D()
        self.acc = math.vec2d.Vec2D()
        self.speed = 30
        self.max_speed = 50
        self.mass = random.randint(1, 3)
        self.scale = 0.5
        self.remove = False

    def updateEntity(self, dt):
        self.applyForce(0, -dt)
        nX, nY = self.nextPosition()
        self.update(x=nX, y=nY, scale=self.scale)

        if self.offScreen():
            self.remove = True

    def collidesWith(self, other):
        if other.__class__.__name__ == "Bullet":
            self.remove = True
