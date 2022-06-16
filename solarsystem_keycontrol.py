from OpenGL.GL import *
from OpenGL.GLUT import *
from PIL.Image import *
from OpenGL.GLU import *
import numpy as np
IS_PERSPECTIVE = True  # 透视投影
VIEW = np.array([-0.5, 0.5, -0.5, 0.5, 2, 10.0])  # 视景体的left/right/bottom/top/near/far六个面
RIGHT_IS_DOWNED = False
CameraPos = np.array([0.0, 0.0, 1])
CameraFront = np.array([0, 0, 0])
CameraUp = np.array([0, 1, 0])
SCALE_K = np.array([1.0, 1.0, 1.0])
yaw = 0
pitch = 0
MOUSE_X, MOUSE_Y = 0, 0
WIN_W = 480
WIN_H = 480
textures = {}
window = 0
rot = 0.0
rot1 = 0.0
rot2 = 0.0
rot3 = 0.0
rot4 = 0.0
rot5 = 0.0
rot6 = 0.0
rot7 = 0.0
rot8 = 0.0
objects = ('sun','earth','moon')
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # 设置画布背景色。注意：这里必须是4个参数
    glEnable(GL_DEPTH_TEST)  # 开启深度测试，实现遮挡关系
    glDepthFunc(GL_LEQUAL) # 设置深度测试函数（GL_LEQUAL只是选项之一）
    global nurb
    nurb = gluNewNurbsRenderer()
    global samplingTolerance
    gluNurbsProperty(nurb, GLU_SAMPLING_TOLERANCE, samplingTolerance)

nurb=None
samplingTolerance=1.0
def show():
    global IS_PERSPECTIVE, VIEW
    global CameraPos, CameraFront, CameraUp
    global SCALE_K
    global WIN_W, WIN_H
    global POINTS
    global nurb
    global rot, texture,rot1,rot2,rot3,rot4, rot5, rot6, rot7, rot8

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # 设置投影（透视投影）
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    if IS_PERSPECTIVE:
        glFrustum(VIEW[0], VIEW[1], VIEW[2], VIEW[3], VIEW[4], VIEW[5])

    # 设置模型视图
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # 几何变换
    glScale(SCALE_K[0], SCALE_K[1], SCALE_K[2])

    # 视点
    gluLookAt(
        CameraPos[0], CameraPos[1], CameraPos[2],
        CameraFront[0], CameraFront[1], CameraFront[2],
        CameraUp[0], CameraUp[1], CameraUp[2]
    )

    glViewport(0, 0, WIN_W, WIN_H)

    glTranslatef(0.0,0.0,-5.0)#-20.0)  # Move Into The Screen
    # DrawStars(10,10)
    # draw_background('universe.bmp')

    # glRotatef(10, 1.0, 0.0, 0.0)  # Rotate The Cube On It's X Axis
    glRotatef(rot, 0.0, 1.0, 0.0)  # Rotate The Cube On Its's Y Axis
    # glRotatef(-1, 0.0, 0.0, 1.0)  # Rotate The Cube On It's Z Axis
    # draw_teapot(0.2)
    DrawSun()
    

    # glRotatef(rot3, 1.0, 0.0, 0.0)  # Rotate The Cube On It's X Axis
    glRotatef(rot1, 0.0, 1.0, 0.0)  # Rotate The Cube On Its's Y Axis
    # glRotatef(-1, 0.0, 0.0, 1.0)  # Rotate The Cube On It's Z Axis
    # DrawEarth_bunny()
    DrawEarth()

    # glPushMatrix()
    
    # glPopMatrix()
    # DrawSun()
 
    
    # Start Drawing The Cube
    rot = (rot + 0.3) % 360  # rotation0.16太阳自转
    rot1 = (rot1 + 0.5) % 360#地球公转
    rot2 = (rot2 + 0.7) % 360#地球自转
    rot3 = (rot3 + 0.4) % 360#0.12#月球绕地公转
    rot4 = (rot3 + 0.010) % 360#月球自转
    rot5 = (rot3 + 0.008) % 360#
    rot6 = (rot3 + 0.006) % 360
    rot7 = (rot3 + 0.004) % 360
    rot8 = (rot8 + 0.002) % 360

    glutSwapBuffers()

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
    glTranslatef(0.0,0.0,2.0)			# Center The Cylinder
    glRotatef(rot2, 0.0, 1.0, 0.0)
    gluSphere(Q1,0.2,32,16) 
    # glLoadName(objects.index('earth'))
    gluDeleteQuadric( Q1 )
    DrawMoon()
    glPopMatrix()
    glPopName()

