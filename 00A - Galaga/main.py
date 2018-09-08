import pybox
import pyglet

from gamestates.game import GameState
from settings import const

if __name__ == "__main__":
    pybox.game.run(width=const.WIDTH, height=const.HEIGHT, caption="GALAGA")
    pybox.game.switch(GameState())

    pyglet.app.run()
