import pyglet
import pybox
import Box2D

from pybox.variables import *
from pybox.graphics.shape2d import Rectangle, Ellipse, Circle, Polygon, Line
from pyglet.window import key, mouse


@pybox.game.load
def load(win):
    global window, shape1, shape2, shape3

    window = win

    shape1 = Rectangle(100, 250, 50, 50, "fill")
    shape1.color = (255, 0, 0, 255)

    shape2 = Polygon([(300, 300), (350, 350), (325, 400), (275, 400), (250, 350)])
    shape2.color = (0, 0, 255, 255)
    shape2.lineWidth = 2

    shape3 = Line(400, 100, 500, 150)
    shape3.color = (0, 255, 0, 255)
    shape3.lineWidth = 3

@pybox.game.update
def update(dt):
    shape1.position.x += 10 * dt
    shape1.angle += 5 * dt
    shape2.angle += 25 * dt
    shape3.position.x -= 10 * dt
    shape3.angle += 25 * dt
    pass

@pybox.game.draw
def draw():
    default_batch.draw()

@pybox.game.key_press
def key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        window.close()


if __name__ == "__main__":
    pybox.game.run()