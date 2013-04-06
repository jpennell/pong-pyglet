from pyglet.window import key
import resources
from gameobject import GameObject, AiGameObject
from vector import Vector2d


class PlayerPaddle(GameObject):
    def __init__(self, name='paddle', image=resources.paddle_image,
                 position=Vector2d(x=resources.paddle_image.width,
                                   y=resources.window.height / 2), velocity=Vector2d(0, 0)):
        super(PlayerPaddle, self).__init__(name=name, image=image, position=position, velocity=velocity)

    def update(self, delta):
        super(PlayerPaddle, self).update(delta)

        if self.key_handler[key.UP]:
            self.position.y += (150 * delta)
        if self.key_handler[key.DOWN]:
            self.position.y -= (150 * delta)

        self.cap_position()


class ComputerPaddle(AiGameObject):

    def __init__(self, name='computer-paddle', image=resources.computer_paddle_image,
                 position=Vector2d(x=resources.window.width - resources.computer_paddle_image.width,
                                   y=resources.window.height / 2), velocity=Vector2d(0, 0)):
        super(ComputerPaddle, self).__init__(name=name, image=image, position=position, velocity=velocity)

    def think(self, game_objects):
        super(ComputerPaddle, self).think(game_objects)
        for game_object in game_objects:
            if game_object.name == "ball":
                self.handle_think(game_object)
                break

    def handle_think(self, ball):
        if ball.velocity.x > 0:
            if ball.position.y > self.position.y:
                self.velocity.y = 150
            if ball.position.y < self.position.y:
                self.velocity.y = -150
        else:
            self.velocity.y = 0
