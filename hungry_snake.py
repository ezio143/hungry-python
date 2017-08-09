# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
import random


pygame.init()
width = 600
height = 400
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,155,155)
green = (0,155,0)
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption("HungryPython")

gameDisplay.fill(white)
img = pygame.image.load("snkhd.png")

clock = pygame.time.Clock()
gameOver = True
FPS = 15

smallfont = pygame.font.SysFont("comicsansms",25)
mediumfont = pygame.font.SysFont("comicsansms",40)
largefont = pygame.font.SysFont("somicsansms",65)


direction  = "right"


#function to create the game intro

def game_intro():
    intro = True
    
    while intro:
        displayMessage("Welcom to HungryPython ",green,-100,"large")
        
        displayMessage("eat as much as apple's possible  ",blue,size="medium")
        
        displayMessage("press c to start playing ",blue,70,"medium")
        
        displayMessage("press q to quit ",blue,+100,"small")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                if event.key == pygame.K_c:
                    intro = False
        
        
        
        pygame.display.update()
        
        clock.tick(FPS)

def snake(block_size,snakeList):
    
    if direction == "right":
        head = pygame.transform.rotate(img,270)
        
    
    if direction == "left":
        head = pygame.transform.rotate(img,90)
        
    
    if direction == "up":
        head = img
        
    
    if direction == "down":
        head = pygame.transform.rotate(img,180)
        
        
        
    gameDisplay.blit(head, (snakeList[-1][0],snakeList[-1][1])) #draw the attached head
    
    for XnY in snakeList[:-1]: # draw the body 
        pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])

        
def text_object(msg,color,size):
    if size == "large":
        text_surface = largefont.render(msg,True,color)
    elif size == "medium":
        text_surface = mediumfont.render(msg,True,color)
    elif size == "small":
        text_surface = smallfont.render(msg,True,color)
    
    return text_surface,text_surface.get_rect()
        
        
def displayMessage(msg,color,y_displace=0,size = "small"):
    text_surface,text_rect = text_object(msg,color,size)
    text_rect.center = (width/2),(height/2)+y_displace
    #screenText = font.render(msg,True,color)
    gameDisplay.blit(text_surface,text_rect)

def gameLoop():
    lead_x = width/2
    lead_y = height/2
    lead_dx,lead_dy = 0,0
    
    snakeList = []
    snakeLength = 1

    appleThickness = 30
    block_size = 20
    gameExit = False
    gameOver = False
    
    global direction # tell the function to use the global value of direction 
    
    # to get the apple in the same row as snake 
    appleX = round(random.randrange(0,width - appleThickness)/10.0) * 10.00
    appleY = round(random.randrange(0,height - appleThickness)/10.0) * 10.0
    
    
    
    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill(white)
            displayMessage("Game Over",
                           red,
                           y_displace=-50,
                           size= "large")
            displayMessage("press c to play again, q to quit",
                           black,
                           size = "small")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        gameLoop()    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_dx = -block_size
                    lead_dy = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_dx = +block_size
                    lead_dy = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_dy = -block_size
                    lead_dx = 0
                elif event.key == pygame.K_DOWN:
                    direction  =  "down"
                    lead_dy = block_size
                    lead_dx = 0
                    
                elif event.key == pygame.K_q:
                    gameOver = True
        lead_x += lead_dx
        lead_y += lead_dy
        if lead_x > width - block_size:
            lead_x = block_size
        if lead_x < 0 :
            lead_x = width - block_size
        if lead_y >= height :
            lead_y = 0
        if lead_y < 0:
            lead_y = height
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,black,[appleX,appleY,appleThickness,appleThickness])
        
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        
        if len(snakeList) > snakeLength:
            del snakeList[0]
        
        for everyblock in snakeList[:-1]:
            if everyblock == snakeHead:
                gameOver = True

        snake(block_size,snakeList)      
        
        if lead_x > appleX and lead_x < appleX + appleThickness or lead_x + block_size > appleX and lead_x + block_size < appleX + appleThickness : 
            if lead_y > appleY and lead_y < appleY + appleThickness or lead_y + block_size > appleY and lead_y + block_size < appleY + appleThickness:
                        
                appleX = round(random.randrange(0,width - block_size)/10.0) * 10.0
                appleY = round(random.randrange(0,height - block_size)/10.0) * 10.0
                snakeLength += 1
                
        
        
        pygame.display.update()        
        clock.tick(FPS)
    
        
    pygame.quit()
    

game_intro()
gameLoop()