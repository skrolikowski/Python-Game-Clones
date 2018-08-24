import pyglet
import pybox

from pyglet.window import key

@pybox.game.load
def load(win):
    global window
    window = win
    window.set_location(100, 100)

@pybox.game.key_press
def key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        window.close()

@pybox.game.update
def update(dt):
    pass

@pybox.game.draw
def draw():
    pybox.graphics.setColor(255, 0, 0, 255)
    pybox.graphics.setLineWidth(5)
    pybox.graphics.rectangle('line', 150, 150, 50, 75)

    pybox.graphics.push()
    pybox.graphics.translate(200, 200)
    pybox.graphics.rotate(120)
    pybox.graphics.setColor(0, 0, 255, 255)
    pybox.graphics.setLineWidth(2)
    pybox.graphics.rectangle('line', 0, 0, 50, 50)
    pybox.graphics.pop()
    pass

if __name__ == "__main__":
    # t1 = pybox.graphics.transform.Transform()
    # t1.translate(1, 2)
    # t1.scale(0.5, 0.5)
    # print(t1)

    pybox.game.run()