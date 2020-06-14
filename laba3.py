import sys, pygame 
pygame.init()
w = 360
h = 280
size = (w, h)
screen = pygame.display.set_mode(size) 

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
ball2 = pygame.image.load("ball2.png")
ballrect2 = ball2.get_rect()
#РАСЧИТАЕМ ВЫСОТУ И ШИРИНУ ОБЛАСТИ ИЗОБРАЖЕНИЯ
sizes = list(ball.get_rect().size)
sizes2 = list(ball2.get_rect().size)
#print(sizes) proverka [w,h]
imgw=sizes[0]
imgh=sizes[1]
imgw2=sizes2[0]
imgh2=sizes2[1]

steplimitheight=h//imgh
steplimitwidth=w//imgw

#помещаем 2 обьект приблизительно в середине изображения

ballrect2.left += (steplimitwidth//2)*imgw2
ballrect2.top += (steplimitheight//2)*imgh2

stepcountheight=0
stepcountwidth=0
s1=steplimitheight//2
s2=steplimitwidth//2


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if stepcountwidth!= steplimitwidth -1:
                    if (stepcountwidth == (s2-1)) and (stepcountheight == s1):
                        ballrect.left +=0
                    else:    
                        ballrect.left += imgw
                        stepcountwidth +=1
                        
            if event.key == pygame.K_LEFT:
                if stepcountwidth!=0:
                    if (stepcountwidth ==(s2+1)) and (stepcountheight ==s1) :
                        ballrect.left +=0
                    else:
                        ballrect.left -= imgw
                        stepcountwidth -=1
                        
            if event.key == pygame.K_UP:
                if stepcountheight!=0:
                    if (stepcountwidth ==s2) and (stepcountheight ==(s1+1)) :
                        ballrect.left +=0
                    else:
                        ballrect.top -= imgh
                        stepcountheight -=1
   
            if event.key == pygame.K_DOWN :
                if stepcountheight!=steplimitheight -1 :
                    if (stepcountwidth ==s2) and (stepcountheight ==(s1-1)) :
                        ballrect.left +=0
                    else:
                        ballrect.top += imgh
                        stepcountheight +=1   

    screen.fill((0, 0, 0))

    screen.blit(ball, ballrect)
    screen.blit(ball2,ballrect2)
    pygame.display.flip()