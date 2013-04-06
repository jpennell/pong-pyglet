import pyglet

pyglet.resource.path = ['images']
pyglet.resource.reindex()

#Window
window = pyglet.window.Window(800, 600)

#Images
ball_image = pyglet.resource.image("ball.png")
paddle_image = pyglet.resource.image("paddle.png")

#Batch
default_batch = pyglet.graphics.Batch()
