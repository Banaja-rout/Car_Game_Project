import pygame

pygame.init()

gray =(128,128,128)

width,height = 800,600
screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("Car Game")
screen.fill(gray)


carimg = pygame.image.load('images/car.png')
grass = pygame.image.load("images/grass.jpg")
yellow_strip = pygame.image.load("images/yellow_strip.png")
white_strip = pygame.image.load("images/white_strip.jpg")

img = pygame.transform.scale(carimg,(40,80))
ws = pygame.transform.scale(white_strip,(10,height))


carimg_x = 386
carimg_y = 520

def car(x,y):
    screen.blit(img,(x,y))

def background():
    screen.blit(grass,(0,0))
    screen.blit(grass,(700,0))
    screen.blit(yellow_strip,(400,0))
    screen.blit(yellow_strip,(400,150))
    screen.blit(yellow_strip,(400,300))
    screen.blit(yellow_strip,(400,450))
    screen.blit(ws,(100,0))
    screen.blit(ws,(700,0))
   
    
background()
car(carimg_x,carimg_y)
pygame.display.update()
