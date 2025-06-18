import arcade
from arcade.types import Color
from typing import Any, cast

WINDOW_TITLE = "Platformer"
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

PLAYER_MOVEMENT_SPEED = 10
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

FOLLOW_DECAY_CONST = 0.3

class GameView(arcade.View):
    def __init__(self) -> None:
        super().__init__()
        self.camera_sprites = arcade.Camera2D()
        self.camera_bounds = self.window.rect
        self.camera_gui = arcade.Camera2D()
        self.scene = self.create_scene()
        self.player_sprite = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
            scale=CHARACTER_SCALING,
        )
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=cast(arcade.SpriteList[Any], self.scene["Platforms"])
        )
        self.score = 0
        self.left_key_down = False
        self.right_key_down = False
        self.score_display = arcade.Text(
            "Score: 0",
            x=10,
            y=10,
            color=arcade.csscolor.WHITE,
            font_size=18,
        )

    def create_scene(self) -> arcade.Scene:
        layer_options = {
            "Platforms": {
                "use_spatial_hash": True,
            },
        }
        tile_map = arcade.load_tilemap(
            ":resources:tiled_maps/map.json",
            scaling=TILE_SCALING,
            layer_options=layer_options,
        )
        if tile_map.background_color:
            self.window.background_color = Color.from_iterable(tile_map.background_color)
        self.camera_bounds = arcade.LRBT(
            self.window.width / 2.0,
            tile_map.width * GRID_PIXEL_SIZE - self.window.width / 2.0,
            self.window.height / 2.0,
            tile_map.height * GRID_PIXEL_SIZE,
        )
        return arcade.Scene.from_tilemap(tile_map)

    def reset(self) -> None:
        self.score = 0
        self.scene = self.create_scene()
        self.player_sprite.position = (128, 128)
        self.scene.add_sprite("Player", self.player_sprite)

    def on_draw(self) -> None:
        self.clear()
        with self.camera_sprites.activate():
            self.scene.draw()  # type: ignore
        with self.camera_gui.activate():
            self.score_display.text = f"Score: {self.score}"
            self.score_display.draw()

    def update_player_speed(self) -> None:
        self.player_sprite.change_x = 0
        if self.left_key_down and not self.right_key_down:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_key_down and not self.left_key_down:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        key = symbol
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_key_down = True
            self.update_player_speed()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_key_down = True
            self.update_player_speed()

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        key = symbol
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_key_down = False
            self.update_player_speed()
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_key_down = False
            self.update_player_speed()

    def center_camera_to_player(self) -> None:
        self.camera_sprites.position = arcade.math.smerp_2d(
            self.camera_sprites.position,
            self.player_sprite.position,
            self.window.delta_time,
            FOLLOW_DECAY_CONST,
        )
        self.camera_sprites.view_data.position = arcade.camera.grips.constrain_xy(
            self.camera_sprites.view_data, self.camera_bounds
        )

    def on_update(self, delta_time: float) -> None:
        self.physics_engine.update()
        coin_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, cast(arcade.SpriteList[Any], self.scene["Coins"])
        )
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
        self.center_camera_to_player()

    def on_resize(self, width: int, height: int) -> None:
        super().on_resize(width, height)
        self.camera_sprites.match_window()
        self.camera_gui.match_window(position=True)

def main() -> None:
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    game = GameView()
    game.reset()
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()

