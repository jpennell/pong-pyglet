import pyglet
import resources
from models.ball import Ball
from models.paddle import PlayerPaddle, ComputerPaddle

game_objects = [
    Ball(),
    PlayerPaddle(),
    ComputerPaddle()
]


@resources.window.event
def on_draw():
    resources.window.clear()
    resources.default_batch.draw()


def update(delta):
    [game_object.update(delta) for game_object in game_objects]


def handle_collisions(delta):
    [game_object.handle_collisions(game_objects) for game_object in game_objects]


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.clock.schedule_interval(handle_collisions, 1/120.0)
    [resources.window.push_handlers(game_object.key_handler) for game_object in game_objects]
    pyglet.app.run()
