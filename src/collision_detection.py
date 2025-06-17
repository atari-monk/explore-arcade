import arcade
from arcade import Sprite
from arcade.types import Color
from typing import List

class CollisionWindow(arcade.Window):
    def __init__(self) -> None:
        super().__init__(width=800, height=600, title="Collision Detection")
        arcade.set_background_color(arcade.color.ALMOND)
        self.player: Sprite = arcade.SpriteSolidColor(
            width=50, 
            height=50, 
            color=Color(0, 0, 255, 255)
        )
        self.player.center_x = 400
        self.player.center_y = 300
        self.obstacles: arcade.SpriteList[arcade.Sprite] = arcade.SpriteList()
        self.create_obstacles()

    def create_obstacles(self) -> None:
        for i in range(5):
            obstacle: Sprite = arcade.SpriteSolidColor(
                width=40,
                height=40,
                color=Color(255, 0, 0, 255)
            )
            obstacle.center_x = 100 + i * 150
            obstacle.center_y = 100 + i * 100
            self.obstacles.append(obstacle)

    def on_draw(self) -> None:
        self.clear()
        arcade.draw_sprite(self.player)
        self.obstacles.draw()

    def on_update(self, delta_time: float) -> None:
        self.player.center_x += self.player.change_x
        self.player.center_y += self.player.change_y

        hit_list: List[Sprite] = arcade.check_for_collision_with_list(
            self.player, 
            self.obstacles
        )
        
        for obstacle in hit_list:
            obstacle.color = Color(0, 255, 0, 255)
            self.player.change_x *= -1
            self.player.change_y *= -1

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        speed: float = 5.0
        if symbol == arcade.key.LEFT:
            self.player.change_x = -speed
        elif symbol == arcade.key.RIGHT:
            self.player.change_x = speed
        elif symbol == arcade.key.UP:
            self.player.change_y = speed
        elif symbol == arcade.key.DOWN:
            self.player.change_y = -speed

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        if symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0
        elif symbol in (arcade.key.UP, arcade.key.DOWN):
            self.player.change_y = 0

def main() -> None:
    _ = CollisionWindow()
    arcade.run()

if __name__ == "__main__":
    main()