import pyglet

def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

# Set resource path
pyglet.resource.path = ['../res/sprites', '../res/textures']
pyglet.resource.reindex()

# bullet image
bullet_image = pyglet.resource.image('bullet.png')
center_image(bullet_image)

# player image
player_image = pyglet.resource.image('ship.png')
center_image(player_image)

# enemy images
enemy_images = []
enemy_images.append(pyglet.resource.image('enemy1.png'))
enemy_images.append(pyglet.resource.image('enemy1.png'))
enemy_images.append(pyglet.resource.image('enemy2.png'))
enemy_images.append(pyglet.resource.image('enemy3.png'))
enemy_images.append(pyglet.resource.image('enemy4.png'))

for enemy_image in enemy_images:
    center_image(enemy_image)

# background image
background_img = pyglet.resource.image('black.png')
background = pyglet.image.TileableTexture.create_for_image(background_img)

window = None
batch = pyglet.graphics.Batch()