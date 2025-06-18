import arcade
from arcade import Sprite, SpriteList, View
from arcade.types import Color
from typing import Optional

class Scene(View):
    def __init__(self) -> None:
        super().__init__()
        self.window: Optional[arcade.Window] = None

    def do_clear(self) -> None:
        if self.window:
            self.clear()

    def on_draw(self) -> None:
        self.do_clear()

    def on_update(self, delta_time: float) -> None:
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int) -> None:
        pass

class MenuScene(Scene):
    def __init__(self) -> None:
        super().__init__()
        self.button: Sprite = arcade.SpriteSolidColor(200, 50, color=Color(0, 255, 0, 255))
        self.button.center_x = 400
        self.button.center_y = 300
        self.sprites: SpriteList[Sprite] = SpriteList()
        self.sprites.append(self.button)

    def on_draw(self) -> None:
        super().on_draw()
        self.sprites.draw()
        arcade.draw_text("Main Menu", 400, 400, Color(255, 255, 255, 255), 30, anchor_x="center")

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int) -> None:
        if button == arcade.MOUSE_BUTTON_LEFT and self.button.collides_with_point((x, y)):
            if self.window:
                view = GameView(Level1Scene())
                view.window = self.window
                self.window.show_view(view)

class Level1Scene(Scene):
    def __init__(self) -> None:
        super().__init__()
        self.player: Sprite = arcade.SpriteSolidColor(50, 50, color=Color(0, 0, 255, 255))
        self.player.center_x = 400
        self.player.center_y = 100
        self.sprites: SpriteList[Sprite] = SpriteList()
        self.sprites.append(self.player)

    def on_draw(self) -> None:
        super().on_draw()
        self.sprites.draw()
        arcade.draw_text("Level 1", 400, 550, Color(255, 255, 255, 255), 30, anchor_x="center")

    def on_update(self, delta_time: float) -> None:
        self.player.center_y += 1
        if self.player.center_y > 600 and self.window:
            view = GameView(Level2Scene())
            view.window = self.window
            self.window.show_view(view)

class Level2Scene(Scene):
    def __init__(self) -> None:
        super().__init__()
        self.player: Sprite = arcade.SpriteSolidColor(50, 50, color=Color(255, 0, 0, 255))
        self.player.center_x = 400
        self.player.center_y = 100
        self.sprites: SpriteList[Sprite] = SpriteList()
        self.sprites.append(self.player)

    def on_draw(self) -> None:
        super().on_draw()
        self.sprites.draw()
        arcade.draw_text("Level 2", 400, 550, Color(255, 255, 255, 255), 30, anchor_x="center")

    def on_update(self, delta_time: float) -> None:
        self.player.center_y += 2
        if self.player.center_y > 600 and self.window:
            view = GameView(MenuScene())
            view.window = self.window
            self.window.show_view(view)

class GameView(View):
    def __init__(self, scene: Scene) -> None:
        super().__init__()
        self.current_scene: Scene = scene
        if self.window:
            scene.window = self.window

    def on_draw(self) -> None:
        self.current_scene.on_draw()

    def on_update(self, delta_time: float) -> None:
        self.current_scene.on_update(delta_time)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int) -> None:
        self.current_scene.on_mouse_press(x, y, button, modifiers)

def main() -> None:
    window = arcade.Window(800, 600, "Scene Management")
    window.show_view(GameView(MenuScene()))
    arcade.run()

if __name__ == "__main__":
    main()