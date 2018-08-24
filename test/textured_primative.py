import pyglet
import pybox
import pyglet.gl as gl

from pyglet.window import key

# ------------------------------

pyglet.resource.path = ['../res/sprites', '../res/textures']
pyglet.resource.reindex()

# ------------------------------

window = None
batch = pyglet.graphics.Batch()

rect = {"x":100, "y":200, "w":50, "h":50}
rect_cl = (255, 255, 255, 255)
rect_vl = None

rect_img = pyglet.resource.image('ship.png')
rect_img.anchor_x = rect_img.width // 2
rect_img.anchor_y = rect_img.height // 2

rect_vg1 = pybox.graphics.groups.transform.TransformGroup(rect["x"], rect["y"])
rect_vg2 = pyglet.graphics.TextureGroup(rect_img.get_texture(), parent=rect_vg1)
rect_vg3 = pybox.graphics.groups.blend.BlendGroup(parent=rect_vg2)

# ------------------------------

@pybox.game.load
def loadWindow(win):
    global window
    window = win
    window.set_location(100, 125)

@pybox.game.load
def loadShapes(win):
    global rect_vl
    rect_vl = batch.add_indexed(4, gl.GL_TRIANGLES,
        rect_vg3,
        [0, 1, 2, 2, 3, 0],
        ('v2i', (
                    -rect["w"],  rect["h"],
                     rect["w"],  rect["h"],
                     rect["w"], -rect["h"],
                    -rect["w"], -rect["h"]
                )
        ),
        ('c4B', rect_cl * 4),
        ('t3f', rect_img.get_texture().tex_coords)
    )

@pybox.game.key_press
def key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        window.close()

@pybox.game.update
def update(dt):
    rect_vg1.angle += 0.5
    rect_vg1.x += 50 * dt
    pass

@pybox.game.draw
def draw():
    batch.draw()


if __name__ == "__main__":
    pybox.game.run()