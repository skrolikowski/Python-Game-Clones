import pyglet
import pybox
import player
import enemy
import const
import resources
import random

from player import Player
from pyglet.window import key

entities = []

@pybox.game.load
def load(win):
    resources.window = win

    # Entities ---------------------
    player = Player(x=const.WIDTH//2, y=50, batch=resources.batch)
    win.push_handlers(player.key_handler)
    win.push_handlers(player)

    entities.append(player)

@pybox.game.update
def update(dt):
    # remove entities
    for entity in [obj for obj in entities if obj.remove]:
        entity.delete()
        entities.remove(entity)

    # update entities
    for entity in entities:
        entity.updateEntity(dt)

        if hasattr(entity, "children"):
            entities.extend(entity.children)
            entity.children.clear()

    # check for collision
    for i in range(len(entities)):
        for j in range(i+1, len(entities)):
            obj1 = entities[i]
            obj2 = entities[j]

            if obj1.hasCollidedWith(obj2):
                obj1.collidesWith(obj2)
                obj2.collidesWith(obj1)

@pybox.game.draw
def draw():
    resources.background.blit_tiled(0, 0, 0, resources.window.width, resources.window.height)
    resources.batch.draw()

@pybox.game.key_press
def key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        resources.window.close()

def spawnEnemy(dt):
    x = random.randint(25, const.WIDTH-10)
    y = const.HEIGHT-5
    img = random.choice(resources.enemy_images)

    entities.append(enemy.Enemy(x=x, y=y, img=img, batch=resources.batch))


if __name__ == "__main__":
    pyglet.clock.schedule_interval(spawnEnemy, 1/3.0)
    pybox.game.run(width=const.WIDTH, height=const.HEIGHT, caption="Dodger")