car_speed=5
#movement player car
    if event.type==pygame.KEYDOWN:
         if event.key==pygame.K_LEFT and carimg_x>115:
             carimg_x-=car_speed
         if event.key==pygame.K_RIGHT and carimg_x<655:
             carimg_x+=car_speed
