# def LoadTextures(fname):
#     if textures.get( fname ) is not None:
#         return textures.get( fname )
#     texture = textures[fname] = glGenTextures(1)
#     image = open(fname)

#     ix = image.size[0]
#     iy = image.size[1]
#     image = image.tobytes("raw", "RGBX", 0, -1)
#     # Create Texture    
#     glBindTexture(GL_TEXTURE_2D, texture)   # 2d texture (x and y size)
    
#     glPixelStorei(GL_UNPACK_ALIGNMENT,1)
#     glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
#     glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
#     return texture
# def DrawStars(Width,Height):

#     glColor3f(1.0, 1.0, 1.0)
#     glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
#     glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
#     glDisable(GL_DEPTH_TEST)
    
#     glBindTexture( GL_TEXTURE_2D, LoadTextures('stars.bmp') )
#     glPushMatrix()
#     glBegin(GL_QUADS)
#     glTexCoord2f(-Width,Height)
#     glVertex2d(-Width,-Height)
#     glTexCoord2f(Width,Width)
#     glVertex2d(Width,0)
#     glTexCoord2f(Width,0.0)
#     glVertex2d(Width,Height)
#     glTexCoord2f(0.0,0.0)
#     glVertex2d(0,Height)
#     glEnd()
#     glPopMatrix()
#     glEnable(GL_DEPTH_TEST)
#     glBindTexture( GL_TEXTURE_2D,0)

# def draw_background(imname):
#     glColor3f(1.0, 1.0, 1.0)
#     glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
#     glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
#     # 载入背景图像
#     # bg_image = pygame.image.load(imname).convert()
#     # bg_data = pygame.image.tostring(bg_image, "RGBX", 1)  # 将图像转为字符串描述
#     image = open(imname)
#     ix = image.size[0]
#     iy = image.size[1]
#     image = image.tobytes("raw", "RGBX", 0, -1)
    
#     glMatrixMode(GL_MODELVIEW)  # 将当前矩阵指定为投影矩阵
#     glLoadIdentity()  # 把矩阵设为单位矩阵
 
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # 清楚颜色、深度缓冲
#     glPushMatrix()
#     glEnable(GL_TEXTURE_2D)  # 纹理映射
#     glBindTexture(GL_TEXTURE_2D, glGenTextures(1))
#     # glPixelStorei(GL_UNPACK_ALIGNMENT,1)
#     glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
#     # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
#     # glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
#     # 绑定纹理
#     glBegin(GL_QUADS)
    
#     glTexCoord2f(0.0, 0.0)  glVertex3f(-1.0, -1.0, -1.0)
#     glTexCoord2f(1.0, 0.0)  glVertex3f(1.0, -1.0, -1.0)
#     glTexCoord2f(1.0, 1.0)  glVertex3f(1.0, 1.0, -1.0)
#     glTexCoord2f(0.0, 1.0)  glVertex3f(-1.0, 1.0, -1.0)
#     # glTexCoord2f(0.0, 0.0)  glVertex2d(-1.0, 1.0)
#     # glTexCoord2f(1.0, 0.0)  glVertex2d(1.0, -1.0)
#     # glTexCoord2f(1.0, 1.0)  glVertex2d(1.0, 1.0)
#     # glTexCoord2f(0.0, 1.0)  glVertex2d(-1.0, -1.0)
#     # glTexCoord2f(-Width,Height)
#     # glVertex2d(-Width,-Height)
#     # glTexCoord2f(Width,Width)
#     # glVertex2d(Width,0)
#     # glTexCoord2f(Width,0.0)
#     # glVertex2d(Width,Height)
#     # glTexCoord2f(0.0,0.0)
#     # glVertex2d(0,Height)
#     glEnd()
#     glPopMatrix()
#     # glDeleteTextures(1)  # 清除纹理
#     glBindTexture( GL_TEXTURE_2D,0)


# def model_build():
#     global window
#     glutInit(sys.argv)
#     glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

#     # get a 640 x 480 window
#     image = open('universe.bmp')
#     ix = image.size[0]
#     iy = image.size[1]
#     print(ix,iy)
#     glutInitWindowSize(612*2, 540)#(612, 540)612*2,540

#     # the window starts at the upper left corner of the screen
#     glutInitWindowPosition(0, 0)
#     window = glutCreateWindow("Solar System")
#     glutDisplayFunc(DrawGLScene)
#     glutIdleFunc(DrawGLScene)
#     glutReshapeFunc(ReSizeGLScene)
#     glutKeyboardFunc(keyPressed)
#     InitGL(612, 540)
#     glutMainLoop()
# from PIL import Image
# im1 = Image.open(r"E:\code\AR_homework\Solar-System-master\universe.jpg").rotate(180).transpose(Image.FLIP_LEFT_RIGHT).resize((512,512))
# im1.show()

a = []
for i in range(0,5):
    a.append(i)
print(a[1])