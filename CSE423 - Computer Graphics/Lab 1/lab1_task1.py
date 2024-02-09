from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

rain_lines = []
rains = []
bg_color = [1, 1, 1] 
obj_color = [0, 0, 0]


def generate_rain_lines():
    rain_lines.clear()
    i = -1
    length = 0.08
    toggle = True
    while (i <= 1):
        if toggle:
            j = 1
            while (j >= 0.4):
                x = i
                y = j
                rains.append((x, y, x, y - length))
                j -= 0.1
            i += 0.03
            rain_lines.append(rains)
            toggle = False
        else:
            j = 0.97
            while (j >= 0.4):
                x = i
                y = j
                rains.append((x, y, x, y - length))
                j -= 0.1
            i += 0.03
            rain_lines.append(rains)
            toggle = True


def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()



def draw_rain():
    glColor3f(obj_color[0], obj_color[1], obj_color[2])
    glLineWidth(1)
    for line in range(len(rain_lines)):
        for l in range(len(rain_lines[line])):
            a, b, c, d = rain_lines[line][l]
            draw_line(a, b, c, d)


def draw_house():
    glColor3f(obj_color[0], obj_color[1], obj_color[2]) 
    glLineWidth(5) 
    glBegin(GL_LINES)
    glVertex2f(-0.5, -0.7)
    glVertex2f(0.5, -0.7)
    glVertex2f(0.5, -0.7)
    glVertex2f(0.5, 0.0)
    glVertex2f(0.5, 0.0)
    glVertex2f(-0.5, 0.0)
    glVertex2f(-0.5, 0.0)
    glVertex2f(-0.5, -0.7)
    glEnd()
    # (-0.5, 0.0)               (0.5, 0.0)
    # (-0.5, -0.7)              (0.5, -0.7)


    glColor3f(obj_color[0], obj_color[1], obj_color[2]) 
    glLineWidth(5) 
    glBegin(GL_LINES)
    glVertex2f(-0.6, 0.0)
    glVertex2f(0.6, 0.0)
    glVertex2f(-0.6, 0.0)
    glVertex2f(0.0, 0.4)
    glVertex2f(0.6, 0.0)
    glVertex2f(0.0, 0.4)
    glEnd()

   
    glColor3f(obj_color[0], obj_color[1], obj_color[2])  
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(-0.4, -0.7)
    glVertex2f(-0.4, -0.3)
    glVertex2f(-0.4, -0.3)
    glVertex2f(-0.15, -0.3)
    glVertex2f(-0.15, -0.3)
    glVertex2f(-0.15, -0.7)
    glEnd()

    glColor3f(obj_color[0], obj_color[1], obj_color[2])  
    glPointSize(4)  
    glBegin(GL_POINTS)
    glVertex2f(-0.2, -0.5)
    glEnd()

    glColor3f(obj_color[0], obj_color[1], obj_color[2]) 
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(0.15, -0.15)
    glVertex2f(0.4, -0.15)
    glVertex2f(0.15, -0.33)
    glVertex2f(0.4, -0.33)
    glVertex2f(0.15, -0.15)
    glVertex2f(0.15, -0.33)
    glVertex2f(0.4, -0.15)
    glVertex2f(0.4, -0.33)
    glEnd()

    glColor3f(obj_color[0], obj_color[1], obj_color[2]) 
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(0.27, -0.15)
    glVertex2f(0.27, -0.33)
    glVertex2f(0.15, -0.24)
    glVertex2f(0.4, -0.24)
    glEnd()

def specialKeyListener(key, x, y):
    global obj_color
    if key == GLUT_KEY_UP:
        bg_color[0] -= 0.1
        bg_color[1] -= 0.1
        bg_color[2] -= 0.1
        bg_color[0] = max(bg_color[0], 0)
        bg_color[1] = max(bg_color[1], 0)
        bg_color[2] = max(bg_color[2], 0)
        print(bg_color)
        if bg_color[0] < 0.2:
            obj_color = [1, 1, 1]
        glutPostRedisplay()
    elif key == GLUT_KEY_DOWN:
        bg_color[0] += 0.1
        bg_color[1] += 0.1
        bg_color[2] += 0.1
        bg_color[0] = min(bg_color[0], 1)
        bg_color[1] = min(bg_color[1], 1)
        bg_color[2] = min(bg_color[2], 1)
        if bg_color[0] >= 0.2:
            obj_color = [0, 0, 0]
        glutPostRedisplay()
    elif key == GLUT_KEY_LEFT:
        print("Left Key Pressed")
        for line in range(len(rain_lines)):
            for l in range(len(rain_lines[line])):
                temp = list(rain_lines[line][l])
                temp[2] -= 0.0001
                #temp[3] += 0.0001
                rain_lines[line][l] = tuple(temp)

    elif key == GLUT_KEY_RIGHT:
        print("Right Key Pressed")
        for line in range(len(rain_lines)):
            for l in range(len(rain_lines[line])):
                temp = list(rain_lines[line][l])
                temp[2] += 0.0001
                #temp[3] += 0.0001
                rain_lines[line][l] = tuple(temp)

    glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(1, 1, 1, 1)
    glClearColor(*bg_color, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_house()
    draw_rain()
    glutSwapBuffers()

def animate():
    glutPostRedisplay()


glutInit()
glutInitWindowSize(500, 500)

glutInitWindowPosition(250, 100)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

glutCreateWindow(b"Task 1")
generate_rain_lines()
glutDisplayFunc(display)
glutSpecialFunc(specialKeyListener)
glutIdleFunc(animate)
glutMainLoop()