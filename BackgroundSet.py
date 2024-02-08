green = (0,255,0)
red = (255,0,0)

## intro image load
intro_image = pygame.image.load("background.jpg")

def text_object(text,font):
    textSurface = font.render(text,True,(0,0,0))
    return textSurface,textSurface.get_rect()

def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.blit(intro_image,(0,0))
##################        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        
        font = pygame.font.SysFont(None,187)
        title = font.render("CAR GAME", True,(0,0,0))
        screen.blit(title,(50,50))
        pygame.draw.rect(screen,green,(80,500,150,50))
        pygame.draw.rect(screen,red,(550,500,150,50))
      
        
###### for START        
        smallText = pygame.font.Font("freesansbold.ttf",25)
        textSurface,textRect = text_object("START",smallText)
        textRect.center = ((80+(150/2)),(500+(50/2)))
        screen.blit(textSurface,textRect)
###### for  quit       
        textSurface,textRect = text_object("QUIT",smallText)
        textRect.center = ((550+(150/2)),(500+(50/2)))
        screen.blit(textSurface,textRect)
        pygame.display.update()                 
