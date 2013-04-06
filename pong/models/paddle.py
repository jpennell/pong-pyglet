from pyglet.window import key
import resources
from gameobject import GameObject
from vector import Vector2d


class Paddle(GameObject):
    def __init__(self, name, image=resources.paddle_image,
                 position=Vector2d(x=resources.paddle_image.width,
                                   y=resources.window.height / 2)):
        super(Paddle, self).__init__(name=name, image=image, position=position)


class PlayerPaddle(Paddle):
    def __init__(self):
        super(PlayerPaddle, self).__init__(name="paddle")

    def update(self, delta):
        super(PlayerPaddle, self).update(delta)

        if self.key_handler[key.UP]:
            self.position.y += (150 * delta)
        if self.key_handler[key.DOWN]:
            self.position.y -= (150 * delta)

        self.cap_position()


class ComputerPaddle(Paddle):
    def __init__(self, position=Vector2d(x=resources.window.width - resources.paddle_image.width,
                                         y=resources.window.height / 2)):
        super(ComputerPaddle, self).__init__(name="computer-paddle", position=position)
