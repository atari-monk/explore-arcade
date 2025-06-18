import arcade

class ArcadeWindow(arcade.Window):
    def __init__(self) -> None:
        super().__init__(
            width=800,
            height=600,
            title="Arcade Learning Window",
            resizable=True
        )
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self) -> None:
        self.clear()

def main() -> None:
    _window = ArcadeWindow()
    arcade.run()

if __name__ == "__main__":
    main()