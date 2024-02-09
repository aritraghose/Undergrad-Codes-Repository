from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

circles = []
speed = 1
freeze = False

def drawPoints(x, y, dx, dy):
    #global circles
    #print(circles)
    #if ((-375 <= x+dx <= 375) and (-375 <= -x+dx <= 375) and (-375 <= y+dx <= 375) and (-375 <= -y+dx <= 375) and (-375 <= y+dy <= 375) and (-375 <= -y+dy <= 375) and (-375 <= -x+dy <= 375) and (-375 <= x+dy <= 375)):
    glPointSize(1.5)
    glBegin(GL_POINTS)
    glVertex2i(x+dx, y+dy)
    glEnd()

    glPointSize(1.5)
    glBegin(GL_POINTS)
    glVertex2i(-x+dx, y+dy)
    glEnd()

    glPointSize(1.5)
    glBegin(GL_POINTS)
    glVertex2i(-x+dx, -y+dy)
    glEnd()
    
    glPointSize(1.5)
    glBegin(GL_POINTS)
    glVertex2i(x+dx, -y+dy)
    glEnd()

    glPointSize(1.5)
    glBegin(GL_POINTS)
    glVertex2i(y+dx, x+dy)
    glEnd()

    glPointSize(1.5)
    glBegin(GL_POINTS)
    glVertex2i(-y+dx, x+dy)
    glEnd()

    glPointSize(1.5)
    glBegin(GL_POINTS)
    glVertex2i(-y+dx, -x+dy)
    glEnd()

    glPointSize(1.5)
    glBegin(GL_POINTS)
    glVertex2i(y+dx, -x+dy)
    glEnd()




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



def specialKeyListener(key, x, y):
    global speed
    global freeze
    if not freeze:
        if key == GLUT_KEY_LEFT:
            speed += 1
        elif key == GLUT_KEY_RIGHT:
            speed -= 1


def mouseListener(button, state, x, y):
    global circles
    global freeze
    if not freeze:
        if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
            circles.append([x - 375, 375 - y, 0])
 
def keyboardListener(key, x, y):
    global freeze
    if key == b" ":
        freeze = not freeze
    glutPostRedisplay()





def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-375, 375, -375, 375)




def display():
    global circles
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    
    glPointSize(1.5)
    glBegin(GL_POINTS)
    glVertex2i(375, 375)
    glEnd()


    for i in range(len(circles)):
        MidPointCircleAlgorithm(circles[i][0], circles[i][1], circles[i][2])

    glutSwapBuffers()


def animate():
    glutPostRedisplay()

def update(value):
    global circles
    global speed
    global freeze
    glutTimerFunc(10, update, 0)

    if not freeze:
        for i in range(len(circles)):
            if (i >= len(circles)):
                break
            circles[i][2] += speed
            if (i >= len(circles)):
                break
            if ((circles[i][0] + circles[i][2] > 375) or (circles[i][0] - circles[i][2] < -375) or (circles[i][1] + circles[i][2] > 375) or (circles[i][1] - circles[i][2] < -375)):
                circles.pop(i)
                i -= 1
    glutPostRedisplay()



glutInit()
glutInitWindowSize(750, 750)
glutInitWindowPosition(350, 20)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"Lab 3: Mid Point Circle and Activity Task")
glutDisplayFunc(display)
init()  
glutTimerFunc(25, update, 0)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutKeyboardFunc(keyboardListener)
glutIdleFunc(animate)
glutMainLoop()
