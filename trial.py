#CFU17
#Marisa Ramautar
#12/6/24
#Period 5-6
#scaling code for scaling images

import simplegui
width = int(input("Inital Width?"))
height = int(input("Inital Height?"))

show_hailey = False
show_marisa = False
scale = 0.4

frame = None #Global reference to the frame
    
    
def all_false():
    global show_hailey
    global show_marisa
    show_hailey = False
    show_marisa = False

    
def toggle_hailey():
    all_false()
    global show_hailey
    show_hailey = not show_hailey
       
def toggle_marisa():
    all_false()
    global show_marisa
    show_marisa = not show_marisa
    

    
def draw(canvas):
    
    if show_hailey:
        canvas.draw_circle(((width/2)/2, (height/2)/2), (width/2 - 50)*scale, 10, "Yellow", "Yellow")
       
        # Right eye (winking)
        canvas.draw_circle([width/3, height/6], 60*scale, 2, "Black", "yellow")
        canvas.draw_circle([width/3, height/5.5], 62.5*scale, 2, "yellow", "yellow")
       
        # Left eye (open)
        canvas.draw_circle([width/6, height/6], 60*scale, 2, "black", "white")
        canvas.draw_circle([width/6, height/6], 15*scale, 2, "black", "black")
       
        # Big smiling mouth
        canvas.draw_circle([width/4, height/3.5 + 30], 75*scale, 2, "black","black")
        canvas.draw_circle([width/4, height/4.5 + 30], 75*scale, 2, "yellow", "yellow")
     

       
    if show_marisa:
        canvas.draw_circle((width-(width/2)/2, (height/2)/2), (width/2 - 50)*scale, 10, "Yellow", "Yellow")
        canvas.draw_line([width/6,height/3],[width/3,height/3],5*scale,"white")
        canvas.draw_line([width-(width/6),height/3],[width-(width/3),height/3],5,"black")
    #Mouth
        canvas.draw_circle([width/2,height/2+70],90,2,"black")
        canvas.draw_polygon([(width/1,height/1),(width/2,height/1),
        (width/4,5*height/3),(width/4,5*height/3)],2,"yellow","yellow")
        
        
        
       


def create_frame():
    global frame
    frame = simplegui.create_frame("CFU #17",width,height)
    frame.set_canvas_background("green")
    frame.add_button("Hailey", toggle_hailey,100)
    frame.add_button("Marisa",toggle_marisa,100)
    frame.set_draw_handler(draw)
    frame.start() #starts the frame

create_frame()
