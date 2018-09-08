import pybox

from app.variables import *
from pybox.graphics.drawables import shape2d
from pyglet.window import key

WIDTH = 600
HEIGHT = 600

@pybox.game.load
def load(win):
    global window, shapes

    window = win
    shapes = []

    """
        sprite1 = sprite2d.Sprite(img, x=, y=)
        sprite1.add(space, BODY_TYPE_KINEMATIC)

        shape1 = shape2d.Rectangle(x=, y=, width=, height=)
        shape1.add(space, BODY_TYPE_RIGID)
    """

    shape1 = shape2d.Rectangle(100, 250, 50, 50, "fill")
    shape1.rotation = 45
    shapes.append(shape1)
    print(shape1.bounds)

    shape2 = shape2d.Polygon([(300, 300), (350, 350), (325, 400), (275, 400), (250, 350)])
    shape2.color = (0, 0, 255, 255)
    shape2.lineWidth = 2
    shapes.append(shape2)
    print(shape2.bounds)

    shape3 = shape2d.Segment(400, 100, 500, 150)
    shape3.color = (0, 255, 0, 255)
    shape3.lineWidth = 3
    shapes.append(shape3)
    print(shape3.bounds)

    shape4 = shape2d.Circle(250, 300, 25)
    shape4.color = (0, 255, 0, 255)
    shapes.append(shape4)
    print(shape4.bounds)

    shape5 = shape2d.Ellipse(250, 400, 5, 10)
    shape5.color = (0, 255, 0, 255)
    shapes.append(shape5)
    print(shape5.bounds)

    shape6 = shape2d.Arc(100, 100, 50, 45, 90)
    shapes.append(shape6)
    print(shape6.bounds)

@pybox.game.update
def update(dt):
    shapes[0].rotation += 25 * dt
    shapes[1].rotation += 25 * dt
    shapes[2].rotation += 25 * dt
    shapes[3].rotation += 25 * dt
    shapes[4].rotation += 25 * dt
    shapes[5].rotation += 25 * dt

    for shape in shapes:
        shape.update(dt)

@pybox.game.draw
def draw():
    default_batch.draw()

    for shape in shapes:
        shape.debug()

@pybox.game.key_press
def key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        window.close()
    elif symbol == key.D:
        shapes[0].apply_impulse((1000, 0), (1, 1))
    elif symbol == key.A:
        shapes[0].apply_force((10, 0), (-1, -1))

if __name__ == "__main__":
    pybox.game.run(WIDTH, HEIGHT)