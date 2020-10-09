#Displays key codes on screen to aid key identification. Esc to quit

from pygame_functions import *
    
screenSize(300,100)

while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        print("up", end=" ")
    if keys[pygame.K_LEFT]:
        print("left", end=" ")        
    if keys[pygame.K_RIGHT]:
        print("right", end=" ")         
    if keys[pygame.K_DOWN]:
        print("down", end=" ") 
    if keys[pygame.K_SPACE]:
        print("space", end=" ")    
    print()
    tick(60)
pause(1000, False)
