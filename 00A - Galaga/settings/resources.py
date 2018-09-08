import pyglet
import pymunk

from pybox.graphics.resources import ResourceManager

resources = ResourceManager(['../res/sprites', '../res/textures'])

# Register assets
resources.add_image('ship.png', 'player')
resources.add_image('black.png', 'background')

# Global resource variables
window     = None
world      = pymunk.Space()
batch      = pyglet.graphics.Batch()
background = pyglet.image.TileableTexture.create_for_image(resources.get_image('background'))