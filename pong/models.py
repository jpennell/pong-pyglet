import pyglet
from pyglet.window import key

import resources


class Vector2d(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __mul__(self, scalar):
        return Vector2d(self.x * scalar, self.y * scalar)

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def __str__(self):
        return "{%.2f, %.2f}" % (self.x, self.y)


class GameObject(object):

    def __init__(self, name, image, position=Vector2d(0, 0), velocity=Vector2d(0, 0), batch=resources.default_batch):
        self.name = name
        self.image = image
        self.position = position
        self.velocity = velocity
        self.image.anchor_x = self.image.width / 2
        self.image.anchor_y = self.image.height / 2
        self.sprite = pyglet.sprite.Sprite(img=self.image, x=position.x, y=position.y, batch=batch)
        self.key_handler = key.KeyStateHandler()

    def update(self, delta):
        self.position.add(self.velocity * delta)
        self.cap_position()
        self._update_sprite_position()

    def handle_collisions(self, game_objects):
        pass

    def _update_sprite_position(self):
        self.sprite.x = self.position.x
        self.sprite.y = self.position.y

    def cap_position(self):

        if self.position.y >= (resources.window.height - (self.image.height / 2)):
            self.position.y = (resources.window.height - (self.image.height / 2))

        if self.position.y <= (self.image.height / 2):
            self.position.y = self.image.height / 2


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
