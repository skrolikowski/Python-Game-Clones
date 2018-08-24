import resources
import entity
import bullet
import math

from pybox.math import vec2d
from pyglet.window import key

class Player(entity.Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.player_image, *args, **kwargs)

        self.vel = vec2d.Vec2d()
        self.acc = vec2d.Vec2d()
        self.speed = 35
        self.max_speed = 50
        self.mass = 3
        self.scale = 0.5
        self.remove = False
        self.children = []
        self.key_handler = key.KeyStateHandler()

    def fire(self):
        cos   = math.cos(math.pi/2)
        sin   = math.sin(math.pi/2)

        left_bullet = bullet.Bullet(x=self.x-15, y=self.y, batch=self.batch)
        right_bullet = bullet.Bullet(x=self.x+15, y=self.y, batch=self.batch)

        left_bullet.vel.x = self.vel.x + cos * left_bullet.speed
        left_bullet.vel.y = self.vel.y + sin * left_bullet.speed
        right_bullet.vel.x = self.vel.x + cos * right_bullet.speed
        right_bullet.vel.y = self.vel.y + sin * right_bullet.speed

        self.children.append(left_bullet)
        self.children.append(right_bullet)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.fire()

    def updateEntity(self, dt):
        self.processKeyHandler(dt)
        nX, nY = self.nextPosition()

        if self.inBounds(nX, nY):
            self.update(x=nX, y=nY, scale=self.scale)
        else:
            self.vel.scale(0)

    def processKeyHandler(self, dt):
        if self.key_handler[key.UP] or self.key_handler[key.W]:
            self.applyForce(0, self.speed * dt)
        elif self.key_handler[key.DOWN] or self.key_handler[key.S]:
            self.applyForce(0, -self.speed * dt)
        else:
            self.vel.y *= 0.98

        if self.key_handler[key.LEFT] or self.key_handler[key.A]:
            self.applyForce(-self.speed * dt, 0)
        elif self.key_handler[key.RIGHT] or self.key_handler[key.D]:
            self.applyForce(self.speed * dt, 0)
        else:
            self.vel.x *= 0.98

    def collidesWith(self, other):
        if other.__class__.__name__ == "Enemy":
            self.remove = True