import random # For generating random numbers
import math
import sys # We will use sys.exit to exit the program
import pygame
from pygame.locals import * # Basic pygame imports

GAME_SPRITES = {}
GAME_SOUNDS = {}
score = 0
speed = 0

def getOtherCar1():
    car ={'x1':random.randrange(60,120),'y1':-random.randrange(20,30)}
    return car
def getOtherCar2():
    car ={'x1':random.randrange(150,200),'y1':-random.randrange(120,150)}
    return car

def landingScreen():
    global score  
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(welcome, (0, 0))  
                #blitting Score
                myDigits = [int(x) for x in list(str(math.floor(score/100)))]
                width = 45
                for digit in myDigits:
                    width += GAME_SPRITES['numbers'][digit].get_width()
                Xoffset = (background.get_width() - width)

                for digit in myDigits:
                    SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, background.get_height()-180))
                    Xoffset += GAME_SPRITES['numbers'][digit].get_width()      
                pygame.display.update()


def mainGame():
    global score
    speed = 1
    crashed = False
    
    my_car_x=(background.get_width()/2)-(my_car.get_width()/2)
    my_car_y=background.get_height()-my_car.get_height()


    # receive other car 
    car1 = [{'x1':90,'y1':-20}
    ]
    car2 = [{'x1':170,'y1':-40}
    ]
    
    i=0
    while True:
        for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and (event.key == K_LEFT ):
                    if my_car_x>=60:
                        my_car_x-=20
                        # print(my_car_x) #55.0
                if event.type == KEYDOWN and event.key == K_RIGHT:
                    if my_car_x<=background.get_width()-110:
                        my_car_x+=20
                        # print(my_car_x) #195.0
        
        if crashed:
            return                  

        #move others car
        for c1,c2 in zip(car1,car2):
            c1['y1']+=speed
            c2['y1']+=speed
        
        #add new car
        if car1[len(car1)-1]['y1']>((background.get_height()/100)*50) and car2[len(car2)-1]['y1']>((background.get_height()/100)*50):
            newcar = getOtherCar1()
            car1.append(newcar)
            newcar2 = getOtherCar2()
            car2.append(newcar2)

        #delete outer cars
        if car1[0]['y1']>background.get_height() and car2[0]['y1']>background.get_height():
            car1.pop(0)
            car2.pop(0)

        #score calculate
        for c1 , c2 in zip(car1,car2):
            # car crasherd
            if (my_car_x+28>c1['x1'] and my_car_x < c1['x1']+28) and (my_car_y < c1['y1']+50 and my_car_y+50 > c1['y1']) or (my_car_x+28>c2['x1'] and my_car_x < c2['x1']+28) and (my_car_y < c2['y1']+50 and my_car_y+50 > c2['y1']):
                crashed = True
            #not crashed
            else:
                if (my_car_y < c1['y1']+51 and my_car_y+50 > c1['y1']):
                    score +=1
                if (my_car_y < c2['y1']+51 and my_car_y+50 > c2['y1']):
                    score += 1
        

        #lets Blit the screen
        SCREEN.blit(background,(0,0+i))
        SCREEN.blit(background,(0,-(background.get_height()-i)))
        SCREEN.blit(my_car,(my_car_x,my_car_y))

        #blitting others car
        for c1,c2 in zip(car1,car2):        
            SCREEN.blit(otherscar1,(c1['x1'],c1['y1']))
            SCREEN.blit(otherscar2,(c2['x1'],c2['y1']))


        #blitting Score
        myDigits = [int(x) for x in list(str(math.floor(score/100)))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (background.get_width() - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, background.get_height()*0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()


        pygame.display.update()
        #for move background
        i+=speed
        if i>=background.get_height():
            i=0

        # increase speed
        if score !=0 and ((math.floor(score/100))%10)==0:
            speed+=((1/265)*0.1)

        


if __name__ == "__main__":
    #initializing pygame
    pygame.init()
    pygame.display.set_caption('carGame')
    SCREEN = pygame.display.set_mode((300,500))
    background = pygame.image.load('gallery/images/background.png')
    welcome = pygame.image.load('gallery/images/welcome.png')
    my_car = pygame.image.load('gallery/images/car.png').convert_alpha()
    otherscar1 = pygame.image.load('gallery/images/otherscar1.png').convert_alpha()
    otherscar2 = pygame.image.load('gallery/images/otherscar2.png').convert_alpha()
    # cave = pygame.image.load('gallery/images/cave.png').convert_alpha()
    
    GAME_SPRITES['numbers'] = ( 
        pygame.image.load('gallery/images/0.png').convert_alpha(),
        pygame.image.load('gallery/images/1.png').convert_alpha(),
        pygame.image.load('gallery/images/2.png').convert_alpha(),
        pygame.image.load('gallery/images/3.png').convert_alpha(),
        pygame.image.load('gallery/images/4.png').convert_alpha(),
        pygame.image.load('gallery/images/5.png').convert_alpha(),
        pygame.image.load('gallery/images/6.png').convert_alpha(),
        pygame.image.load('gallery/images/7.png').convert_alpha(),
        pygame.image.load('gallery/images/8.png').convert_alpha(),
        pygame.image.load('gallery/images/9.png').convert_alpha(),
    )


    while True:
        landingScreen()
        mainGame()
        
