road_y=0
#add road_y in backaground function
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
while True:
   # Move the road
    road_y -= 10
    
    # Reset the position of background element
    if road_y <=-height:
        road_y = 0
 
