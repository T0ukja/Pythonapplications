import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")
image = pygame.image.load(r'stick.png')
x = 50
y = 50
vel = 5
screen_width=460
screen_height=450

isJump = False
jumpCount = 10

run = True

def gravity():
        global y
        y+= 3.2

while run:
    
    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]: 
        x -= vel


    if keys[pygame.K_RIGHT]:  
        x += vel
        

        
    if not(isJump): 
      
           
        if keys[pygame.K_DOWN]:
            y += vel
            


        if keys[pygame.K_SPACE]:
            isJump = True
        
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    if x < 0:

        x = 0
        

    if x > screen_width:

        x = screen_width

    if y <= 0:

        y = 0

    if y >= screen_height:
        y = screen_height

    win.fill((255, 255, 255))
    win.blit(image, (x, y))
    gravity()
    pygame.display.update() 
    
pygame.quit()


'''


'''
    
