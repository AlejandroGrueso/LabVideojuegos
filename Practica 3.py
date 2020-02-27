import arcade



def draw_suelo():
    arcade.draw_lrtb_rectangle_filled(0, 600, 200, 0, arcade.csscolor.SANDY_BROWN)


def draw_mesa():
    arcade.draw_rectangle_filled(50, 200, 20, 150, arcade.csscolor.SIENNA)
    arcade.draw_rectangle_filled(150, 200, 20, 150, arcade.csscolor.SIENNA)
    arcade.draw_rectangle_filled(100, 280, 150, 20, arcade.csscolor.SIENNA)


def draw_lampara():
    arcade.draw_rectangle_filled(100, 315, 50, 50, arcade.csscolor.FIREBRICK)
    arcade.draw_rectangle_filled(100, 365, 15, 50, arcade.csscolor.BROWN)
    arcade.draw_triangle_filled(70, 380, 130, 380, 100, 440, arcade.csscolor.GREEN)


def draw_puerta():
    arcade.draw_rectangle_filled(400, 350, 150, 300, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(450, 320, 10, arcade.csscolor.YELLOW)

def pelota(x,y):
    arcade.draw_circle_filled(x, y, 30, arcade.csscolor.BLACK)

def on_draw(delta_time):
    arcade.start_render()
    draw_suelo()
    draw_lampara()
    draw_mesa()
    pelota(on_draw.pelota, 150)
    draw_puerta()
    on_draw.pelota += 1
on_draw.pelota = 100

def main():
    arcade.open_window(600, 600, "Dibujo")
    arcade.schedule(on_draw, 1/60)
    arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)
    arcade.run()
main()