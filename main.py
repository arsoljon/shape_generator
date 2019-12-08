#shape generator




def setup():
    global x, y, fwd, x1, y1, x2, y2, coord1, coord2
    x = displayWidth
    y = displayHeight
    fwd = 30
    x1 = x/4
    y1 = y/4
    x2 = x/4
    y2 = (y/4) - fwd
    coord1 = [x1, y1]
    coord2 = [x2, y2]
    size(displayWidth/2, displayHeight/2)
    background(50)
    stroke(240, 230, 140)
    line(x1, y1, x2, y2)
    
def correctY():
    #used only for makeHoro() when point change is at the ends of a vertical line. 
    if(random(0,2) < 1):
        #top
        coord1[1] = coord2[1]
    else:
        #bottom
        coord2[1] = coord1[1]

def makeHoro():
    #Decide if line is created on top or bottom or center of the vertical line
    r = random(0,3)
    if(r > 2):
        coord1[0] -= fwd / 2
        coord2[0] += fwd / 2
        correctY()
    elif(r < 1):    
        #CENTER of vertical line
        ##move y points to correct center
        if(coord1[1] < coord2[1]):
            coord1[1] += fwd / 2
            coord2[1] = coord1[1]
        else:
            coord1[1] -= fwd / 2
            coord2[1] = coord1[1]
        ##decide to go left/right of vertical line. 
        if(random(0,2) < 1):
            coord2[0] -= fwd
        else:
            coord2[0] += fwd
    else:
        coord1[0] += fwd / 2
        coord2[0] -= fwd / 2
        correctY()
    
def correctX():
    #used only for makeVert() when point change is at the ends of a Horizontal line. 
    if(random(0,2) < 1):
        #right
        coord1[0] = coord2[0]
    else:
        #left?
        coord2[0] = coord1[0]

    
def makeVert():
    coord1[0] = coord1[0] + (fwd / 2)
    coord2[0] = coord1[0] 
    coord2[1] -= fwd 
    #Decide if line is created on left or right or center of the vertical line
    r = random(0,3)
    if(r > 2):
        coord1[1] -= fwd / 2
        coord2[1] += fwd / 2
        correctX()
    elif(r < 1):    
        #CENTER of horizontal line
        ##move x points to correct center 
        if(coord1[0] < coord2[0]):
            coord1[0] += fwd / 2
            coord2[0] = coord1[0]
        else:
            coord1[0] -= fwd / 2
            coord2[0] = coord1[0]
        ##decide to go up/down 
        if(random(0,2) < 1):
            coord2[1] -= fwd
        else:
            coord2[1] += fwd
    else:
        coord1[1] += fwd / 2
        coord2[1] -= fwd / 2
        correctX()

roy = 240
gee = 230
biv = 140
def draw():
    global x, y, fwd
    global coord1, coord2
    global x1, y1, x2, y2  #used for reset purposes only 
    global roy,gee,biv
    stroke(roy, gee, biv)
    mv1 = (False,False,False,False)
    mv2 = (False,False,False,False)
    #add a new line for as long as the mouse is being pressed. 
    if mousePressed:
        if(coord1[0] == coord2[0]):  #line is vertical, shift to horizontal 
            #make line horizontal. y coordinates stay the same. 
            makeHoro()
        else:  #line is horizontal, shift to vertical 
            makeVert()
        line(coord1[0], coord1[1], coord2[0], coord2[1])

    #randomly decide which point to make the new x1 & y1 coordinates
        
    #reset
    if( (coord1[0] > x / 2) or (coord1[1] > y / 2) or (coord2[0] < 0)or (coord2[1] < 0) ):
        coord1[0] = x1
        coord1[1] = y1
        coord2[0] = x2
        coord2[1] = y2
        #background(50) #clears screen
        roy = random(250)
        gee = random(250)
        biv = random(250)
        line(x1, y1, x2, y2) #starting line. 
        
    
  
            
    
#12/6 made lines move up shifting from vertical to horizontal
    #GOAL: make lines randomly appear along either side or point of a given line. 
        #  Dont repeat lines. 
        #  if any line touches another line, stop the loop and shade that area 
        #  This will represent the new shape created. 

    
