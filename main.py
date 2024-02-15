import pygame
import random
import sys

pygame.init()

gray = (128, 128, 128)

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Car Game")

carimg = pygame.image.load('images/car.png')
grs = pygame.image.load("images/grass.jpg")
yellow_strip = pygame.image.load("images/yellow_strip.png")
white_strip = pygame.image.load("images/white_strip.jpg")

grass=pygame.transform.scale(grs, (103, height*2))
img = pygame.transform.scale(carimg, (40, 80))
ws = pygame.transform.scale(white_strip, (10, height))

carimg_x = 386
carimg_y = 500

# set Enemy car image
enemy_car = pygame.image.load("images/enemy.jpg")
enemy = pygame.transform.scale(enemy_car, (40, 80))

enemy_car_x = random.randint(120, 650)
enemy_car_y = 0

enemy_car_speed = 7
car_speed = 5


score=0
road_y=0

# add crash img
car_crash = pygame.image.load('images/crash.png')
crash_img = pygame.transform.scale(car_crash, (40, 80))

clock = pygame.time.Clock()

# create enemy car function
def draw_enemy_car(x, y):
    screen.blit(enemy, (x, y))


# create car function
def car(x, y):
    screen.blit(img, (x, y))


# create background function
def background(): 
    screen.blit(grass, (0, road_y))    
    screen.blit(grass, (700, road_y)) 
    screen.blit(yellow_strip, (400, road_y))
    screen.blit(yellow_strip, (400, 150 + road_y))
    screen.blit(yellow_strip, (400, 300 + road_y))
    screen.blit(yellow_strip, (400, 450 + road_y))
    screen.blit(yellow_strip, (400, 600 + road_y))
    screen.blit(yellow_strip, (400, 750 + road_y))
    screen.blit(yellow_strip, (400, 900 + road_y))
    screen.blit(yellow_strip, (400, 1050 + road_y))
    screen.blit(ws, (100, 0))
    screen.blit(ws, (700, 0))

# create crash function
def crash():
    screen.blit(crash_img,(carimg_x,carimg_y))
    pygame.display.update()
    print("You crashed! Total Score:", score)
    pygame.quit()
    sys.exit()
    
#create a score function
def display_score():
    font=pygame.font.Font(None,32)
    text=font.render("Score:"+str(score),True,(255,255,255))
    screen.blit(text,(10,10))
    
        
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # run enemy car
    enemy_car_y += enemy_car_speed
    if enemy_car_y > height:
        enemy_car_y = 0
        enemy_car_x = random.randint(240, 630)
        score += 1 
    # player car movement
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_LEFT and carimg_x>115:
            carimg_x-=car_speed
        if event.key==pygame.K_RIGHT and carimg_x<655:
            carimg_x+=car_speed

    # Crash car
    if (
        carimg_x < enemy_car_x + 40 and
        carimg_x + 40 > enemy_car_x and
        carimg_y < enemy_car_y + 80 and
        carimg_y + 80 > enemy_car_y
    ):
        crash()

        
     # Move the road
    road_y -= 10
    
    # Reset the position of background element
    if road_y <=-height:
        road_y = 0
    

    # Update the display
    #intro_loop()
    screen.fill(gray)
    background()
    car(carimg_x, carimg_y)
    draw_enemy_car(enemy_car_x, enemy_car_y)
    
    display_score()
    pygame.display.update()

    clock.tick(70)
    

pygame.quit()
