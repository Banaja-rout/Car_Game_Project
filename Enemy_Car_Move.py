# time module    
clock = pygame.time.Clock()
clock.tick(70)

# enemy_car move

enemy_car_speed = 7

enemy_car_y += enemy_car_speed
if enemy_car_y > height:
        enemy_car_y = 0
        enemy_car_x = random.randint(120, 670)
