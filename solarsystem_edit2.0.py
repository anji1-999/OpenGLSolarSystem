from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL.Image import *
import pdb
import sys,gc
import bunny
from bunny import *
import numpy as np
import pdb
from skybox import *
ESCAPE = '\x1b'

# Number of the glut window.
window = 0
rot = 0.0
rot1 = 0.0
rot2 = 0.0
rot3 = 0.0
rot4 = 0.0

LightAmb=(0.7,0.7,0.7)  
LightDif=(1.0,1.0,0.0)  
LightPos=(0.0,0.0,0.0,0.0)#(4.0,4.0,6.0,1.0)
VIEW = np.array([-0.5, 0.5, -0.5, 0.5, 0.4, 10])
SCALE_K = np.array([1.0, 1.0, 1.0])
IS_PERSPECTIVE = True
MOUSE_X, MOUSE_Y = 0, 0
POINTS = np.array([[0, 0, 0]])
yaw = 0
pitch = 0
#q=GLUquadricObj()
xrot=yrot=0.0
CameraPos = np.array([0.0, 0.0, 0.8])#([0.0, 0.0, 2])1.2
CameraPos1 = np.array([0.0, 0.0, 0])
CameraFront = np.array([0, 0, 0])
CameraUp = np.array([0,1, 0])#([0, 1, 0])
xrotspeed=yrotspeed=0.0 
height=0.5 
textures = {}
objects = ('sun','earth','moon')


def LoadTextures(fname):
    if textures.get( fname ) is not None:
        return textures.get( fname )
    texture = textures[fname] = glGenTextures(1)
    image = open(fname)

    ix = image.size[0]
    iy = image.size[1]
    image = image.tobytes("raw", "RGBX", 0, -1)
    # Create Texture    
    glBindTexture(GL_TEXTURE_2D, texture)   # 2d texture (x and y size)
    
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    return texture



# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:  # Prevent A Divide By Zero If The Window Is Too Small
        Height = 1
    glViewport(0, 0, Width, Height)  # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.0001, 100.0)
    glMatrixMode(GL_MODELVIEW)




def DrawStars(Width,Height):

    glColor3f(1.0, 1.0, 1.0)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glDisable(GL_DEPTH_TEST)
    
    glBindTexture( GL_TEXTURE_2D, LoadTextures(r'E:\code\AR_homework\OpenGLSolarSystem\stars.bmp') )
    glPushMatrix()
    glBegin(GL_QUADS)
    glTexCoord2f(-Width,-Height)
    glVertex2d(-Width,-Height)
    glTexCoord2f(Width,-Height)
    glVertex2d(Width,-Height)
    glTexCoord2f(Width,Height)
    glVertex2d(Width,Height)
    glTexCoord2f(-Width,Height)
    glVertex2d(-Width,Height)
    
    glEnd()
    glPopMatrix()
    glEnable(GL_DEPTH_TEST)
    glBindTexture( GL_TEXTURE_2D,0)
    
def draw_teapot(size):  # 红色茶壶
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glClear(GL_DEPTH_BUFFER_BIT)
    # 绘制红色茶壶
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0, 0, 0, 0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.5, 0.0, 0.0, 0.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.7, 0.6, 0.6, 0.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 0.25 * 128.0)
    glutSolidTeapot(size)

def DrawSkybox():
    loadskybox()
    drawskybox()

def DrawSun():
    global Q
    glColor3f(1.0, 1.0, 1.0)
    glBindTexture( GL_TEXTURE_2D, LoadTextures('sun.tga') )#('earthmap.bmp') )
    
    Q=gluNewQuadric()
    gluQuadricNormals(Q, GL_SMOOTH)
    gluQuadricTexture(Q, GL_TRUE)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    
    gluSphere(Q, 0.2, 32, 16)
    
    glColor4f(1.0, 1.0, 1.0, 0.4)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    gluSphere(Q, 0.2, 32, 16)

    glDisable(GL_TEXTURE_GEN_S)
    glDisable(GL_TEXTURE_GEN_T)
    glDisable(GL_BLEND)
    gluDeleteQuadric( Q )
    

