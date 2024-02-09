from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


#truck = [350, 0]  #[350, 0, 350, 200]
truck = {'x':400, 'y':400, 'direction':'up'}
#houseOriginalColors = [[[218/255, 165/255, 32/255], [184/255, 134/255, 30/255]], [[255/255, 0/255, 128/255], [128/255, 0/255, 64/255]], [[191/255, 0/255, 255/255], [115/255, 0/255, 153/255]], [[51/255, 102/255, 255/255], [0/255, 45/255, 179/255]], [[138/255, 138/255, 92/255], [92/255, 92/255, 61/255]], [[117/255, 117/255, 163/255], [71/255, 71/255, 107/255]]]
#houseColors = [[[218/255, 165/255, 32/255], [184/255, 134/255, 30/255]], [[255/255, 0/255, 128/255], [128/255, 0/255, 64/255]], [[191/255, 0/255, 255/255], [115/255, 0/255, 153/255]], [[51/255, 102/255, 255/255], [0/255, 45/255, 179/255]], [[138/255, 138/255, 92/255], [92/255, 92/255, 61/255]], [[117/255, 117/255, 163/255], [71/255, 71/255, 107/255]]]

house_li = [
    { 'x':0,'y':0, 'health':100, 'cond':'normal', 'color': [[218/255, 165/255, 32/255], [184/255, 134/255, 30/255]], 'originalColor': [[218/255, 165/255, 32/255], [184/255, 134/255, 30/255]]},
    { 'x':0,'y':250, 'health':100, 'cond':'normal', 'color':[[255/255, 0/255, 128/255], [128/255, 0/255, 64/255]], 'originalColor':[[255/255, 0/255, 128/255], [128/255, 0/255, 64/255]]},
    { 'x':0,'y':500, 'health':100, 'cond':'normal', 'color':[[191/255, 0/255, 255/255], [115/255, 0/255, 153/255]], 'originalColor':[[191/255, 0/255, 255/255], [115/255, 0/255, 153/255]] },
    { 'x':650,'y':0, 'health':100, 'cond':'normal', 'color': [[51/255, 102/255, 255/255], [0/255, 45/255, 179/255]], 'originalColor':[[51/255, 102/255, 255/255], [0/255, 45/255, 179/255]]},
    { 'x':650,'y':250, 'health':100, 'cond':'normal', 'color':[[138/255, 138/255, 92/255], [92/255, 92/255, 61/255]], 'originalColor':[[138/255, 138/255, 92/255], [92/255, 92/255, 61/255]] },
    { 'x':650,'y':500, 'health':100, 'cond':'normal', 'color':[[117/255, 117/255, 163/255], [71/255, 71/255, 107/255]], 'originalColor':[[117/255, 117/255, 163/255], [71/255, 71/255, 107/255]] }
]

houseHealth = [[25, 160, 25+house_li[0]['health'], 160], [25, 410, 25+house_li[1]['health'], 410], [25, 660, 25+house_li[2]['health'], 660], [670, 160, 670+house_li[3]['health'], 160], [670, 410, 670+house_li[4]['health'], 410], [670, 660, 670+house_li[5]['health'], 660]]
#house_li[0]['cond']='fire'
fireTimer = 100
water = -1
score = 0
fast_travel_left = 3
gameover = -1
restart = -1
speed = 0
pause = -1

#################### Mid point line and circle algorithm:
def drawPoint(x, y):
    
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

def findZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        elif dx <= 0 and dy >= 0:
            return 3
        elif dx <= 0 and dy <= 0:
            return 4
        elif dx >= 0 and dy <= 0:
            return 7
    else:
        if dx >= 0 and dy >= 0:
            return 1
        elif dx <= 0 and dy >= 0:
            return 2
        elif dx <= 0 and dy <= 0:
            return 5
        elif dx >= 0 and dy <= 0:
            return 6
        
def convertToZone0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y

