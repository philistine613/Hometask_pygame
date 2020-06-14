import sys, pygame 
pygame.init()
w = 320
h = 240
size = (w, h)
screen = pygame.display.set_mode(size) 

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
#РАСЧИТАЕМ ВЫСОТУ И ШИРИНУ ОБЛАСТИ ИЗОБРАЖЕНИЯ
sizes = list(ball.get_rect().size)
#print(sizes) proverka [w,h]
imgw=sizes[0]
imgh=sizes[1]

steplimitheight=h//imgh
steplimitwidth=w//imgw

stepcountheight=0
stepcountwidth=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if stepcountwidth!= steplimitwidth -1 :
                    ballrect.left += 40
                    stepcountwidth +=1
            if event.key == pygame.K_LEFT:
                if stepcountwidth!=0:
                    ballrect.left -= 40
                    stepcountwidth -=1
            if event.key == pygame.K_UP:
                if stepcountheight!=0:
                    ballrect.top -= 40
                    stepcountheight -=1
            if event.key == pygame.K_DOWN:
                if stepcountheight!=steplimitheight -1 :
                    ballrect.top += 40
                    stepcountheight +=1

    screen.fill((0, 0, 0))

    screen.blit(ball, ballrect)
    pygame.display.flip()