from gameobject import GameObject
import resources
from vector import Vector2d


class Ball(GameObject):
    def __init__(self, image=resources.ball_image,
                 position=Vector2d(400, 300),
                 velocity=Vector2d(-100, -150)):
        super(Ball, self).__init__(name="ball", image=image, position=position, velocity=velocity)

    def update(self, delta):
        super(Ball, self).update(delta)

        if self.position.y >= (resources.window.height - self.image.height) or self.position.y <= self.image.height:
            self.velocity.y = -self.velocity.y

        self.cap_position()

    def handle_collisions(self, game_objects):
        super(Ball, self).handle_collisions(game_objects)
        for game_object in game_objects:
            if game_object.name == "paddle":
                self.handle_paddle_collision(game_object)
            elif game_object.name == "computer-paddle":
                self.handle_computer_paddle_collision(game_object)

    def handle_paddle_collision(self, paddle):
        x = paddle.position.x + (paddle.image.width / 2)
        y_top = paddle.position.y + (paddle.image.height / 2)
        y_bottom = paddle.position.y - (paddle.image.height / 2)

        if self.position.x <= x and y_bottom <= self.position.y <= y_top:
            self.velocity.x = -self.velocity.x
            self.position.x = paddle.position.x + (paddle.image.width / 2) + (self.image.width / 2) + 1

    def handle_computer_paddle_collision(self, paddle):
        x = paddle.position.x - (paddle.image.width / 2)
        y_top = paddle.position.y + (paddle.image.height / 2)
        y_bottom = paddle.position.y - (paddle.image.height / 2)

        if self.position.x >= x and y_bottom <= self.position.y <= y_top:
            self.velocity.x = -self.velocity.x
            self.position.x = paddle.position.x - (paddle.image.width / 2) - (self.image.width / 2) - 1