def convertToOriginalZone(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y

def MidPointLineAlgorithm(x1, y1, x2, y2):
    zone = findZone(x1, y1, x2, y2)

    x1, y1 = convertToZone0(x1, y1, zone)
    x2, y2 = convertToZone0(x2, y2, zone)

    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    dE = 2 * dy
    dNE = 2 * (dy - dx)
    x = x1
    y = y1
    while(x <= x2):
        x_original, y_original = convertToOriginalZone(x, y, zone)
        drawPoint(x_original, y_original)
        x += 1
        if d > 0:
            d += dNE
            y = y + 1
        else:
            d += dE

def drawPoints(x, y, dx, dy):
    #global circles
    #print(circles)
    #if ((-375 <= x+dx <= 375) and (-375 <= -x+dx <= 375) and (-375 <= y+dx <= 375) and (-375 <= -y+dx <= 375) and (-375 <= y+dy <= 375) and (-375 <= -y+dy <= 375) and (-375 <= -x+dy <= 375) and (-375 <= x+dy <= 375)):
    drawPoint(x+dx, y+dy)
    drawPoint(-x+dx, y+dy)
    drawPoint(-x+dx, -y+dy)
    drawPoint(x+dx, -y+dy)
    drawPoint(y+dx, x+dy)
    drawPoint(-y+dx, x+dy)
    drawPoint(-y+dx, -x+dy)
    drawPoint(y+dx, -x+dy)

def MidPointCircleAlgorithm(x, y, r):
    x0 = 0
    y0 = r
    d = 1-r
    drawPoints(x0, y0, x, y)
    while (x0 < y0):
        if (d < 0):
            d += (2*x0 + 3)
            x0 += 1
        else:
            d += ((2*x0) - (2*y0) + 5)
            x0 += 1
            y0 -= 1
        drawPoints(x0, y0, x, y)

###########################################################################
def buildHouse(x1, y1, color1, color2):
    glPointSize(3)
    glColor3f(*color1)
    MidPointLineAlgorithm(x1+25, y1+20, x1+25, y1+135)
    MidPointLineAlgorithm(x1+25, y1+135, x1+135, y1+135)
    MidPointLineAlgorithm(x1+135, y1+135, x1+135, y1+20)
    glPointSize(10)
    MidPointLineAlgorithm(x1+30, y1+130, x1+130, y1+130)
    MidPointLineAlgorithm(x1+30, y1+120, x1+130, y1+120)
    MidPointLineAlgorithm(x1+30, y1+110, x1+30, y1+30)
    MidPointLineAlgorithm(x1+60, y1+110, x1+60, y1+30)
    MidPointLineAlgorithm(x1+70, y1+110, x1+70, y1+30)
    MidPointLineAlgorithm(x1+80, y1+110, x1+80, y1+30)
    MidPointLineAlgorithm(x1+90, y1+110, x1+90, y1+30)
    MidPointLineAlgorithm(x1+100, y1+110, x1+100, y1+30)
    MidPointLineAlgorithm(x1+130, y1+110, x1+130, y1+30)
    MidPointLineAlgorithm(x1+30, y1+90, x1+130, y1+90)
    MidPointLineAlgorithm(x1+30, y1+80, x1+130, y1+80)
    MidPointLineAlgorithm(x1+30, y1+50, x1+130, y1+50)
    MidPointLineAlgorithm(x1+30, y1+20, x1+130, y1+20)
    glPointSize(3)
    glColor3f(*color2)
    MidPointLineAlgorithm(x1+25, y1+135, x1+17, y1+120)
    MidPointLineAlgorithm(x1+17, y1+120, x1+17, y1+25)
    glPointSize(8)
    MidPointLineAlgorithm(x1+19, y1+120, x1+19, y1+25)
    glPointSize(5)
    MidPointLineAlgorithm(x1+25, y1+130, x1+25, y1+20)

def buildHouses():
    global houseHealth, pause, gameover
    #global houseColors
    global house_li
    # House Serial: Bottom Left to Top Left, then, Bottom Right to Top Right
    #buildHouse(0, 0,  houseColors[0][0], houseColors[0][1])
    #buildHouse(0, 250,  houseColors[1][0], houseColors[1][1])
    #buildHouse(0, 500,  houseColors[2][0], houseColors[2][1])
    #buildHouse(650, 0,  houseColors[3][0], houseColors[3][1])
    #buildHouse(650, 250,  houseColors[4][0], houseColors[4][1])
    #buildHouse(650, 500,  houseColors[5][0], houseColors[5][1])

    #buildHouse(house_li[0]['x'], house_li[0]['y'],  houseColors[0][0], houseColors[0][1])
    #buildHouse(house_li[1]['x'], house_li[1]['y'],  houseColors[1][0], houseColors[1][1])
    #buildHouse(house_li[2]['x'], house_li[2]['y'],  houseColors[2][0], houseColors[2][1])
    #buildHouse(house_li[3]['x'], house_li[3]['y'],  houseColors[3][0], houseColors[3][1])
    #buildHouse(house_li[4]['x'], house_li[4]['y'],  houseColors[4][0], houseColors[4][1])
    #buildHouse(house_li[5]['x'], house_li[5]['y'],  houseColors[5][0], houseColors[5][1])

    
    for house in house_li:
        if(gameover==-1 and pause==-1):
            if(house['cond'] == 'fire'):
                house['color'] = [[1,0,0],[0.4, 0, 0]] 
                house['health'] -= 1  #1  #0.001
                #print(house['health'])        

            if(house['cond']=='fire' and house['health'] <= 5):
                house['cond'] = 'burnt'     
                house['health'] = 0
            
            if(house['cond'] == 'burnt'):
                house['color'] = [[0.7,0.7,0.7],[0.7, 0.7, 0.7]]

        buildHouse(house['x'], house['y'], house['color'][0], house['color'][1] )

def showHouseHealth():
    global houseHealth
    for i in range(len(houseHealth)):
        glPointSize(15)
        glColor3f(1, 0, 0)
        MidPointLineAlgorithm(houseHealth[i][0], houseHealth[i][1], houseHealth[i][2], houseHealth[i][3])


angle = 0
def showTruck():
    global angle, truck
    tx=-40
    ty=-75
    glTranslatef(truck['x'], truck['y'], 0.0)  # change position from 0,0
    glRotatef(angle, 0, 0, 1)  # change angle of object

    glPointSize(5)
    glColor3f(0, 0, 0)
    MidPointCircleAlgorithm(tx, ty+30, 5)
    MidPointCircleAlgorithm(tx, ty+15, 5)
    MidPointCircleAlgorithm(tx, ty+80, 5)
    MidPointCircleAlgorithm(tx, ty+95, 5)
    MidPointCircleAlgorithm(tx+80, ty+30, 5)
    MidPointCircleAlgorithm(tx+80, ty+15, 5)
    MidPointCircleAlgorithm(tx+80, ty+80, 5)
    MidPointCircleAlgorithm(tx+80, ty+95, 5)
    glPointSize(4)
    glColor3f(0, 0, 0)
    MidPointLineAlgorithm(tx, ty, tx, ty+120)
    MidPointLineAlgorithm(tx, ty+120, tx+80, ty+120)
    MidPointLineAlgorithm(tx+80, ty+120, tx+80, ty)
    MidPointLineAlgorithm(tx, ty, tx+80, ty)

    if(gameover==-1):
        glColor3f(179/255, 0, 0)
    else:
        glColor3f(0.2, 0.2, 0.2)
    glPointSize(20)
    MidPointLineAlgorithm(tx+10, ty+130, tx+10, ty+140)
    MidPointLineAlgorithm(tx+30, ty+130, tx+30, ty+140)
    MidPointLineAlgorithm(tx+50, ty+130, tx+50, ty+140)
    MidPointLineAlgorithm(tx+70, ty+130, tx+70, ty+140)
    glPointSize(5)
    glColor3f(0, 0, 0)
    MidPointLineAlgorithm(tx, ty+120, tx+80, ty+120)
    MidPointLineAlgorithm(tx, ty+150, tx+80, ty+150)
    MidPointLineAlgorithm(tx, ty+120, tx, ty+150)
    MidPointLineAlgorithm(tx+80, ty+150, tx+80, ty+120)
    glColor3f(204/255, 204/255, 204/255)
    MidPointCircleAlgorithm(tx+10, ty+140, 3)
    MidPointCircleAlgorithm(tx+70, ty+140, 3)

    glPointSize(20)
    if(gameover==-1):
        glColor3f(200/255, 0, 0)
    else:
        glColor3f(0.2, 0.2, 0.2)
    MidPointLineAlgorithm(tx+10, ty+5, tx+10, ty+105)
    #glColor3f(200/255, 0, 0) #
    MidPointLineAlgorithm(tx+20, ty+5, tx+20, ty+105)
    #glColor3f(200/255, 0, 0)
    MidPointLineAlgorithm(tx+30, ty+5, tx+30, ty+105)
    #glColor3f(200/255, 0, 0) #
    MidPointLineAlgorithm(tx+40, ty+5, tx+40, ty+105)
    #glColor3f(200/255, 0, 0)
    MidPointLineAlgorithm(tx+50, ty+5, tx+50, ty+105)
    #glColor3f(200/255, 0, 0) #
    MidPointLineAlgorithm(tx+60, ty+5, tx+60, ty+105)
    #glColor3f(200/255, 0, 0)
    MidPointLineAlgorithm(tx+70, ty+5, tx+70, ty+105)
    #glColor3f(200/255, 0, 0) #
    MidPointLineAlgorithm(tx+60, ty+5, tx+60, ty+105)
    glPointSize(5)
    if(gameover==-1):
        glColor3f(200/255, 51/255, 51/255)
    else:
        glColor3f(0.2, 0.2, 0.2)
    MidPointCircleAlgorithm(tx+40, ty+135, 3)
    glColor3f(0, 0, 0)


    MidPointLineAlgorithm(tx+10, ty+105, tx+10, ty+10)
    MidPointLineAlgorithm(tx+20, ty+105, tx+20, ty+10)
    MidPointLineAlgorithm(tx+30, ty+105, tx+30, ty+10)
    MidPointLineAlgorithm(tx+40, ty+105, tx+40, ty+10)
    MidPointLineAlgorithm(tx+50, ty+105, tx+50, ty+10)
    MidPointLineAlgorithm(tx+60, ty+105, tx+60, ty+10)
    MidPointLineAlgorithm(tx+70, ty+105, tx+70, ty+10)

    #glPointSize(5)
    #glColor3f(0, 0, 0)
    #MidPointCircleAlgorithm(truck['x'], truck['y']+30, 5)
    #MidPointCircleAlgorithm(truck['x'], truck['y']+15, 5)
    #MidPointCircleAlgorithm(truck['x'], truck['y']+80, 5)
    #MidPointCircleAlgorithm(truck['x'], truck['y']+95, 5)
    #MidPointCircleAlgorithm(truck['x']+80, truck['y']+30, 5)
    #MidPointCircleAlgorithm(truck['x']+80, truck['y']+15, 5)
    #MidPointCircleAlgorithm(truck['x']+80, truck['y']+80, 5)
    #MidPointCircleAlgorithm(truck['x']+80, truck['y']+95, 5)
    #glPointSize(4)
    #glColor3f(0, 0, 0)
    #MidPointLineAlgorithm(truck['x'], truck['y'], truck['x'], truck['y']+120)
    #MidPointLineAlgorithm(truck['x'], truck['y']+120, truck['x']+80, truck['y']+120)
    #MidPointLineAlgorithm(truck['x']+80, truck['y']+120, truck['x']+80, truck['y'])
    #MidPointLineAlgorithm(truck['x'], truck['y'], truck['x']+80, truck['y'])

    #glColor3f(179/255, 0, 0)
    #glPointSize(20)
    #MidPointLineAlgorithm(truck['x']+10, truck['y']+130, truck['x']+10, truck['y']+140)
    #MidPointLineAlgorithm(truck['x']+30, truck['y']+130, truck['x']+30, truck['y']+140)
    #MidPointLineAlgorithm(truck['x']+50, truck['y']+130, truck['x']+50, truck['y']+140)
    #MidPointLineAlgorithm(truck['x']+70, truck['y']+130, truck['x']+70, truck['y']+140)
    #glPointSize(5)
    #glColor3f(0, 0, 0)
    #MidPointLineAlgorithm(truck['x'], truck['y']+120, truck['x']+80, truck['y']+120)
    #MidPointLineAlgorithm(truck['x'], truck['y']+150, truck['x']+80, truck['y']+150)
    #MidPointLineAlgorithm(truck['x'], truck['y']+120, truck['x'], truck['y']+150)
    #MidPointLineAlgorithm(truck['x']+80, truck['y']+150, truck['x']+80, truck['y']+120)
    #glColor3f(204/255, 204/255, 204/255)
    #MidPointCircleAlgorithm(truck['x']+10, truck['y']+140, 3)
    #MidPointCircleAlgorithm(truck['x']+70, truck['y']+140, 3)

    #glPointSize(20)
    #glColor3f(200/255, 0, 0)
    #MidPointLineAlgorithm(truck['x']+10, truck['y']+5, truck['x']+10, truck['y']+105)
    #glColor3f(200/255, 0, 0) #
    #MidPointLineAlgorithm(truck['x']+20, truck['y']+5, truck['x']+20, truck['y']+105)
    #glColor3f(200/255, 0, 0)
    #MidPointLineAlgorithm(truck['x']+30, truck['y']+5, truck['x']+30, truck['y']+105)
    #glColor3f(200/255, 0, 0) #
    #MidPointLineAlgorithm(truck['x']+40, truck['y']+5, truck['x']+40, truck['y']+105)
    #glColor3f(200/255, 0, 0)
    #MidPointLineAlgorithm(truck['x']+50, truck['y']+5, truck['x']+50, truck['y']+105)
    #glColor3f(200/255, 0, 0) #
    #MidPointLineAlgorithm(truck['x']+60, truck['y']+5, truck['x']+60, truck['y']+105)
    #glColor3f(200/255, 0, 0)
    #MidPointLineAlgorithm(truck['x']+70, truck['y']+5, truck['x']+70, truck['y']+105)
    #glColor3f(200/255, 0, 0) #
    #MidPointLineAlgorithm(truck['x']+60, truck['y']+5, truck['x']+60, truck['y']+105)
    #glPointSize(5)
    #glColor3f(200/255, 51/255, 51/255)
    #MidPointCircleAlgorithm(truck['x']+40, truck['y']+135, 3)
    #glColor3f(0, 0, 0)


    #MidPointLineAlgorithm(truck['x']+10, truck['y']+105, truck['x']+10, truck['y']+10)
    #MidPointLineAlgorithm(truck['x']+20, truck['y']+105, truck['x']+20, truck['y']+10)
    #MidPointLineAlgorithm(truck['x']+30, truck['y']+105, truck['x']+30, truck['y']+10)
    #MidPointLineAlgorithm(truck['x']+40, truck['y']+105, truck['x']+40, truck['y']+10)
    #MidPointLineAlgorithm(truck['x']+50, truck['y']+105, truck['x']+50, truck['y']+10)
    #MidPointLineAlgorithm(truck['x']+60, truck['y']+105, truck['x']+60, truck['y']+10)
    #MidPointLineAlgorithm(truck['x']+70, truck['y']+105, truck['x']+70, truck['y']+10)

def showWater():
    #global angle, truck
    ##glTranslatef(truck['x'], truck['y'], 0.0)  # change position from 0,0
    #glRotatef(angle, 0, 0, 1)  # change angle of object
    #tx=-40
    #ty=-75
    MidPointCircleAlgorithm(0, 110, 20)
    MidPointCircleAlgorithm(-20, 140, 10)
    MidPointCircleAlgorithm(20, 150, 15)
    MidPointCircleAlgorithm(-5, 165, 13)

def show_cross():
    MidPointLineAlgorithm(745, 745,  775, 775)
    MidPointLineAlgorithm(775, 745,  745, 775)

def show_restart():
    #glColor3f(0.5, 1.0, 1.0)
    MidPointLineAlgorithm(20, 760,  50, 760)
    MidPointLineAlgorithm(20, 760,  35, 770)
    MidPointLineAlgorithm(20, 760,  35, 750)

def show_pause():
    MidPointLineAlgorithm(395, 745,  395, 775)
    MidPointLineAlgorithm(405, 745,  405, 775)

def show_play():
    MidPointLineAlgorithm(395, 745,  395, 775)
    MidPointLineAlgorithm(395, 745,  415, 760)
    MidPointLineAlgorithm(395, 775,  415, 760)

#########################################################################################

def specialKeyListener(key, x, y):
    global angle, truck, water, pause, gameover

    if(gameover==-1 and pause==-1):
        if key==GLUT_KEY_RIGHT:
            angle=-90
            if(truck['x']+30 <= 580):
                truck['x'] += 30
            truck['direction'] = 'right'
            water = -1
        if key== GLUT_KEY_LEFT:	 
            angle=90
            if(truck['x']-30 >= 220):
                truck['x'] -= 30
            truck['direction'] = 'left'
            water = -1
        if key== GLUT_KEY_UP:	 
            angle=0
            if(truck['y']+30 <= 650):
                truck['y'] += 30
            truck['direction'] = 'up'
            water = -1
        if key== GLUT_KEY_DOWN:	 
            angle=180
            truck['y'] -= 30
            truck['direction'] = 'down'
            water = -1

    #print(truck['direction'])
    #print(truck['x'], truck['y'])
    glutPostRedisplay()

def keyboardListener(key, x, y):
    global water, gameover, pause
    if(gameover==-1 and pause==-1):
        if key==b' ':
            water = -water
    glutPostRedisplay()

def mouseListener(button, state, x, y):	
    global truck, fast_travel_left, score, restart, pause, gameover
    if button==GLUT_LEFT_BUTTON:
        if(state == GLUT_DOWN):    
            #print(x,y)	
            if(x>=220 and x<=580 and y>=150 and fast_travel_left>0 and gameover==-1 and pause==-1):
                truck['x'] = x
                truck['y'] = 800-y # convert mouse coordinate 
                fast_travel_left-=1
            print("Fast Travel Left:", fast_travel_left)

            #print(x, y)
            if( x>730 and y<60 ):
                print("Goodbye! Score:", score)
                glutLeaveMainLoop()

            if( x<=60 and y<=60 ): 
                #print('in')
                restart = 1
            
            if( x>378 and y<65 and x<420 ): 
                #print('in')
                pause = -pause

    glutPostRedisplay()

def animate():
    glutPostRedisplay()
    global fireTimer, houseHealth, water, score, fast_travel_left, gameover, truck, house_li, restart, printGameOver, speed, pause
    speed += 0.005

    if(gameover==-1 and pause==-1):
    
        if(fireTimer<=0):
            random_integer = random.randint(0, 5)
            #print(random_integer)
            house_li[random_integer]['cond'] = 'fire'
            fireTimer=100
        fireTimer -= (3+speed)  #0.0075

        houseHealth = [[25, 160, 25+house_li[0]['health'], 160], [25, 410, 25+house_li[1]['health'], 410], [25, 660, 25+house_li[2]['health'], 660], [670, 160, 670+house_li[3]['health'], 160], [670, 410, 670+house_li[4]['health'], 410], [670, 660, 670+house_li[5]['health'], 660]]

        # checking if water is inside house on fire
        if(  (truck['y']<=130) and (truck['y']>=10) and (truck['direction']=='left') ):
            if( (truck['x']<=310) and water==1 and house_li[0]['cond']!='burnt'):
                #print("in")
                if(house_li[0]['health'] <= 95):
                    house_li[0]['health'] += 3 #0.01
                    if(house_li[0]['health']>=95):
                        house_li[0]['cond'] = 'normal'
                        score += 1
                        print('Score:', score)
                        house_li[0]['health'] = 100
                        house_li[0]['color'] = house_li[0]['originalColor']
        
        if(  (truck['y']<=400) and (truck['y']>=280) and (truck['direction']=='left') ):
            if( (truck['x']<=310) and water==1 and house_li[1]['cond']!='burnt'):
                #print("in")
                if(house_li[1]['health'] <= 95):
                    house_li[1]['health'] += 3 #0.01
                    if(house_li[1]['health']>=95):
                        house_li[1]['cond'] = 'normal'
                        score += 1
                        print('Score:',score)
                        house_li[1]['health'] = 100
                        house_li[1]['color'] = house_li[1]['originalColor']

        if(  (truck['y']<=640) and (truck['y']>=520) and (truck['direction']=='left') ):
            if( (truck['x']<=310) and water==1 and house_li[2]['cond']!='burnt'):
                #print("in")
                if(house_li[2]['health'] <= 95):
                    house_li[2]['health'] += 3 #0.01
                    if(house_li[2]['health']>=95):
                        house_li[2]['cond'] = 'normal'
                        score += 1
                        print('Score:',score)
                        house_li[2]['health'] = 100
                        house_li[2]['color'] = house_li[2]['originalColor']

        if(  (truck['y']<=130) and (truck['y']>=10) and (truck['direction']=='right') ):
            if( (truck['x']>=490) and water==1 and house_li[3]['cond']!='burnt'):
                #print("in")
                if(house_li[3]['health'] <= 95):
                    house_li[3]['health'] += 3 #0.01
                    if(house_li[3]['health']>=95):
                        house_li[3]['cond'] = 'normal'
                        score += 1
                        print('Score:',score)
                        house_li[3]['health'] = 100
                        house_li[3]['color'] = house_li[3]['originalColor']

        if(  (truck['y']<=370) and (truck['y']>=250) and (truck['direction']=='right') ):
            if( (truck['x']>=490) and water==1 and house_li[4]['cond']!='burnt'):
                #print("in")
                if(house_li[4]['health'] <= 95):
                    house_li[4]['health'] += 3 #0.01
                    if(house_li[4]['health']>=95):
                        house_li[4]['cond'] = 'normal'
                        score += 1
                        print('Score:',score)
                        house_li[4]['health'] = 100
                        house_li[4]['color'] = house_li[4]['originalColor']
        if(  (truck['y']<=640) and (truck['y']>=490) and (truck['direction']=='right') ):
            if( (truck['x']>=490) and water==1 and house_li[5]['cond']!='burnt'):
                #print("in")
                if(house_li[5]['health'] <= 95):
                    house_li[5]['health'] += 3 #0.01
                    if(house_li[5]['health']>=95):
                        house_li[5]['cond'] = 'normal'
                        score += 1
                        print('Score:',score)
                        house_li[5]['health'] = 100
                        house_li[5]['color'] = house_li[5]['originalColor']


    if(restart==1):
        restart=-1
        truck = {'x':400, 'y':400, 'direction':'up'}
        gameover = -1

        house_li = [
            { 'x':0,'y':0, 'health':100, 'cond':'normal', 'color': [[218/255, 165/255, 32/255], [184/255, 134/255, 30/255]], 'originalColor': [[218/255, 165/255, 32/255], [184/255, 134/255, 30/255]]},
            { 'x':0,'y':250, 'health':100, 'cond':'normal', 'color':[[255/255, 0/255, 128/255], [128/255, 0/255, 64/255]], 'originalColor':[[255/255, 0/255, 128/255], [128/255, 0/255, 64/255]]},
            { 'x':0,'y':500, 'health':100, 'cond':'normal', 'color':[[191/255, 0/255, 255/255], [115/255, 0/255, 153/255]], 'originalColor':[[191/255, 0/255, 255/255], [115/255, 0/255, 153/255]] },
            { 'x':650,'y':0, 'health':100, 'cond':'normal', 'color': [[51/255, 102/255, 255/255], [0/255, 45/255, 179/255]], 'originalColor':[[51/255, 102/255, 255/255], [0/255, 45/255, 179/255]]},
            { 'x':650,'y':250, 'health':100, 'cond':'normal', 'color':[[138/255, 138/255, 92/255], [92/255, 92/255, 61/255]], 'originalColor':[[138/255, 138/255, 92/255], [92/255, 92/255, 61/255]] },
            { 'x':650,'y':500, 'health':100, 'cond':'normal', 'color':[[117/255, 117/255, 163/255], [71/255, 71/255, 107/255]], 'originalColor':[[117/255, 117/255, 163/255], [71/255, 71/255, 107/255]] }
        ]

        houseHealth = [[25, 160, 25+house_li[0]['health'], 160], [25, 410, 25+house_li[1]['health'], 410], [25, 660, 25+house_li[2]['health'], 660], [670, 160, 670+house_li[3]['health'], 160], [670, 410, 670+house_li[4]['health'], 410], [670, 660, 670+house_li[5]['health'], 660]]
        #house_li[0]['cond']='fire'
        #fireTimer = 100
        water = -1
        score = 0
        fast_travel_left = 3
        gameover = -1
        printGameOver = 1       
        speed = 0


#house_li[4]['cond']='fire'
#####################################################################################
def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    

printGameOver = 1
def showScreen():
    global water, gameover, score, printGameOver
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0/255, 60/255, 40/255, 1)  #(0, 128/255, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #glColor3f(1.0, 1.0, 0.0) 
    #call the draw methods here
    # glColor3f(1, 1, 1)  
    # x1, y1 = 0, 0
    # x2, y2 = 400, 400
    # MidPointLineAlgorithm(x1, y1, x2, y2)
    # MidPointCircleAlgorithm(400, 400, 50)
    glPointSize(3)
    glColor3f(179/255, 179/255, 179/255)
    MidPointLineAlgorithm(400, 700, 400, 5)

    glColor3f(1,0,0)
    show_cross()
    glColor3f(0.5, 1.0, 1.0)
    show_restart()
    if(pause==-1):
        glColor3f(255/255, 140/255, 0)
        show_pause()
    elif(pause==1):
        glColor3f(255/255, 140/255, 0)
        show_play()    
    showHouseHealth()
    buildHouses()

    showTruck()

    num_burnt = 0
    for house in house_li:
        if(house['cond'] == 'burnt'):
            num_burnt += 1
        if(num_burnt>=3):
            gameover = 1
            if(printGameOver==1):
                print("Game Over!")
                print('Score:', score)
            printGameOver = 0

    if(water==1):
        glColor3f(0.0, 0.9, 0.9)
        showWater()


    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800) #window size
glutInitWindowPosition(700, 25)
wind = glutCreateWindow(b"CSE423 project") #window name
################################
glutDisplayFunc(showScreen)
glutSpecialFunc(specialKeyListener)
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseListener)

glutMainLoop()
