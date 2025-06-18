import arcade
from pathlib import Path

class SpriteWindow(arcade.Window):
    def __init__(self) -> None:
        super().__init__(width=800, height=600, title="Sprite Basics")
        arcade.set_background_color(arcade.color.ALMOND)
        self.sprite_list: arcade.SpriteList[arcade.Sprite] = arcade.SpriteList()
        
        sprite_path = Path(__file__).parent.parent / "assets" / "character.png"
        print(sprite_path)
        self.sprite = arcade.Sprite(sprite_path, center_x=400, center_y=300, scale=1.0)
        self.sprite.angle = 0
        self.sprite.alpha = 255
        self.sprite_list.append(self.sprite)

    def on_draw(self) -> None:
        self.clear()
        self.sprite_list.draw()

    def on_update(self, delta_time: float) -> None:
        self.sprite.angle += 60 * delta_time

def main() -> None:
    _window = SpriteWindow()
    arcade.run()

if __name__ == "__main__":
    main()