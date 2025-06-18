import arcade

class ShapeDrawingWindow(arcade.Window):
    def __init__(self) -> None:
        super().__init__(width=800, height=600, title="Shape Drawing", resizable=False)
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self) -> None:
        self.clear()
        arcade.draw_circle_filled(100, 100, 50, arcade.color.BLUE)
        arcade.draw_rect_filled(arcade.XYWH(200, 200, 100, 50), arcade.color.RED)
        arcade.draw_line(300, 300, 500, 400, arcade.color.GREEN, 3)
        arcade.draw_ellipse_outline(400, 100, 100, 50, arcade.color.PURPLE, 2)
        arcade.draw_arc_filled(600, 500, 80, 80, arcade.color.ORANGE, 0, 180)
        arcade.draw_rect_filled(arcade.XYWH(500, 100, 60, 120), arcade.color.YELLOW, 45)

def main() -> None:
    _window = ShapeDrawingWindow()
    arcade.run()

if __name__ == "__main__":
    main()