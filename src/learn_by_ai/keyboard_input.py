import arcade
from arcade import Sprite
from arcade.types import Color

class KeyboardInputWindow(arcade.Window):
    def __init__(self) -> None:
        super().__init__(width=800, height=600, title="Keyboard Input")
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.player: Sprite = arcade.SpriteSolidColor(
            width=50,
            height=50,
            color=Color(0, 0, 255, 255),
            center_x=400,
            center_y=300
        )
        self.speed: float = 300.0
        self.pressed_keys: set[int] = set()

    def on_draw(self) -> None:
        self.clear()
        arcade.draw_sprite(self.player)

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        self.pressed_keys.add(symbol)

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self.pressed_keys.discard(symbol)

    def on_update(self, delta_time: float) -> None:
        velocity_x: float = 0.0
        velocity_y: float = 0.0

        if arcade.key.LEFT in self.pressed_keys:
            velocity_x -= self.speed
        if arcade.key.RIGHT in self.pressed_keys:
            velocity_x += self.speed
        if arcade.key.UP in self.pressed_keys:
            velocity_y += self.speed
        if arcade.key.DOWN in self.pressed_keys:
            velocity_y -= self.speed

        self.player.center_x += velocity_x * delta_time
        self.player.center_y += velocity_y * delta_time

def main() -> None:
    _window = KeyboardInputWindow()
    arcade.run()

if __name__ == "__main__":
    main()