import pyglet
import pybox
import pymunk

from pybox.variables import *
from pybox.graphics import shape2d
from pyglet.window import key, mouse


@pybox.game.load
def load(win):
    global window, space, balls

    window = win

    space = pymunk.Space()
    space.gravity = 0.0, -900.0

    balls = []

    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape0 = pymunk.Segment(body, pymunk.Vec2d(100, 50), pymunk.Vec2d(500, 50), 3.0)
    shape0.friction = 0.99
    shape1 = shape2d.Line(100, 50, 500, 50)
    shape1.lineWidth = 3
    space.add(shape0)

@pybox.game.update
def update(dt):
    space.step(dt)

    for ball in balls:
        shape0 = ball[0]
        shape1 = ball[1]

        shape1.radius = shape0.radius
        shape1.update(
            x=shape0.body.position.x,
            y=shape0.body.position.y,
            angle=shape0.body.angle
        )

@pybox.game.draw
def draw():
    default_batch.draw()

@pybox.game.key_press
def key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        window.close()

@pybox.game.mouse_press
def mouse_press(x, y, button, modifiers):
    if button == 1:
        body = pymunk.Body(10, 100)
        body.position = x, y

        shape0 = pymunk.Circle(body, 10, (0,0))
        shape0.friction = 0.5

        shape1 = shape2d.Circle(x, y, 10)

        space.add(body, shape0)
        balls.append((shape0, shape1))

if __name__ == "__main__":
    pybox.game.run()