score=0  #to initialize 
#score part:
def display_score():
    font=pygame.font.Font(None,36)
    text=font.render("Score:"+str(score),True,(255,255,255))
    screen.blit(text,(10,10))
 #Game loop
 while True:
     score+=1 #it stored in the enemy car run part....
   display_score()
    print("Total Score:",score) #after all print this in the crash function...
