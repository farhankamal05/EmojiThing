import simplegui
width = int(input("Inital Width?"))
height = int(input("Inital Height?"))

show_hailey = False
show_marisa = False
show_malachi = False
show_farhan = False
together = False
scale = 0.4

frame = None #Global reference to the frame
    
    
def all_false():
    global show_hailey
    global show_marisa
    global show_malachi
    global show_farhan
    global together
    show_hailey = False
    show_marisa = False
    show_malachi = False
    show_farhan = False
    together = False
    
    
def toggle_hailey():
    all_false()
    global show_hailey
    show_hailey = not show_hailey
       
def toggle_marisa():
    all_false()
    global show_marisa
    show_marisa = not show_marisa
    
def toggle_malachi():
    all_false()
    global show_malachi
    show_malachi = not show_malachi
    
def toggle_farhan():
    all_false()
    global show_farhan
    show_farhan = not show_farhan

def toggle_together():
    all_false()
    global together
    together = not together
    
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
        canvas.draw_line([width-(width/3)-10,height/5],[width-(width/4)-5,height/5],5,"black")
        canvas.draw_line([width-(width/8),height/5],[width-(width/5),height/5],5,"black")
    #Mouth
        canvas.draw_circle([width/1.3,height/3],70*scale,2,"black")

        
    if show_malachi:
        canvas.draw_circle((((width/2)/2), (height/2)*1.5), (width/2 - 50)*scale, 10, "DarkOrange", "DarkOrange")
    # Eyes
        canvas.draw_line(((width/2 - 100)*0.4, (height/2)*1.4), ((width/2)*0.4, (height/2)*1.4), 5, "Black")
        canvas.draw_circle([width/2-100, (height/2)*1.4], 40*0.4, 2, "Black", "White")
        canvas.draw_circle([width/2-100, (height/2)*1.4], 20*0.4, 2, "Black", "Black")
    # Smile
        canvas.draw_circle([(width/2)/2, (height/2)*1.6], 60*0.4, 5,"black")
        canvas.draw_polygon([((width/7 , height/6 + 280)),((3 * (width/8)+10,height/6 + 280)),((3 * (width/8) +10 , 2 * height/6 + 240)), ((width/9 , 2 * height/6 + 240 ))], 2,
        "DarkOrange", "DarkOrange")
        
    if show_farhan:
        canvas.draw_circle((width-(width/2)/2, (height/2)*1.5), (width/2 - 50)*scale, 10, "Red", "Red")
        canvas.draw_circle((345,340 ), 40*0.4, 5, "Black", "Black")
        canvas.draw_circle((400,340), 40*0.4, 5, "Black", "Black")
        canvas.draw_line((350,380),(380,430), 5, "Black")
        canvas.draw_line((380,430),(410,380), 5, "Black")
        canvas.draw_circle((325,360), 20*0.4, 5, "Blue", "Blue")       


    if together:
        #hailey
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
        
        #marisa
        canvas.draw_circle((width-(width/2)/2, (height/2)/2), (width/2 - 50)*scale, 10, "Yellow", "Yellow")
        canvas.draw_line([width-(width/3)-10,height/5],[width-(width/4)-5,height/5],5,"black")
        canvas.draw_line([width-(width/8),height/5],[width-(width/5),height/5],5,"black")
    #Mouth
        canvas.draw_circle([width/1.3,height/3],70*scale,2,"black")
        
        #malachi
        canvas.draw_circle((((width/2)/2), (height/2)*1.5), (width/2 - 50)*scale, 10, "DarkOrange", "DarkOrange")
    # Eyes
        canvas.draw_line(((width/2 - 100)*0.4, (height/2)*1.4), ((width/2)*0.4, (height/2)*1.4), 5, "Black")
        canvas.draw_circle([width/2-100, (height/2)*1.4], 40*0.4, 2, "Black", "White")
        canvas.draw_circle([width/2-100, (height/2)*1.4], 20*0.4, 2, "Black", "Black")
    # Smile
        canvas.draw_circle([(width/2)/2, (height/2)*1.6], 60*0.4, 5,"black")
        canvas.draw_polygon([((width/7 , height/6 + 280)),((3 * (width/8)+10,height/6 + 280)),((3 * (width/8) +10 , 2 * height/6 + 240)), ((width/9 , 2 * height/6 + 240 ))], 2,
        "DarkOrange", "DarkOrange")
        
        #farhan
        canvas.draw_circle((width-(width/2)/2, (height/2)*1.5), (width/2 - 50)*scale, 10, "Red", "Red")
        canvas.draw_circle((345,340 ), 40*0.4, 5, "Black", "Black")
        canvas.draw_circle((400,340), 40*0.4, 5, "Black", "Black")
        canvas.draw_line((350,380),(380,430), 5, "Black")
        canvas.draw_line((380,430),(410,380), 5, "Black")
        canvas.draw_circle((325,360), 20*0.4, 5, "Blue", "Blue") 
        
def create_frame():
    global frame
    frame = simplegui.create_frame("CFU #17",width,height)
    frame.set_canvas_background("green")
    frame.add_button("Hailey", toggle_hailey,100)
    frame.add_button("Marisa",toggle_marisa,100)
    frame.add_button("Malachi", toggle_malachi,100)
    frame.add_button("Farhan", toggle_farhan,100)
    frame.add_button("All faces", toggle_together,100)
    frame.set_draw_handler(draw)
    frame.start() #starts the frame

create_frame()