def DrawEarth():
    glPushName(1)
    global Q1
    glColor3f(1.0, 1.0, 1.0)
    glBindTexture( GL_TEXTURE_2D, LoadTextures('earthmap.bmp') )
    
    Q1=gluNewQuadric()
    gluQuadricNormals(Q1, GL_SMOOTH)
    gluQuadricTexture(Q1, GL_TRUE)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
	
    glPushMatrix()
    glTranslatef(0.0,0.0,0.5)			# Center The Cylinder
    glRotatef(rot2, 0.0, 1.0, 0.0)
    gluSphere(Q1,0.05,32,16) 
    # glLoadName(objects.index('earth'))
    gluDeleteQuadric( Q1 )
    DrawMoon()
    glPopMatrix()
    glPopName()

def DrawEarth_bunny():
    # global Q1
    glColor3f(1.0, 1.0, 1.0)
    glBindTexture( GL_TEXTURE_2D, LoadTextures(r'E:\code\AR_homework\OpenGLSolarSystem\mercurymap.bmp') )
    
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)

    glTranslatef(1.0,0.0,0.0)			# Center The Cylinder
    glRotatef(rot2, 0.0, 1.0, 0.0)
    Model1()
    DrawMoon()
    glPopMatrix()
    
def DrawMoon():
    glPushName(2)
    global Q4
    glColor3f(1.0, 1.0, 1.0)
    glBindTexture( GL_TEXTURE_2D, LoadTextures(r'E:\code\AR_homework\OpenGLSolarSystem\moon.bmp') )
    
    Q4=gluNewQuadric()
    gluQuadricNormals(Q4, GL_SMOOTH)
    gluQuadricTexture(Q4, GL_TRUE)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)

    glPushMatrix()
    glRotatef(rot3, 0.0, 1.0, 0.0)
    glRotatef(rot3, 1.0, 0.0, 1.0)
    # glRotatef(rot3, 0.0, 0.0, 1.0)
    glTranslatef(0.1,0.0,0)			# Center The Cylinder
    glRotatef(rot4, 0.0, 1.0, 0.0)
    gluSphere(Q4,0.02,32,16)	
    gluDeleteQuadric( Q4 )
    glPopMatrix()
    glBindTexture( GL_TEXTURE_2D,0)
    glPopName() 

RIGHT_IS_DOWNED = False

def Mouse_click(button, state, x, y):
    global RIGHT_IS_DOWNED
    global MOUSE_X, MOUSE_Y
    global SCALE_K
    global WIN_W
    global WIN_H
    global POINTS

    MOUSE_X = x
    MOUSE_Y = y

    if button == GLUT_RIGHT_BUTTON:
        RIGHT_IS_DOWNED = state == GLUT_DOWN
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        do_selection(x,y)
    
def Mouse_motion(x, y):
    global RIGHT_IS_DOWNED
    global MOUSE_X, MOUSE_Y
    global yaw, pitch
    global CameraPos

    if RIGHT_IS_DOWNED:
        dx = x - MOUSE_X
        dy = y - MOUSE_Y
        MOUSE_X = x
        MOUSE_Y = y

        sensitivity = 0.2
        dx = dx * sensitivity
        dy = dy * sensitivity
        print("I can mooooooooooove!!")
        print("Before",CameraPos)

        yaw = yaw + dx
        pitch = pitch + dy

        if pitch > 89:#89:
            pitch = 89
        if pitch < -89:
            pitch = -89

        r = np.sqrt(CameraPos[0]**2+CameraPos[1]**2+CameraPos[2]**2)
        CameraPos[2] = r * np.cos(np.radians(yaw)) * np.cos(np.radians(pitch))
        CameraPos[1] = r *np.sin(np.radians(pitch))
        CameraPos[0] = -r *np.sin(np.radians(yaw)) * np.cos(np.radians(pitch))
        print("after:",CameraPos)
        glutPostRedisplay()
        # pdb.set_trace()
