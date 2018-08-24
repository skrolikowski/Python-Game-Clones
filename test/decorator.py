import pyglet
import pybox

from pyglet.window import key, mouse

# ----------------------------
# General
# ----------------------------

@pybox.game.load
def load(win):
    global window
    window = win

@pybox.game.update
def update(dt):
    pass

@pybox.game.draw
def draw():
    pass

# ----------------------------
# Window
# ----------------------------

# @pybox.game.focus
# def focus():
#     print('focused')

# @pybox.game.blur
# def blur():
#     print('blur')

# @pybox.game.hide
# def hide():
#     print('hidden')

# @pybox.game.show
# def show():
#     print('shown')

# @pybox.game.move
# def move(x, y):
#     print('moved', x, y)

# ----------------------------
# Keyboard
# ----------------------------

@pybox.game.key_press
def key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        window.close()

# @pybox.game.key_release
# def key_press(symbol, modifiers):
#     pass

# @pybox.game.key_down
# def key_down(keys):
#     pass

# @pybox.game.text
# def text(text):
#     print(text)

# ----------------------------
# Mouse
# ----------------------------

# @pybox.game.mouse_drag
# def mouse_drag(x, y, dx, dy, buttons, modifiers):
#     print(x, y, dx, dy, buttons)

# @pybox.game.mouse_motion
# def mouse_motion(x, y, dx, dy):
#     print(x, y, dx, dy)

# @pybox.game.mouse_press
# def mouse_press(x, y, button, modifiers):
#     print(x, y, button)

# @pybox.game.mouse_release
# def mouse_release(x, y, button, modifiers):
#     print(x, y, button)

# @pybox.game.mouse_scroll
# def on_mouse_scroll(x, y, scroll_x, scroll_y):
#     print(x, y, scroll_x, scroll_y)


# ----------------------------
# Joystick
# ----------------------------

# joysticks = pyglet.input.get_joysticks()
# joystick = joysticks[0]
# joystick.open()

# @joystick.event
# def on_joybutton_press(joystick, button):
#     print('release', joystick, button)

# @joystick.event
# def on_joybutton_release(joystick, button):
#     print('release', joystick, button)

# @joystick.event
# def on_joyaxis_motion(joystick, axis, value):
#     print('axis motion', joystick, axis, value)

# @joystick.event
# def on_joyhat_motion(joystick, hat_x, hat_y):
#     print('hat motion', joystick, hat_x, hat_y)


if __name__ == "__main__":
    pybox.game.run()