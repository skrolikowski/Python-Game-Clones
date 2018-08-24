import resources
import entity

from pybox import math

class Bullet(entity.Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.bullet_image, *args, **kwargs)

        self.vel = math.vec2d.Vec2d()
        self.acc = math.vec2d.Vec2d()
        self.speed = 20
        self.max_speed = self.speed
        self.mass = 1
        self.scale = 0.25
        self.remove = False

    def updateEntity(self, dt):
        nX, nY = self.nextPosition()
        self.update(x=nX, y=nY, scale=self.scale)

        if self.offScreen():
            self.remove = True

    def collidesWith(self, other):
        if other.__class__.__name__ == "Enemy":
            self.remove = True