def mouse_downup(button,state,x,y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        do_selection(x,y)

def do_selection(x,y):
    selection_buffer = glSelectBuffer(16)
    glRenderMode(GL_SELECT)
    
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    print("I can sellllllllllect!")
    glLoadIdentity()
    viewport = glGetIntegerv(GL_VIEWPORT)
    gluPickMatrix(x,viewport[3]-y,0.5,0.5,viewport)
    aspect = viewport[2]/viewport[3]
    gluPerspective(45,aspect,0.001,100)
    DrawGLScene()
    hits = glRenderMode(GL_RENDER)
    if hits:
        label = objects[selection_buffer[3]]
        print("select: ",label)
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

# A general OpenGL initialization function.  Sets all of the initial parameters. 
def InitGL(Width, Height):                # We call this right after our OpenGL window is created.
    glClearColor(0.0, 0.0, 0.0, 0.0)    # This Will Clear The Background Color To Black
    glClearDepth(1.0)                    # Enables Clearing Of The Depth Buffer
    glClearStencil(0)
    glDepthFunc(GL_LEQUAL)                # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)                # Enables Depth Testing
    glShadeModel(GL_SMOOTH)                # Enables Smooth Color Shading



    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    glEnable(GL_TEXTURE_2D)


    glLightfv(GL_LIGHT0, GL_AMBIENT, LightAmb)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, LightDif)
    glLightfv(GL_LIGHT0, GL_POSITION, LightPos)
    glEnable(GL_LIGHT0)           
    glEnable(GL_LIGHTING)

    gluPerspective(45.0, float(Width)/float(Height), 0.0001, 100.0)

    glMatrixMode(GL_MODELVIEW)




def DrawGLScene():
    global rot, texture,rot1,rot2,rot3,rot4, rot5, rot6, rot7, rot8
    global CameraPos, CameraFront, CameraUp
    global VIEW, SCALE_K
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear The Screen And The Depth Buffer
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()                    # Reset The Projection Matrix
    if IS_PERSPECTIVE:
        glFrustum(VIEW[0], VIEW[1], VIEW[2], VIEW[3], VIEW[4], VIEW[5])
    # 设置模型视图
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(
        CameraPos[0], CameraPos[1], CameraPos[2],
        CameraFront[0], CameraFront[1], CameraFront[2],
        CameraUp[0], CameraUp[1], CameraUp[2]
    )
    glTranslatef(0.0,0.0,0.0)#-20.0)  # Move Into The Screen
    # DrawStars(10,10)
    # drawCoordinate()
    drawskybox()
    glRotatef(rot, 0.0, 1.0, 0.0)  # Rotate The Cube On Its's Y Axis
    # draw_teapot(0.2)
    DrawSun()
    glRotatef(rot1, 0.0, 1.0, 0.0)  # Rotate The Cube On Its's Y Axis
    # DrawEarth_bunny()
    DrawEarth()
    # Start Drawing The Cube
    rot = (rot + 0.2) % 360  # rotation0.16太阳自转
    rot1 = (rot1 + 0.35) % 360#地球公转
    rot2 = (rot2 + 0.5) % 360#地球自转
    rot3 = (rot3 + 0.25) % 360#0.12#月球绕地公转
    rot4 = (rot3 + 0.010) % 360#月球自转
    #  since this is double buffered, swap the buffers to display what just got drawn.
    glutSwapBuffers()

def main():
    global window
    global CameraPos, CameraFront, CameraUp
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(612, 540)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Solar System")
    
    glutDisplayFunc(DrawGLScene)
    glutMouseFunc(Mouse_click)
    glutMotionFunc(Mouse_motion)#视角翻转
    # glutMouseFunc(mouse_downup)#select
    glutIdleFunc(DrawGLScene)
    glEnable(GL_DEPTH_TEST)
    glutReshapeFunc(ReSizeGLScene)
    InitGL(612, 540)
    # Start Event Processing Engine
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    main()














