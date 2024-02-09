from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def drawPoint(x, y):
    glPointSize(2)
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

def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-100, 100, -100, 100)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)


    glColor3f(1, 1, 1)  
    x1, y1 = 0, 10
    x2, y2 = 50, 50

    MidPointLineAlgorithm(x1, y1, x2, y2)

    glutSwapBuffers()



glutInit()
glutInitWindowSize(500, 500)
glutInitWindowPosition(250, 250)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

glutCreateWindow(b"Task 1: Mid Point Line Algorithm")

glutDisplayFunc(display)
init()  

glutMainLoop()
