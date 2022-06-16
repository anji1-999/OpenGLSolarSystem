from OpenGL.GL import *
from OpenGL.GLU import *
import pywavefront

scene = pywavefront.Wavefront(r'E:\code\AR_homework\OpenGLSolarSystem\bunny.obj', collect_faces=True)
scene_box = (scene.vertices[0], scene.vertices[0])
for vertex in scene.vertices:
    min_v = [min(scene_box[0][i], vertex[i]) for i in range(3)]
    max_v = [max(scene_box[1][i], vertex[i]) for i in range(3)]
    scene_box = (min_v, max_v)

scene_size     = [scene_box[1][i]-scene_box[0][i] for i in range(3)]
max_scene_size = max(scene_size)
scaled_size    = 0.5#3
scene_scale    = [scaled_size/max_scene_size for i in range(3)]
scene_trans    = [-(scene_box[1][i]+scene_box[0][i])/2 for i in range(3)]

def Model1():
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    # glPushMatrix()
    glScalef(*scene_scale)
    glTranslatef(*scene_trans)

    for mesh in scene.mesh_list:
        glBegin(GL_TRIANGLES)
        for face in mesh.faces:
            for vertex_i in face:
                glVertex3f(*scene.vertices[vertex_i])
        glEnd()
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

scene1 = pywavefront.Wavefront(r'E:\code\AR_homework\OpenGLSolarSystem\dragon.obj', collect_faces=True)
scene_box1 = (scene1.vertices[0], scene1.vertices[0])
for vertex1 in scene1.vertices:
    min_v = [min(scene_box1[0][i], vertex1[i]) for i in range(3)]
    max_v = [max(scene_box1[1][i], vertex1[i]) for i in range(3)]
    scene_box1 = (min_v, max_v)

scene_size1     = [scene_box1[1][i]-scene_box1[0][i] for i in range(3)]
max_scene_size1 = max(scene_size1)
scaled_size1    = 0.2#3
scene_scale1    = [scaled_size1/max_scene_size1 for i in range(3)]
scene_trans1    = [-(scene_box1[1][i]+scene_box1[0][i])/2 for i in range(3)]

def Model2():
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    # glPushMatrix()
    glScalef(*scene_scale1)
    glTranslatef(*scene_trans1)

    for mesh in scene1.mesh_list:
        glBegin(GL_TRIANGLES)
        for face in mesh.faces:
            for vertex_i in face:
                glVertex3f(*scene1.vertices[vertex_i])
        glEnd()
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)    