import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import wireCube

pygame.init()

#Configurações
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Cubo')

def initialise():
    glClearColor(*background_color)
    glColor(*drawing_color)

    #Projeção
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

    #Modelo de visão
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_DEPTH_TEST)

#Eixo X (movendo para a esquerda)
positions_x = [2, 1.5, 1, 0.5, 0, -0.5, -1, -1.5, -2]

#O cubo cresce ao longo do tempo)
scales = [0.5, 0.7, 0.9, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

index = 0 

def drawCube(x, y, scale, mirrored=False):
    glPushMatrix()
    glTranslatef(x, y, -5)  #Translação
    
    if mirrored:
        glScalef(scale, -scale, scale)  #Espelhamento no eixo Y
    else:
        glScalef(scale, scale, scale)  #Escala normal
    
    glRotatef(1, 10, 0, 1)  #Mantemos a rotação do cubo
    wireCube()
    glPopMatrix()

def display():
    global index

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #Desenha o cubo original (acima)
    drawCube(positions_x[index], 1, scales[index])

    #Desenha o reflexo (invertido no eixo Y)
    drawCube(positions_x[index], -1, scales[index], mirrored=True)

    #Avança para a próxima posição e escala
    index += 1
    if index >= len(positions_x):  
        index = len(positions_x) - 1  #Mantém último estágio

fim = False
initialise()
while not fim:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fim = True

    display()
    pygame.display.flip()
    pygame.time.wait(600)  

pygame.quit()
