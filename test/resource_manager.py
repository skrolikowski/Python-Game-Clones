import pybox

from pybox.graphics.resources import ResourceManager

resources = ResourceManager(['../res/sprites', '../res/textures'])

resources.add_image('ship.png', 'player')

print(resources.get_image('player'))