import simplegui
width = int(input("Inital Width?"))
height = int(input("Inital Height?"))

show_hailey = False
show_marisa = False
show_malachi = False
show_farhan = False
scale = 0.4

frame = None #Global reference to the frame
    
    
def all_false():
    global show_hailey
    global show_marisa
    global show_malachi
    global show_farhan
    show_hailey = False
    show_marisa = False
    show_malachi = False
    show_farhan = False
    
    
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
        
    if show_malachi:
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "DarkOrange", "DarkOrange")
    # Eyes
        canvas.draw_line((width/2 - 100, height/2 - 100), (width/2, height/2 - 100), 5, "Black")
        canvas.draw_circle([width/2 + 100, height/2 - 100], 40, 2, "Black", "White")
        canvas.draw_circle([width/2 + 100, height/2 - 100], 20, 2, "Black", "Black")
    # Smile
        canvas.draw_circle([width/2, height/2 + 50], 75, 5,"black")
        canvas.draw_polygon([(width/4, height/3 + 50),(3 * width/4,height/3+50),(3 * width/4, 2 * height/3), (width/4, 2 * height/3)], 2,
        "DarkOrange", "DarkOrange")
        
    if show_farhan:
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "Yellow", "Yellow")
        canvas.draw_polygon([(195,86),(242,91),(245,133),(309,143),(328,203),(298,208),(253,186),(242,222),(245,265),(294,273),(326,292),(347,332),(343,385),(303,419),(253,429),(203,424),(165,410),(173,369),(202,373),(211,337),(213,306),(182,277),(139,267),(113,225),(126,153),(159,127),(184,163),(159,197),(197,229),(213,172),(257,319),(253,369),(299,359)], 2, "Black","Green")
        canvas.draw_polygon([(532,78),(483,71),(466,135),(413,150),(394,215),(425,259),(477,274),(479,333),(478,370),(438,378),(439,429),(492,433),(526,427),(564,392),(582,346),(573,279),(524,241),(522,193),(521,167),(565,169),(579,120),(516,121),(452,179),(441,211),(468,244),(481,184),(517,307),(516,361),(553,327)],2,"Black","Green")
        canvas.draw_polygon([(228,469),(304,511),(383,529),(455,503),(512,464),(502,528),(383,581),(283,558),(227,503)],2,"Black","White")
       


def create_frame():
    global frame
    frame = simplegui.create_frame("CFU #17",width,height)
    frame.set_canvas_background("green")
    frame.add_button("Hailey", toggle_hailey,100)
    frame.add_button("Marisa",toggle_marisa,100)
    frame.add_button("Malachi", toggle_malachi,100)
    frame.add_button("Farhan", toggle_farhan,100)
    frame.set_draw_handler(draw)
    frame.start() #starts the frame

create_frame()
