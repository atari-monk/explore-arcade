import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Starting Template"

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.AMAZON

    def reset(self):
        pass

    def on_draw(self):
        self.clear()

    def on_update(self, delta_time: float) -> bool | None:
        pass

    def on_key_press(self, symbol: int, modifiers: int) -> bool | None:
        pass

    def on_key_release(self, symbol: int, modifiers: int) -> bool | None:
        pass

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        pass

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        pass

def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    game = GameView()
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()

