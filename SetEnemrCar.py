import random
#Set enemy car  position 
enemy_car= pygame.image.load("images/enemy.jpg") 
enemy = pygame.transform.scale(enemy_car, (40, 80))
enemy_car_x = random.randint(120, 670)
enemy_car_y = 0 

def draw_enemy_car(x, y):
    screen.blit(enemy, (x, y))
draw_enemy_car(enemy_car_x,enemy_car_y)
