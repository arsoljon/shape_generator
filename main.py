#shape generator

def setup():
    global x, y, fwd, x1, y1, x2, y2, coord1, coord2, bkcolor
    x = displayWidth
    y = displayHeight
    fwd = 10
    x1 = x/4
    y1 = y/4
    x2 = x1
    y2 = y1 - fwd
    coord1 = [x1, y1]
    coord2 = [x2, y2]
    size(displayWidth/2, displayHeight/2)
    bkcolor = 50
    background(bkcolor)
    stroke(240, 230, 140)
    line(x1, y1, x2, y2)

#Used for makeHoro()
def correctY():
    if(random(0,2) < 1):
        #Choose top vertical line
        coord1[1] = coord2[1]
    else:
        #bottom
        coord2[1] = coord1[1]

#Decide if line is created on top or bottom or center of the vertical line
def makeHoro():
    r = random(0,3)
    if(r > 2):
        coord1[0] -= fwd / 2
        coord2[0] = coord1[0] + fwd
        correctY()
    elif(r < 1):    
        #CENTER of vertical line
        ##move y points to correct center
        if(coord1[1] < coord2[1]):
            coord1[1] += abs(coord1[1] - coord2[1])
            coord2[1] = coord1[1]
        else:
            coord1[1] -= abs(coord1[1] - coord2[1])
            coord2[1] = coord1[1]
        ##decide to go left/right of vertical line. 
        if(random(0,2) < 1):
            coord2[0] -= fwd
        else:
            coord2[0] += fwd
    else:
        coord1[0] += fwd / 2
        coord2[0] = coord1[0] - fwd
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
    #Decide if line is created on left or right or center of the vertical line
    r = random(0,3)
    if(r > 2):
        coord1[1] -= fwd / 2
        coord2[1] = coord1[1] + fwd
        correctX()
    elif(r < 1):    
        #CENTER of horizontal line
        ##move x points to correct center 
        if(coord1[0] < coord2[0]):
            coord1[0] += abs(coord1[0] - coord2[0])
            coord2[0] = coord1[0]
        else:
            coord1[0] -= abs(coord1[0] - coord2[0])
            coord2[0] = coord1[0]
        ##decide to go up/down 
        if(random(0,2) < 1):
            coord2[1] -= fwd
        else:
            coord2[1] += fwd
    else:
        coord1[1] += fwd / 2
        coord2[1] = coord1[1] - fwd 
        correctX()
        
def reset():
    #if any of the coordinates reach beyond screen size
    #if( (coord1[0] > x / 2) or (coord1[1] > y / 2) or (coord2[0] < 0)or (coord2[1] < 0) ):
        coord1[0] = x1
        coord1[1] = y1
        coord2[0] = x2
        coord2[1] = y2
        global bkcolor
        #background(bkcolor) #clears screen
        return True

roy = 240
gee = 230
biv = 140
def draw():
    global x, y, fwd
    global coord1, coord2
    global x1, y1, x2, y2  #used for reset purposes only 
    global roy,gee,biv
    stroke(roy, gee, biv)
    #Condition here for debugging purposes.  
    if True:
        #make a 3rd case to tilt the line 45 degrees. 
        if(random(0,4) > 3):
            pass
        elif(coord1[0] == coord2[0]):  #line is vertical, shift to horizontal 
            #make line horizontal. y coordinates stay the same. 
            makeHoro()
        else:  #line is horizontal, shift to vertical 
            makeVert()
        line(coord1[0], coord1[1], coord2[0], coord2[1])

    if mousePressed:
        reset()
        roy = random(250)
        gee = random(250)
        biv = random(250)
        line(x1, y1, x2, y2) #starting line.
    
  
            
    
#12/6 made lines move up shifting from vertical to horizontal
#12/8 corrected horizontal and vertical shifts. However, only goes towards one corner
##and has weird behavior of creating a newline with empty space beforehand. 
#12/9 edited the first and last if/else statements of make horo/vert()
##Changing x2/y2 relevant to the change made to x1/y1 beforehand. 
    #GOAL: make lines randomly appear along either side or point of a given line. 
        #  Dont repeat lines. 
        #  if any line touches another line, stop the loop and shade that area 
        #  This will represent the new shape created. 

    
