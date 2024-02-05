import sys
#add crash img
car_crash=pygame.image.load('images/crash.png')
crash_img=pygame.transform.scale(car_crash,(40,80))

#create crash function
def crash():
    screen.blit(crash_img,(carimg_x,carimg_y))
    pygame.display.update()
    print("You crashed!")
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# check collision
while True:
  if (
        carimg_x < enemy_car_x + 40 and
        carimg_x + 40 > enemy_car_x and
        carimg_y < enemy_car_y + 80 and
        carimg_y + 80 > enemy_car_y
    ):
        crash()
