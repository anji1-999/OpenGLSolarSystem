from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL.Image import *

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

def loadskybox(fname,case):
    if textures.get( fname ) is not None:
        return textures.get( fname )
    texture = textures[fname] = glGenTextures(1)
    if case == 1:
        image = open(fname).rotate(180)#.transpose(FLIP_LEFT_RIGHT)
    if case == 2:
        image = open(fname).rotate(180).transpose(FLIP_LEFT_RIGHT)
    if case == 3:
        image = open(fname).transpose(FLIP_LEFT_RIGHT)

    ix = image.size[0]
    iy = image.size[1]
    image = image.tobytes("raw", "RGBX", 0, -1)
    # Create Texture    
    glBindTexture(GL_TEXTURE_2D, texture)   # 2d texture (x and y size)
    
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP_TO_EDGE)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    return texture

def drawskybox():
    # glEnable(GL_TEXTURE_2D)
    #
    # glColor3f(0.0, 0.0, 0.0)
    size = 1
    z = 1#1.5
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    #
    glDisable(GL_DEPTH_TEST)

    glColor3f(0,0,0) # front face
    glBindTexture(GL_TEXTURE_2D, loadskybox(r'E:\code\AR_homework\OpenGLSolarSystem\background\front.jpg',1))#bk_front.jpg',1))
    glPushMatrix()
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3d(-size, size, z)
    glTexCoord2f(1, 0)
    glVertex3d(size, size, z)
    glTexCoord2f(1, 1)
    glVertex3d(size, -size, z)
    glTexCoord2f(0, 1)
    glVertex3d(-size, -size, z)
    glEnd()
    glPopMatrix()

    glBindTexture(GL_TEXTURE_2D, loadskybox(r'E:\code\AR_homework\OpenGLSolarSystem\background\back.jpg',1))#bk_back.jpg',1))#back
    glPushMatrix()
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3d(size, size, -z)
    glTexCoord2f(1, 0)
    glVertex3d(-size, size, -z)
    glTexCoord2f(1, 1)
    glVertex3d(-size, -size, -z)
    glTexCoord2f(0, 1)
    glVertex3d(size,-size, -z)
    glEnd()
    glPopMatrix()

    glBindTexture(GL_TEXTURE_2D, loadskybox(r'E:\code\AR_homework\OpenGLSolarSystem\background\right.jpg',2))#bk_left.jpg',2))#right
    glPushMatrix()
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3d(-size, size, z)
    glTexCoord2f(1, 0)
    glVertex3d(-size, size, -z)
    glTexCoord2f(1, 1)
    glVertex3d(-size, -size, -z)
    glTexCoord2f(0, 1)
    glVertex3d(-size, -size, z)
    glEnd()
    glPopMatrix()

    glBindTexture(GL_TEXTURE_2D, loadskybox(r'E:\code\AR_homework\OpenGLSolarSystem\background\left.jpg',2))#E:\code\AR_homework\Solar-System-master\texture\bk_right.jpg',2))#left
    glPushMatrix()
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3d(size, size, -z)
    glTexCoord2f(1, 0)
    glVertex3d(size, size, z)
    glTexCoord2f(1, 1)
    glVertex3d(size, -size, z)
    glTexCoord2f(0, 1)
    glVertex3d(size, -size, -z)
    glEnd()
    glPopMatrix()

    glBindTexture(GL_TEXTURE_2D, loadskybox(r'E:\code\AR_homework\OpenGLSolarSystem\background\up.jpg',3))#bk_top.jpg',3))#up
    glPushMatrix()
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3d(-size, size, z)
    glTexCoord2f(1, 0)
    glVertex3d(size, size, z)
    glTexCoord2f(1, 1)
    glVertex3d(size, size, -z)
    glTexCoord2f(0, 1)
    glVertex3d(-size, size, -z)
    glEnd()
    glPopMatrix()

    
    glBindTexture(GL_TEXTURE_2D, loadskybox(r'E:\code\AR_homework\OpenGLSolarSystem\background\bottom.jpg',3))#bk_bottom.jpg',3))#down
    glPushMatrix()
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex3d(-size, -size, -z)
    glTexCoord2f(1, 0)
    glVertex3d(size, -size, -z)
    glTexCoord2f(1, 1)
    glVertex3d(size, -size, z)
    glTexCoord2f(0, 1)
    glVertex3d(-size, -size, z)
    glEnd()
    glPopMatrix()

    glBindTexture(GL_TEXTURE_2D, 0)
    glEnable(GL_DEPTH_TEST)





