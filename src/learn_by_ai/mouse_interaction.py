import arcade
from arcade import Sprite
from arcade.types import Color
from arcade.math import lerp, clamp, rand_on_circle
from typing import Tuple

class MouseInteractionWindow(arcade.Window):
    def __init__(self) -> None:
        super().__init__(width=800, height=600, title="Mouse Interaction")
        arcade.set_background_color(arcade.color.ALICE_BLUE)
        self.target: Sprite = arcade.SpriteSolidColor(
            width=60,
            height=60,
            color=Color(255, 0, 0, 255),
            center_x=400,
            center_y=300
        )
        self.mouse_position: Tuple[float, float] = (0.0, 0.0)
        self.click_count: int = 0
        self.lerp_factor: float = 0.0
        self.target_scale: float = 1.0

    def on_draw(self) -> None:
        self.clear()
        arcade.draw_sprite(self.target)
        arcade.draw_text(
            f"Clicks: {self.click_count}",
            10,
            570,
            arcade.color.BLACK,
            20
        )

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float) -> None:
        self.mouse_position = (x, y)
        distance = arcade.math.get_distance(
            self.target.center_x,
            self.target.center_y,
            x,
            y
        )
        self.lerp_factor = clamp(distance / 800.0, 0.0, 1.0)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int) -> None:
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.click_count += 1
            if self.target.collides_with_point((x, y)):
                random_point = rand_on_circle((400, 300), 200)
                self.target.center_x = lerp(self.target.center_x, random_point[0], self.lerp_factor)
                self.target.center_y = lerp(self.target.center_y, random_point[1], self.lerp_factor)
                self.target_scale = lerp(0.5, 2.0, self.lerp_factor)
                self.target.scale = self.target_scale

    def on_update(self, delta_time: float) -> None:
        self.target.angle += delta_time * 60

def main() -> None:
    _window = MouseInteractionWindow()
    arcade.run()

if __name__ == "__main__":
    main()