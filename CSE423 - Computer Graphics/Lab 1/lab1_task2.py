from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import time

speed = 0.01
W_Height = 500
W_Width = 500
points = []
freeze = False
blinkToggle = False
blink = False

class Point:
    def __init__(self, x, y, color, speed, direction):
        self.x = x
        self.y = y
        self.z = 0
        self.color = color
        self.realColor = color
        self.blink = [0, 0, 0]
        self.speed = speed
        self.direction = direction



def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y 
    return a,b


def draw_point(x, y, color):
    glColor3f(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex3f(x, y, 0)
    glEnd()

def generate_point(x, y):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    direction = random.choice([[-1, 1], [-1, -1], [1, 1], [1, -1]])
    speed = 0.01
    p = Point(x, y, color, speed, direction)
    points.append(p)



def specialKeyListener(key, x, y):
    global speed
    if key == GLUT_KEY_UP:
        speed *= 2
        # for point in points:
        #     point.speed *= 2
        glutPostRedisplay()
    elif key == GLUT_KEY_DOWN:
        speed /= 2
        # for point in points:
        #     point.speed /= 2
        glutPostRedisplay()
    
def keyboardListener(key, x, y):
    global freeze
    if key == b"s": 
        print("Spacebar")
        freeze = not freeze
    glutPostRedisplay()


def mouseListener(button, state, x, y):
    global blinkToggle
    global blink
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        c_x, c_y = convert_coordinate(x,y)
        generate_point(c_x, c_y)
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        blinkToggle = True
        blink = True


        
def display():
    global blink
    global blinkToggle
    global freeze
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)

    if (blinkToggle == False):
        for point in points:
            draw_point(point.x, point.y, point.color)
    else:
        if (blink == True):
            for point in points:
                point.color = point.blink
                blink = not blink
                draw_point(point.x, point.y, point.color)
        elif (blink == False):
            for point in points:
                point.color = point.realColor
                blink = not blink
                draw_point(point.x, point.y, point.color)

    glutSwapBuffers()



def animate():
    global speed
    glutPostRedisplay()
    if (freeze == False):
        for point in points:
            dx, dy = point.direction
            new_x = point.x + dx * speed
            new_y = point.y + dy * speed

            if -W_Width/2 < new_x < W_Width/2 and -W_Height/2 < new_y < W_Height/2:
                point.x = new_x
                point.y = new_y
            else:
                point.direction = (-dx, -dy)
                point.x += dx * speed
                point.y += dy * speed

def init():
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104,	1,	1,	1000.0)


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(250, 250)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

wind = glutCreateWindow(b"Task 2")
init()

glutDisplayFunc(display)	
glutIdleFunc(animate)

glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseListener)

glutMainLoop()	
