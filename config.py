#!/usr/bin/python
# introducing config file

import random
import pygame
pygame.init()

# setting fixed screen size

display_width = 1200
display_height = 700

# defining colours for usage in code

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow_text = (245, 218, 66)
yellow = (236, 253, 10)
dark_green = (0, 200, 0)
dark_red = (200, 0, 0)

# defining global variables

tone = 'mission.mp3'
pause = False

time_p1 = 0
time_p2 = 0

# locating images which I have used

bgimg = pygame.image.load('bg1new.png')
caution2 = pygame.image.load('caution2.png')
player1 = pygame.image.load('sply1n.png')
player2 = pygame.image.load('sply2.png')
bomb2 = pygame.image.load('smallbomb2.png')
cannon = pygame.image.load('smallcannon3.png')
largeText = pygame.font.Font('freesansbold.ttf', 50)
smallText = pygame.font.Font('freesansbold.ttf', 20)

win_msg1 = \
    'CROSS THE PATH BEFORE YOUR OPPONENT WITHOUT GETTING HIT WITH AN OBSTACLE'
win_msg2 = 'PLAYER 1 wins'
win_msg3 = 'PLAYER 2 wins'
win_msg4 = 'IT WAS A TIE EVEN AFTER CONSIDERING TIME SCORE'
crash_msg1 = 'THERE IS TIME PENALTY FOR EACH SECOND'
playerLife1 = True
playerLife2 = True
score1 = 0
score2 = 0
time1 = [0, 0, 0, 0]
time2 = [0, 0, 0, 0]

prev_level = 0
level = 3
thing_width = 50
thing_height = 5
final_scr_pl1 = 0
final_scr_pl2 = 0

# defining if obstical  is passed or not
# if passed it is defined as False else True

obs_of_pass1 = [
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    ]
obs_of_pass2 = [
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    ]

# setting random values for bullets to come

a1 = random.randint(1, 1200)
a2 = random.randint(1, 1200)
a3 = random.randint(1, 1200)
a4 = random.randint(1, 1200)
a5 = random.randint(1, 400)
a6 = random.randint(1, 1200)

# assigning by default coordinates of both players

x = display_width * 0.48
y = display_height * 0.90
x2 = display_width * 0.48
y2 = display_height * 0.035


# defing a function to display messages

def message_display(text):
    (TextSurf, TextRect) = text_objects(text, largeText)
    TextRect.center = (int(display_width) / 2, display_height / 2)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()
