import pyglet
import resources

game_window = pyglet.window.Window(800, 600)


@game_window.event
def on_draw():
    game_window.clear()
    resources.label.draw()
    resources.ball.draw()


if __name__ == '__main__':
    pyglet.app.run()
