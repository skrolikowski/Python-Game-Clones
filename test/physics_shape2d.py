import pyglet
import pybox
import pymunk
import pymunk.pyglet_util

from pybox.variables import *
from pybox.physics import shape2d
from pyglet.window import key, mouse


WIDTH = 600
HEIGHT = 600


@pybox.game.load
def load(win):
    global window, shapes, space, draw_options

    window = win
    shapes = []

    space = pymunk.Space()
    space.gravity = 0.0, -900.0

    draw_options = pymunk.pyglet_util.DrawOptions()

    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Segment(body, pymunk.Vec2d(100, 50), pymunk.Vec2d(500, 50), 3.0)
    shape.friction = 0.99
    space.add(body, shape)

    shape1 = shape2d.Rectangle(WIDTH/2, HEIGHT/2, 50, 50)
    shape1.color = (255, 0, 0, 255)
    shape1.friction = 0.5
    shapes.append(shape1)

    space.add(shape1.body, shape1.shape)

@pybox.game.update
def update(dt):
    space.step(dt)

    for shape in shapes:
        shape.update()

@pybox.game.draw
def draw():
    default_batch.draw()
    space.debug_draw(draw_options)

@pybox.game.key_press
def key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        window.close()


if __name__ == "__main__":
    pybox.game.run(WIDTH, HEIGHT)