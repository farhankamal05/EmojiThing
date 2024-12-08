#CFU17
#Marisa Ramautar
#12/6/24
#Period 5-6
#scaling code for scaling images

import simplegui
width = int(input("Inital Width?"))
height = int(input("Inital Height?"))

Marisa = Hailey = False
show_hailey = True
show_marisa = True
show_triangle = True
show_ellipse = True
scale = 0.4

frame = None #Global reference to the frame
    
    
def all_false():
    global show_hailey
    global show_marisa
    global show_triangle
    global show_ellipse
    show_hailey = False
    show_marisa = False
    show_triangle = False
    show_ellipse = False

    
def hailey_emoji():
    all_false()
    global show_hailey
    show_hailey = not show_hailey
       
def marisa_emoji():
    all_false()
    global show_marisa
    show_marisa = not show_marisa
    
def show_triangle():
    all_false()
    global show_triangle
    show_triangle = not show_triangle
    
def show_ellipse():
    all_false()
    global show_ellipse
    show_ellipse = not show_ellipse
    
def draw(canvas):
    
    if show_hailey:
        canvas.draw_circle(((width/2)/2, (height/2)/2), (width/2 - 50)*scale, 10, "Yellow", "Yellow")
       
        # Right eye (winking)
        canvas.draw_circle([2*width/3,height/3], 30*scale, 2, "Black", "yellow")
        canvas.draw_circle([2*width/3, height/3], 15*scale, 2, "yellow", "yellow")
       
        # Left eye (open)
        canvas.draw_circle([width/3, height/3], 30*scale, 2, "black", "white")
        canvas.draw_circle([width/3, height/3], 15, 2, "black", "black")
       
        # Big smiling mouth
        canvas.draw_circle([width/2, height/2 + 30], 75*scale, 2, "black")
        canvas.draw_polygon([(width/3.5, height/3), (3*width/3.5, height/3), (3*width/3.5, 1.5*height/3), (width/3.5, 1.5*height/3)], 2, "yellow", "yellow")
     

       
    if marisa_emoji:
        canvas.draw_circle((width-(width/2)/2, (height/2)/2), (width/2 - 50)*scale, 10, "Yellow", "Yellow")
        canvas.draw_line([width/6,height/3],[width/3,height/3],5*scale,"white")
        canvas.draw_line([width-(width/6),height/3],[width-(width/3),height/3],5,"black")
    #Mouth
        canvas.draw_circle([width/2,height/2+70],90,2,"black")
        canvas.draw_polygon([(width/1,height/1),(width/2,height/1),
        (width/4,5*height/3),(width/4,5*height/3)],2,"yellow","yellow")
        
        
        
       
    if show_triangle:
        # Face
        canvas.draw_circle((width-(width/2)/2, (height/1.4)), (width/2 - 50)*scale, 10, "#FA8072", "#FA8072")
    # Eyes
        canvas.draw_line((width/2 - 100, height/2 - 100), (width/2, height/2 - 100), 5, "Black")
        canvas.draw_circle([width/2 + 100, height/2 - 100], 40, 2, "Black", "White")
        canvas.draw_circle([width/2 + 100, height/2 - 100], 20, 2, "Black", "Black")
    # Smile
        canvas.draw_circle([width/2, height/2 + 50], 75, 5,"black")
        canvas.draw_polygon([(width/4, height/3 + 50),(3 * width/4,height/3+50),(3 * width/4, 2 * height/3), (width/4, 2 * height/3)], 2,
        "DarkOrange", "DarkOrange")
        
                
        
        
    if show_ellipse:
        canvas.draw_circle(((width/2)/2, (height/1.4)), (width/2 - 50)*scale, 10, "#FA8072", "#FA8072")
        canvas.draw_circle((200, 200), 30, 2, "Black", "White")
        canvas.draw_circle((400, 200), 30, 2, "Black", "White")
        canvas.draw_circle((200, 215), 15, 2, "Black", "Black")
        canvas.draw_circle((400, 215), 15, 2, "Black", "Black")
        canvas.draw_circle((200, 215), 4, 2, "White", "White")
        canvas.draw_circle((400, 215), 4, 2, "White", "White")
        canvas.draw_line((160, 180),(200, 150), 3, "Black")
        canvas.draw_line((200, 150),(240, 180), 3, "Black")
        canvas.draw_line((360, 180),(400, 150), 3, "Black")
        canvas.draw_line((400, 150),(440, 180), 3, "Black")
        canvas.draw_circle((300, 400), 30, 2, "Black", "Black")


def create_frame():
    global frame
    frame = simplegui.create_frame("CFU #17",width,height)
    frame.set_canvas_background("green")
    frame.add_button("triangle", hailey_emoji,100)
    frame.set_draw_handler(draw)
    frame.start() #starts the frame

create_frame()
