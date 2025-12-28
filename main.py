from pyray import *
import random
import math

nu = 30
nx,ny = 20,20

brush_rad = 20

init_window( int(nx*nu), int(ny*nu), "Hello")

points = [ 0 for i in range(nx*ny) ]
squares = [ 0 for i in range( (nx-1)*(ny-1) ) ]
mc_sprite = load_texture("marching_squares_strip.png")

def draw_points():
    for i,p in enumerate(points):
        x = (i%nx)*nu + nu//2
        y = (i//nx)*nu + nu//2
        r = 1
        draw_circle(x,y,r, WHITE if p==1 else BLACK )
        #draw_circle_lines(x,y,r,GRAY)

def mouse_brush():

    mp = get_mouse_position()
    draw_circle_lines(int(mp.x),int(mp.y),brush_rad,WHITE)

    for i,p in enumerate(points):
        x = (i%nx)*nu + nu//2
        y = (i//nx)*nu + nu//2
        d = math.hypot(mp.x-x,mp.y-y)

        if d <= brush_rad and (is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT) or is_mouse_button_down(MouseButton.MOUSE_BUTTON_RIGHT)):
            points[i] = 1 if is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT) else 0

def draw_squares():
    for i,s in enumerate(squares):
        x = (i%(nx-1))*nu +nu//2
        y = (i//(nx-1))*nu +nu//2
        
        bi = (i//(nx-1))*nx + (i%(nx-1))

        key = 8*points[bi+1] + 4*points[bi] + 2*points[bi + nx] + points[bi + nx + 1]
        
        draw_texture_pro(mc_sprite, Rectangle(key*32,0,32,32),Rectangle(x,y,nu,nu),Vector2(0,0),0, GREEN )
        #draw_text(str(key),x+2,y+2,20,GREEN)


while not window_should_close():
    begin_drawing()
    clear_background(BLUE)
    draw_squares()
    draw_points()
    mouse_brush()
    end_drawing()

    wheel = get_mouse_wheel_move()
    brush_rad = max(10, brush_rad + wheel*12 )

close_window()