def DrawMoon():
    glPushName(2)
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
    glTranslatef(0.5,0.0,0)			# Center The Cylinder
    glRotatef(rot4, 0.0, 1.0, 0.0)
    gluSphere(Q4,0.04,32,16)	
    gluDeleteQuadric( Q4 )
    # glLoadName(objects.index('moon'))
    glPopMatrix()
    glBindTexture( GL_TEXTURE_2D,0)
    glPopName()
def DrawSun():
    glPushName(0)
    global Q
    glColor3f(1.0, 1.0, 1.0)
    glBindTexture( GL_TEXTURE_2D, LoadTextures('sun.tga') )
    
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
    # glLoadName(objects.index('sun'))

    glDisable(GL_TEXTURE_GEN_S)
    glDisable(GL_TEXTURE_GEN_T)
    glDisable(GL_BLEND)
    gluDeleteQuadric( Q )
    glPopName()
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

def Mouse_click(button, state, x, y):
    global RIGHT_IS_DOWNED
    global MOUSE_X, MOUSE_Y
    global SCALE_K
    global WIN_W
    global WIN_H
    global POINTS

    MOUSE_X = x
    MOUSE_Y = y

    if button == GLUT_LEFT_BUTTON and state == 0:

        modelview_mat = OpenGL.GL.glGetDoublev(OpenGL.GL.GL_MODELVIEW_MATRIX)
        projection_mat = OpenGL.GL.glGetDoublev(OpenGL.GL.GL_PROJECTION_MATRIX)
        viewport = OpenGL.GL.glGetIntegerv(OpenGL.GL.GL_VIEWPORT)

        z = OpenGL.GL.glReadPixels(MOUSE_X, viewport[3] - MOUSE_Y, 1, 1, OpenGL.GL.GL_DEPTH_COMPONENT, OpenGL.GL.GL_FLOAT)

        ret = gluUnProject(MOUSE_X, viewport[3] - MOUSE_Y, z, modelview_mat, projection_mat, viewport)
        ret_paint = [[ret[0], ret[1], ret[2]]]

        if abs(ret[0]) < 0.3 and abs(ret[1]) < 0.3 and abs(ret[2]) < 0.3: #方块之外的点不描出
            POINTS = np.append(POINTS, ret_paint, axis=0)

    if button == GLUT_RIGHT_BUTTON:
        RIGHT_IS_DOWNED = state == GLUT_DOWN


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

        sensitivity = 0.4
        dx = dx * sensitivity
        dy = dy * sensitivity

        yaw = yaw + dx
        pitch = pitch + dy

        if pitch > 89:
            pitch = 89
        if pitch < -89:
            pitch = -89

        CameraPos[0] = np.cos(np.radians(yaw)) * np.cos(np.radians(pitch))
        CameraPos[1] = np.sin(np.radians(pitch))
        CameraPos[2] = np.sin(np.radians(yaw)) * np.cos(np.radians(pitch))

        glutPostRedisplay()


if __name__ == '__main__':
    glutInit()
    displayMode = GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH
    glutInitDisplayMode(displayMode)
    glutInitWindowSize(WIN_W, WIN_H)
    glutInitWindowPosition(300, 200)
    glutCreateWindow("CUBE")

    init()
    glutDisplayFunc(show)
    glutMouseFunc(Mouse_click)
    glutMotionFunc(Mouse_motion)
    glutMainLoop()
