import arcade

#Tamaño de ventana
arcade.open_window(600, 600, "Dibujo")

#Color de fondo
arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

#Comenzar render
arcade.start_render()

#Suelo
arcade.draw_lrtb_rectangle_filled(0, 600, 200, 0, arcade.csscolor.SANDY_BROWN)

#Mesa
arcade.draw_rectangle_filled(50, 200, 20, 150, arcade.csscolor.SIENNA)
arcade.draw_rectangle_filled(150, 200, 20, 150, arcade.csscolor.SIENNA)
arcade.draw_rectangle_filled(100, 280, 150, 20, arcade.csscolor.SIENNA)

#Lampara
arcade.draw_rectangle_filled(100, 315, 50, 50, arcade.csscolor.FIREBRICK)
arcade.draw_rectangle_filled(100, 365, 15, 50, arcade.csscolor.BROWN)
arcade.draw_triangle_filled(70, 380, 130, 380, 100, 440, arcade.csscolor.GREEN)

#puerta

arcade.draw_rectangle_filled(400, 350, 150, 300, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(450, 320, 10, arcade.csscolor.YELLOW)
#Fin de render
arcade.finish_render()

arcade.run()