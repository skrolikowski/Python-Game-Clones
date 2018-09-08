import pyglet
import const

from pybox.math import vec2d, util

class Entity(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def applyForce(self, dx, dy):
        force = vec2d.Vec2D(dx, dy)
        force.scale(1 / self.mass)

        self.acc += force

    def container(self):
        w = self.width
        h = self.height
        x = self.x - w // 2
        y = self.y - h // 2

        return x, y, w, h

    def AABB(self):
        return self.x - self.width / 2,\
               self.y - self.height / 2,\
               self.x + self.width / 2,\
               self.y + self.height / 2

    def inBounds(self, x, y):
        return x - self.width // 2 > 0 and \
               x + self.width // 2 < const.WIDTH and \
               y - self.height // 2 > 0 and \
               y + self.height // 2 < const.HEIGHT

    def offScreen(self):
        x, y, w, h = self.container()

        return x + w < 0 or \
               x > const.WIDTH or \
               y + h < 0 or \
               y > const.HEIGHT

    def nextPosition(self):
        # apply accel forces
        self.vel += self.acc
        self.acc.scale(0)

        # adjust for `maxSpeed`
        self.vel.limit(self.max_speed)

        # next position
        posX = self.x + self.vel.x
        posY = self.y + self.vel.y

        return posX, posY

    def hasCollidedWith(self, other):
        sX1, sY1, sX2, sY2 = self.AABB()
        oX1, oY1, oX2, oY2 = other.AABB()

        return sX1 < oX2 and sX2 > oX1 and sY1 < oY2 and sY2 > oY1

    def draw(self):
        x1, y1, x2, y2 = self.AABB()
        color = 255, 0, 0, 255

        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_LINES,
            [0, 1, 1, 2, 2, 3, 3, 0],
            ('v2f', (x1, y1, x2, y1, x2, y2, x1, y2)),
            ('c4B', color * 4)
        )
