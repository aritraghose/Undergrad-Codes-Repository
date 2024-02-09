from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

def drawPoint(x, y):
    glPointSize(1.5)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

catcher = [[-20, -100, 20, -100], [-20, -100, -24, -95], [20, -100, 24, -95], [-24, -95, 24, -95]]
diamond = [[0, 82, 5, 77], [0, 82, -5, 77], [0, 72, 5, 77], [0, 72, -5, 77]]

speed = 1
play = False
freeze = False
diamondColor = [1.0, 1.0, 1.0]
whiteColor = [1.0, 1.0, 1.0]
catcherColor = [1.0, 1.0, 1.0]
score = 0

def displayDiamond():
    glColor3f(*diamondColor)
    MidPointLineAlgorithm(diamond[0][0], diamond[0][1], diamond[0][2], diamond[0][3])
    MidPointLineAlgorithm(diamond[1][0], diamond[1][1], diamond[1][2], diamond[1][3])
    MidPointLineAlgorithm(diamond[2][0], diamond[2][1], diamond[2][2], diamond[2][3])
    MidPointLineAlgorithm(diamond[3][0], diamond[3][1], diamond[3][2], diamond[3][3])

def diamondFall():
    global speed
    global diamond
    global catcher
    global score
    global freeze
    if (not freeze):
        diamond[0][1] -= speed
        diamond[0][3] -= speed
        diamond[1][1] -= speed
        diamond[1][3] -= speed
        diamond[2][1] -= speed
        diamond[2][3] -= speed
        diamond[3][1] -= speed
        diamond[3][3] -= speed

        #speed += 1

        if (((diamond[0][2] >= catcher[3][0] and diamond[0][2] <= catcher[3][2]) or (diamond[1][2] >= catcher[3][0] and diamond[1][2] <= catcher[3][2])) and (diamond[2][1] < -95)):
            # catched
            score += 1
            print("Score:", score)
            newDiamond()
        if (((diamond[0][2] < catcher[2][0]) or (diamond[1][2] > catcher[2][2])) and (diamond[2][1] < -95)):
            # Game Over
            print("Game Over! Score:", score)
            score = 0
            freeze = True
            gameOver()

        # if (diamond[2][1] < -100):
        #     newDiamond()




def newDiamond():
    global diamondColor
    global diamond
    diamondColor = [random.random(), random.random(), random.random()]
    p = random.randrange(-95, 95)
    diamond = [[p, 82, p+5, 77], [p, 82, p-5, 77], [p, 72, p+5, 77], [p, 72, p-5, 77]]


def gameOver():
    global catcherColor
    global score
    catcherColor = [1.0, 0, 0]
    score = 0



def playPause(freeze):
    if freeze:
        MidPointLineAlgorithm(-8, 85, -8, 95)
        MidPointLineAlgorithm(-8, 85, 8, 90)
        MidPointLineAlgorithm(-8, 95, 8, 90)
    else:
        MidPointLineAlgorithm(-4, 85, -4, 95)
        MidPointLineAlgorithm(4, 85, 4, 95)



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

def specialKeyListener(key, x, y):
    global freeze
    if (not freeze):
        if key == GLUT_KEY_LEFT:
            for i in range(4):
                catcher[i][0] -= 4
                catcher[i][2] -= 4
            if (catcher[3][0] < -100):
                for i in range(4):
                    catcher[i][0] += 4
                    catcher[i][2] += 4

        elif key == GLUT_KEY_RIGHT:
            for i in range(4):
                catcher[i][0] += 4
                catcher[i][2] += 4
            if ((catcher[3][2] > 100)):
                for i in range(4):
                    catcher[i][0] -= 4
                    catcher[i][2] -= 4


def mouseListener(button, state, x, y):
    global play
    global freeze
    global score
    global catcherColor
    global whiteColor
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if ((x >= 160) and (x <= 235) and (y >= 0) and (y <= 65)):
            play = not play
            freeze = not freeze
        elif ((x >= 0) and (x <= 75) and (y >= 0) and (y <= 65)):
            # reset
            print("Starting Over!")
            freeze = False
            catcherColor = [whiteColor[0], whiteColor[1], whiteColor[2]]
            newDiamond()
        elif ((x >= 340) and (x <= 400) and (y >= 0) and (y <= 65)):
            print("Goodbye! Score:", score)
            glutLeaveMainLoop()





def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-100, 100, -100, 100)




def display():
    global freeze
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)

    # Catcher
    glColor3f(*catcherColor)  
    MidPointLineAlgorithm(catcher[0][0], catcher[0][1], catcher[0][2], catcher[0][3])
    MidPointLineAlgorithm(catcher[1][0], catcher[1][1], catcher[1][2], catcher[1][3])
    MidPointLineAlgorithm(catcher[2][0], catcher[2][1], catcher[2][2], catcher[2][3])
    MidPointLineAlgorithm(catcher[3][0], catcher[3][1], catcher[3][2], catcher[3][3])

    # Reset Button
    glColor3f(1/255, 189/255, 198/255)
    MidPointLineAlgorithm(-95, 90, -70, 90)
    MidPointLineAlgorithm(-95, 90, -85, 94)
    MidPointLineAlgorithm(-95, 90, -85, 86)

    # Play Pause Button
    glColor3f(255/255, 191/255, 0/255)
    
    playPause(freeze)

    # Close Button
    glColor3f(1, 0, 0)
    MidPointLineAlgorithm(80, 95, 94, 85)
    MidPointLineAlgorithm(80, 85, 94, 95)


    # boundary
    # MidPointLineAlgorithm(-100, 82, 100, 82) # +82 to -95 height
    # MidPointLineAlgorithm(-100, -95, 100, -95)

    #MidPointLineAlgorithm(-100, 82, 100, 82)

    displayDiamond()

    glutSwapBuffers()


def animate():
    glutPostRedisplay()

def update(value):
    diamondFall()
    glutTimerFunc(10, update, 0)
    glutPostRedisplay()



glutInit()
glutInitWindowSize(400, 700)
glutInitWindowPosition(550, 50)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"Task 2: Catch The Diamonds")
glutDisplayFunc(display)
init()  
glutTimerFunc(25, update, 0)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutIdleFunc(animate)
glutMainLoop()
