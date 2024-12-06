import simplegui
import math

# Global Variables

width = int(input("What is your width"))
height = int(input("What is your height"))
face1 = False
face2 = False
face3 = False
face4 = False
face5 = False

# Event Handlers

def all_false():
    global face1
    global face2
    global face3
    global face4
    global face5
    face1 = False
    face2 = False
    face3 = False
    face4 = False
    face5 = False
    
def toggle_face1():
    all_false()
    global face1
    face1 = not face1
    
def toggle_face2():
    all_false()
    global face2
    face2 = not face2
      
def toggle_face3():
    all_false()
    global face3
    face3 = not face3
    
def toggle_face4():
    all_false()
    global face4
    face4 = not face4

def toggle_face5():
    all_false()
    global face5
    face5 = not face5

def draw(canvas):
    if face1:
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "Yellow", "Yellow")
        canvas.draw_circle((width/3, height/3), width/8, 2, "Black", "White")
        canvas.draw_circle((width/1.5, height/3), width/8, 2, "Black", "White")
        canvas.draw_circle((width/3, height/3), width/16, 2, "Black", "Black")
        canvas.draw_circle((width/1.5, height/3), width/16, 2, "Black", "Black")
        canvas.draw_circle((width/3, height/3), width/64, 2, "White", "White")
        canvas.draw_circle((width/1.5, height/3), width/64, 2, "White", "White")
        canvas.draw_line((160, 180),(200, 150), 3, "Black")
        canvas.draw_line((200, 150),(240, 180), 3, "Black")
        canvas.draw_line((360, 180),(400, 150), 3, "Black")
        canvas.draw_line((400, 150),(440, 180), 3, "Black")
        canvas.draw_polygon([(142,341),(201,402),(290,440),(389,403),(453,336),(296,332)], 2, "Black","White")
        
    if face2:
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "#69e1ff", "#69e1ff")
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
        canvas.draw_polygon([(139,487),(193,398),(272,372),(349,376),(404,425),(426,494),(366,463),(295,444),(223,467)], 2, "Black","White")
        
    if face3:
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "#FA8072", "#FA8072")
        canvas.draw_circle([width/2.75, height/2 - 100], 10 , 10, "Black", "White")
        canvas.draw_circle([width - width/2.75, height/2 - 100], 10 , 10, "Black", "White")
        canvas.draw_line((width/3, height/2 - 150),(width/3 + 50, height/2 - 125), 5, "Black")
        canvas.draw_line((width - width/3, height/2 - 150),(width - width/3 - 50, height/2 - 125), 5, "Black")
        canvas.draw_polygon([(width/2, height - height/4), (width/2 - 50, height - height/4 + 25), (width/2 - 10, height - height/4 - 30), (width/2 + 10, height - height/4 - 30), (width/2 + 50, height - height/4 + 25)],10, "Black", "White")
        canvas.draw_line((width/2 - 30, height - height/4 - 10), (width/2 + 30, height - height/4 - 10), 5, "Black")

    if face4:
        canvas.draw_circle((300, 300), 250, 10, "#FCF4A3", "#FCF4A3")
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

    if face5:
        canvas.draw_circle((width/2, height/2), width/2 - 50, 10, "Yellow", "Yellow")
        canvas.draw_polygon([(195,86),(242,91),(245,133),(309,143),(328,203),(298,208),(253,186),(242,222),(245,265),(294,273),(326,292),(347,332),(343,385),(303,419),(253,429),(203,424),(165,410),(173,369),(202,373),(211,337),(213,306),(182,277),(139,267),(113,225),(126,153),(159,127),(184,163),(159,197),(197,229),(213,172),(257,319),(253,369),(299,359)], 2, "Black","Green")
        canvas.draw_polygon([(532,78),(483,71),(466,135),(413,150),(394,215),(425,259),(477,274),(479,333),(478,370),(438,378),(439,429),(492,433),(526,427),(564,392),(582,346),(573,279),(524,241),(522,193),(521,167),(565,169),(579,120),(516,121),(452,179),(441,211),(468,244),(481,184),(517,307),(516,361),(553,327)],2,"Black","Green")
        canvas.draw_polygon([(228,469),(304,511),(383,529),(455,503),(512,464),(502,528),(383,581),(283,558),(227,503)],2,"Black","White")

        
frame = simplegui.create_frame("Pictures", width, height) 

frame.set_draw_handler(draw)
frame.add_button("Happy", toggle_face1, 100)
frame.add_button("Sad", toggle_face2, 100)
frame.add_button("Angry", toggle_face3, 100)
frame.add_button("Surprised", toggle_face4, 100)
frame.add_button("Money", toggle_face5, 100)

# Remember to start the frame
frame.start()
