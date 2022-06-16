from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL.Image import *
import pdb
import sys
from bunny import *


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
LightPos=(4.0,4.0,6.0,1.0)
#q=GLUquadricObj()
xrot=yrot=0.0
xrotspeed=yrotspeed=0.0 
zoom=-3.0
height=0.5 
textures = {}


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

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()                    # Reset The Projection Matrix

    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:  # Prevent A Divide By Zero If The Window Is Too Small
        Height = 1

    glViewport(0, 0, Width, Height)  # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def draw_background(imname):
    glColor3f(1.0, 1.0, 1.0)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glDisable(GL_DEPTH_TEST)
    
    glBindTexture( GL_TEXTURE_2D, LoadTextures('stars.bmp') )
    glPushMatrix()
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)  
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0)  
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)  
    glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 1.0)  
    glVertex3f(-1.0, 1.0, -1.0)
    glEnd()
    glPopMatrix()
    glEnable(GL_DEPTH_TEST)
    glBindTexture( GL_TEXTURE_2D,0)


def DrawStars(Width,Height):
    glColor3f(1.0, 1.0, 1.0)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glDisable(GL_DEPTH_TEST)
    
    glBindTexture( GL_TEXTURE_2D, LoadTextures('stars.bmp') )
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
    
def draw_teapot(size): 
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glClear(GL_DEPTH_BUFFER_BIT)
    glMaterialfv(GL_FRONT, GL_AMBIENT, [0, 0, 0, 0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.5, 0.0, 0.0, 0.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.7, 0.6, 0.6, 0.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 0.25 * 128.0)
    glutSolidTeapot(size)



def DrawSun():
    global Q
    glColor3f(1.0, 1.0, 1.0)
    glBindTexture( GL_TEXTURE_2D, LoadTextures('sun.tga') )#('sun.tga') )
    Q=gluNewQuadric()
    gluQuadricNormals(Q, GL_SMOOTH)
    gluQuadricTexture(Q, GL_TRUE)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    gluSphere(Q, 0.7, 32, 16)
    
    glColor4f(1.0, 1.0, 1.0, 0.4)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    gluSphere(Q, 0.7, 32, 16)

    glDisable(GL_TEXTURE_GEN_S)
    glDisable(GL_TEXTURE_GEN_T)
    glDisable(GL_BLEND)
    gluDeleteQuadric( Q )
    
def DrawEarth():
    global Q1
    glColor3f(1.0, 1.0, 1.0)
    glBindTexture( GL_TEXTURE_2D, LoadTextures('earthmap.bmp') )
    
    Q1=gluNewQuadric()
    gluQuadricNormals(Q1, GL_SMOOTH)
    gluQuadricTexture(Q1, GL_TRUE)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
	
    glPushMatrix()
    glTranslatef(0.0,0.0,2.0)			# Center The Cylinder
    glRotatef(rot2, 0.0, 1.0, 0.0)
    gluSphere(Q1,0.10,32,16) 
    gluDeleteQuadric( Q1 )
    DrawMoon()
    glPopMatrix()

def DrawEarth_bunny():
    # global Q1
    glColor3f(1.0, 1.0, 1.0)
    glBindTexture( GL_TEXTURE_2D, LoadTextures('mercurymap.bmp') )
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
	
    glPushMatrix()
    glTranslatef(1.0,0.0,0.0)			# Center The Cylinder
    glRotatef(rot2, 0.0, 1.0, 0.0)
    Model1()
    DrawDragon()
    glPopMatrix()

def DrawDragon():
    glPushName(2)
    glColor3f(1.0, 1.0, 1.0)
    glBindTexture( GL_TEXTURE_2D, LoadTextures(r'E:\code\AR_homework\OpenGLSolarSystem\moon.bmp') )
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glRotatef(rot3, 0.0, 1.0, 0.0)
    glRotatef(rot3, 1.0, 0.0, 0.0)
    glRotatef(rot3, 0.0, 0.0, 1.0)
    glTranslatef(0.2,0.1,0)			# Center The Cylinder
    glRotatef(rot4, 0.0, 1.0, 0.0)
    glRotatef(rot4, 1.0, 0.0, 0.0)
    
    Model2()
    glBindTexture( GL_TEXTURE_2D,0)
    glPopName() 

def DrawMoon():
    global Q4
    glColor3f(1.0, 1.0, 1.0)
    glBindTexture( GL_TEXTURE_2D, LoadTextures('moon.bmp') )
    
    Q4=gluNewQuadric()
    gluQuadricNormals(Q4, GL_SMOOTH)
    gluQuadricTexture(Q4, GL_TRUE)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)

    glPushMatrix()
    glRotatef(rot3, 0.0, 1.0, 0.0)
    glTranslatef(0.15,0.0,0)			# Center The Cylinder
    glRotatef(rot4, 0.0, 1.0, 0.0)
    # glRotatef(rot4, 1.0, 0.0, 0.0)
    # glRotatef(rot4, 0.0, 0.0, 1.0)
    gluSphere(Q4,0.04,32,16)	
    gluDeleteQuadric( Q4 )
    glPopMatrix()
    glBindTexture( GL_TEXTURE_2D,0)


def drawCoordinate():
  line_len = 4
  grid_color = [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)]

  glLineWidth(3)
  origin = [0.0, 0.0, 0.0]
  for i in range(3):
    tmp = [0.0, 0.0, 0.0]
    tmp[i] = line_len*1.02
    print(*grid_color[i])
    glColor3f(*grid_color[i])
    glBegin(GL_LINES)
    glVertex3f(*origin)
    glVertex3f(*tmp)
    glEnd()


def DrawGLScene():
    global rot, texture,rot1,rot2,rot3,rot4, rot5, rot6, rot7, rot8
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear The Screen And The Depth Buffer
    glLoadIdentity()  # Reset The View 
	
    glTranslatef(0.0,0.0,-5.0)#-20.0)  # Move Into The Screen
    DrawStars(10,10)
    glRotatef(rot, 0.0, 1.0, 0.0)  # Rotate The Cube On Its's Y Axis
    draw_teapot(0.2)
    # DrawSun()

    glRotatef(rot1, 0.0, 1.0, 0.0)  # Rotate The Cube On Its's Y Axis
    DrawEarth_bunny()
    # DrawEarth()

    # Start Drawing The Cube
    rot = (rot + 1) % 360  # rotation0.16太阳自转
    rot1 = (rot1 + 0.8) % 360#地球公转
    rot2 = (rot2 + 0.6) % 360#地球自转
    rot3 = (rot3 + 0.55) % 360#0.12#月球绕地公转
    rot4 = (rot3 + 0.010) % 360#月球自转
    glutSwapBuffers()

def keyPressed(*args):
    # If escape is pressed, kill everything.
    if args[0] == ESCAPE:
        sys.exit()

def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    # get a 640 x 480 window
    glutInitWindowSize(612, 540)#(612, 540)612*2,540

    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("Solar System")
    glutDisplayFunc(DrawGLScene)
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)
    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)
    # Register the function called when the keyboard is pressed.
    glutKeyboardFunc(keyPressed)
    # Initialize our window.
    InitGL(612, 540)
    # Start Event Processing Engine
    glutMainLoop()


# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    print("Hit ESC key to quit.")
    main()














