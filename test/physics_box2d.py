import pyglet
import pybox
import Box2D

from pybox.variables import *
from pybox.graphics.shape2d import Circle
from pyglet.window import key, mouse
from Box2D.b2 import world, polygonShape, staticBody, dynamicBody


@pybox.game.load
def load(win):
    global window, world, shape1

    window = win
    world = world(gravity=(0, -10), doSleep=True)

    shape1  = Circle(300, 500, 25, "fill")
    shape1.color = (200, 50, 150, 255)

    body    = world.CreateDynamicBody(position=shape1.position.tuple())
    fixture = body.CreateCircleFixture(radius=shape1.radius, density=1, friction=0.3)

@pybox.game.update
def update(dt):
    world.Step(window.fps, 10, 10)

    for body in world.bodies:
        shape1.update(
            x=body.position.x,
            y=body.position.y,
            angle=body.angle
        )

@pybox.game.draw
def draw():
    default_batch.draw()

@pybox.game.key_press
def key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        window.close()


if __name__ == "__main__":
    pybox.game.run()