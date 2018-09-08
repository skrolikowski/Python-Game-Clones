import pybox
import pymunk.pyglet_util

from app.variables import *
from pybox.physics import shape2d
from pyglet.window import key

WIDTH = 600
HEIGHT = 600


@pybox.game.load
def load(win):
    global window, shapes, space, draw_options

    window = win
    shapes = []

    space = pymunk.Space()
    space.gravity = 0.0, -800.0

    handler            = space.add_default_collision_handler()
    handler.begin      = collision_begin
    handler.separate   = collision_end
    handler.pre_solve  = collision_pre_solve
    handler.post_solve = collision_post_solve

    draw_options = pymunk.pyglet_util.DrawOptions()

    shape1 = shape2d.Polygon([(100, 50), (500, 50), (475, 25), (125, 25)], body_type=BODY_TYPE_STATIC)
    shape1.color = (0, 255, 0, 255)
    shape1.elasticity = 0.5
    shape1.friction = 0.5
    shape1.add(space)

    shapes.append(shape1)

def collision_begin(arbiter, space, data):
    return True

def collision_pre_solve(arbiter, space, data):
    return True

def collision_post_solve(arbiter, space, data):
    pass

def collision_end(arbiter, space, data):
    pass

def add_circle(x, y, count=1):
    for i in range(count):
        shape1 = shape2d.Circle(x, y, 15)
        shape1.add(space)

        shape2 = shape2d.Circle(x, y, 15)
        shape2.add(space)

        joint = pymunk.PinJoint(shape1.body, shape2.body)
        joint.distance = 100
        space.add(joint)

        shapes.extend([shape1, shape2])

@pybox.game.update
def update(dt):
    space.step(dt)

    # Remove shapes not on screen
    win_bb = pymunk.BB(window.bounds)
    removables = [s for s in shapes if not s.bounds.intersects(win_bb)]

    for shape in removables:
        shape.delete()
        shapes.remove(shape)

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

@pybox.game.mouse_press
def mouse_press(x, y, button, modifiers):
    if modifiers & key.MOD_SHIFT and button == 1:
        add_circle(x, y, 5)
    elif button == 1:
        add_circle(x, y)

if __name__ == "__main__":
    pybox.game.run(WIDTH, HEIGHT)