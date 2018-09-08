import pybox
import random
import pymunk.pyglet_util

from app.variables import *
from pybox.graphics import shape2d
from pyglet.window import key


@pybox.game.load
def load(win):
    global window, space, draw_options, balls

    window = win

    space = pymunk.Space()
    space.gravity = (0.0, -900.0)
    draw_options = pymunk.pyglet_util.DrawOptions()

    balls = []
    lines = [
        pymunk.Segment(space.static_body, (111.0, 280.0), (407.0, 246.0), 0.0),
        pymunk.Segment(space.static_body, (407.0, 246.0), (407.0, 343.0), 0.0)
    ]

    for line in lines:
        line.elasticity = 0.95
        line.friction = 0.9

        shape2d.Segment(111.0, 280.0, 407.0, 246.0)
        shape2d.Segment(407.0, 246.0, 407.0, 343.0)

    space.add(lines)

@pybox.game.update
def update(dt):
    space.step(dt)

    # Remove balls not on screen
    removables = [b for b in balls if b[0].body.position.y < 100]

    for ball in removables:
        ball[1].delete()
        space.remove(ball[0], ball[0].body)
        balls.remove(ball)

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
    space.debug_draw(draw_options)

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

def spawn_ball(dt):
    x = random.randint(115,350)
    y = 400
    mass = 10
    radius = 25
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))

    body = pymunk.Body(mass, inertia)
    body.position = x, 400

    shape0 = pymunk.Circle(body, radius, (0,0))
    shape0.elasticity = 0.95
    shape0.friction = 0.9

    shape1 = shape2d.Circle(x, y, radius)

    space.add(body, shape0)
    balls.append((shape0, shape1))

if __name__ == "__main__":
    pyglet.clock.schedule_interval(spawn_ball, 1.5)
    pybox.game.run()