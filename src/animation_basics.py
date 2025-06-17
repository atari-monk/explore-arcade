import arcade
import math
from arcade.types import Color

class AnimationWindow(arcade.Window):
    def __init__(self) -> None:
        super().__init__(width=800, height=600, title="Animation Basics")
        arcade.set_background_color(arcade.color.ALMOND)
        self.sprites: arcade.SpriteList[arcade.Sprite] = arcade.SpriteList()
        self.animation_time: float = 0.0
        
        for i in range(5):
            sprite: arcade.Sprite = arcade.SpriteSolidColor(
                width=64,
                height=64,
                color=Color(255, 0, 0, 255),
                center_x=150 + i * 150,
                center_y=300
            )
            self.sprites.append(sprite)

    def on_draw(self) -> None:
        self.clear()
        self.sprites.draw()

    def on_update(self, delta_time: float) -> None:
        self.animation_time += delta_time
        
        for i, sprite in enumerate(self.sprites):
            sprite.angle = self.animation_time * 45 * (i + 1)
            sprite.scale = 1.0 + 0.2 * abs(math.sin(self.animation_time * (i + 1)))
            sprite.color = Color(
                int(150 + 100 * abs(math.sin(self.animation_time * 0.5 + i))),
                int(150 + 100 * abs(math.sin(self.animation_time * 0.7 + i))),
                int(150 + 100 * abs(math.sin(self.animation_time * 0.9 + i))),
                255
            )

def main() -> None:
    _ = AnimationWindow()
    arcade.run()

if __name__ == "__main__":
    main()