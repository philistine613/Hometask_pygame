import sys, pygame 
pygame.init()
w = 320
h = 240
size = (w, h)
screen = pygame.display.set_mode(size) 

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ballrect.left += 40
            if event.key == pygame.K_LEFT:
                ballrect.left -= 40
            if event.key == pygame.K_UP:
                ballrect.top -= 40
            if event.key == pygame.K_DOWN:
                ballrect.top += 40

    screen.fill((0, 0, 0))

    screen.blit(ball, ballrect)
    pygame.display.flip()