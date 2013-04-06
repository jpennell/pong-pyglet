import pyglet
from pyglet.window import key
import resources
from vector import Vector2d


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
