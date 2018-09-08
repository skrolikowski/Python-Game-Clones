import pybox

from settings import resources
from gamestates.pause import PauseState
from pyglet.window import key

class GameState:
    def __init__(self):
        self.window = None

    @pybox.game.load
    def on_load(self, win):
        print(self, win)
        self.window = win
        print("Game - load")

    @pybox.game.enter
    def on_enter(self, prev, *args, **kwargs):
        print("Game - enter")
        pass

    @pybox.game.leave
    def on_leave(self, *args, **kwargs):
        print("Game - leave")
        pass

    @pybox.game.resume
    def on_resume(self, *args, **kwargs):
        print("Game - resume")
        pass

    @pybox.game.update
    def on_update(self, dt):
        pass

    @pybox.game.draw
    def on_draw(self):
        resources.background.blit_tiled(0, 0, 0, self.window.width, self.window.height)
        resources.batch.draw()

    @pybox.game.key_press
    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.window.close()
        elif symbol == key.P:
            pybox.game.push(PauseState())