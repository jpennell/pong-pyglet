from gameobject import GameObject
import resources
from vector import Vector2d


class Ball(GameObject):
    def __init__(self, image=resources.ball_image,
                 position=Vector2d(400, 300),
                 velocity=Vector2d(10, 150)):
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
        pass

    def handle_computer_paddle_collision(self, paddle):
        pass
