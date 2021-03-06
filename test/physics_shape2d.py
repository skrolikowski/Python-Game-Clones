import pybox
import pymunk.pyglet_util

from pybox.app.variables import *
from pybox.graphics.drawables import shape2d
from pybox.graphics.resources import ResourceManager
from pyglet.window import key

WIDTH = 600
HEIGHT = 600

resources = ResourceManager(['../res/sprites', '../res/textures'])
resources.add_image('ship.png', 'player')


@pybox.game.load
def load(win):
    global window, shapes, space, draw_options

    window = win
    shapes = []

    space = pymunk.Space()
    space.gravity = 0.0, -1000.0

    handler            = space.add_default_collision_handler()
    handler.begin      = collision_begin
    handler.separate   = collision_end
    handler.pre_solve  = collision_pre_solve
    handler.post_solve = collision_post_solve

    draw_options = pymunk.pyglet_util.DrawOptions()

    shape1 = shape2d.Polygon([(100, 50), (300, 125), (500, 50), (475, 25), (125, 25)])
    shape1.color = (0, 255, 0, 255)
    shape1.add(space, body_type=BODY_TYPE_STATIC)
    shape1.elasticity = 0.8
    shape1.friction = 0.5

    shape2 = shape2d.Rectangle(WIDTH//2, HEIGHT//2, 50, 50)
    shape2.color = (0, 255, 0, 255)
    shape2.add(space, body_type=BODY_TYPE_RIGID)
    shape2.elasticity = 0.8
    shape2.friction = 0.5

    shapes.extend([shape1, shape2])

def collision_begin(arbiter, space, data):
    # print("Begin")
    return True

def collision_pre_solve(arbiter, space, data):
    # print("Pre Solve")
    return True

def collision_post_solve(arbiter, space, data):
    # print("Post Solve")
    pass

def collision_end(arbiter, space, data):
    # print("End")
    pass

@pybox.game.update
def update(dt):
    space.step(dt)

    # Remove shapes not on screen
    win_bb = pymunk.BB(window.bounds)
    removables = [s for s in shapes if not s.aabb.intersects(win_bb)]

    for shape in removables:
        shape.delete()
        shapes.remove(shape)

    for shape in shapes:
        shape.update(dt)

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