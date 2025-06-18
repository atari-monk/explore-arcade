import arcade

WINDOW_WIDTH: int = 600
WINDOW_HEIGHT: int = 600
WINDOW_TITLE: str = "Happy Face Example"

arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, resizable=True)  # type: ignore
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

x: int = 300
y: int = 300
radius: int = 200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

x = 370
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 230
y = 350
radius = 20
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 300
y = 280
width: int = 240
height: int = 200
start_angle: int = 190
end_angle: int = 350
line_width: int = 20
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, line_width)

arcade.finish_render()
arcade.run()
