import pyglet

pyglet.resource.path = ['images']
pyglet.resource.reindex()

#Ball
ball_image = pyglet.resource.image("ball.png")
ball = pyglet.sprite.Sprite(img=ball_image, x=400, y=300)

#Label
label = pyglet.text.Label(text="Pong, Pong, Pong", x=400, y=575, anchor_x='center')
