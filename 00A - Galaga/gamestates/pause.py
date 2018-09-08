import pybox

from pyglet.window import key

class PauseState:
    def __init__(self):
        self.window = None
        self.prev = None

    @pybox.game.load
    def on_load(self, win):
        self.window = win
        print("Pause - load")

    @pybox.game.enter
    def on_enter(self, prev, *args, **kwargs):
        self.prev = prev
        print("Pause - enter")
        pass

    @pybox.game.leave
    def on_leave(self, *args, **kwargs):
        print("Pause - leave")
        pass

    @pybox.game.resume
    def on_resume(self, *args, **kwargs):
        print("Pause - resume")
        pass

    @pybox.game.draw
    def on_draw(self):
        self.prev.on_draw()

    @pybox.game.key_press
    def on_key_press(self, symbol, modifiers):
        if symbol == key.P:
            pybox.game.pop()