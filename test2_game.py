# this code is to show use of pygame module in python
# importing various modules

import pygame
import time

from config import *

# this is another way of importing from modules

pygame.init()
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_a, K_s, K_d, \
    K_w

pygame.mixer.music.load(tone)

# pause = False

initiate_time = pygame.time.get_ticks()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PyGame: DEV_ED_2020 BHASKAR')
clock = pygame.time.Clock()

previous_sec = pygame.time.get_ticks()

# creating group for sprite

obs_group = pygame.sprite.Group()


# creatiing a class for moving
# obstacle like the bullets

class Obs(pygame.sprite.Sprite):

    def __init__(self, location):
        super().__init__()

        # self.rect = pygame.draw.rect(gameDisplay, yellow, location)

        self.surf = pygame.Surface((location[2], location[3]))

        # self.surf =pygame.Surface((100,200))

        self.surf.fill(yellow)
        self.rect = self.surf.get_rect()

        # self.rect=self.surf.get_rect()

        (self.rect.left, self.rect.top, self.rect.w, self.rect.h) = \
            location

    def update(self, spd_inc):
        self.rect.move_ip(spd_inc, 0)
        if self.rect.left > display_width:
            self.rect.left = 0 - thing_width


# creating object of class

obs_obj1 = Obs([-600, 150, 50, 5])
obs_obj2 = Obs([-390, 250, 50, 5])
obs_obj3 = Obs([-943, 350, 50, 5])
obs_obj4 = Obs([-745, 450, 50, 5])
obs_obj5 = Obs([-1256, 550, 50, 5])

# adding those objects to group

obs_group.add(obs_obj1)
obs_group.add(obs_obj2)
obs_group.add(obs_obj3)
obs_group.add(obs_obj4)
obs_group.add(obs_obj5)


# creating class for fixed objects

class Bombs(pygame.sprite.Sprite):

    def __init__(self, location):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('smallbomb2.png')
        self.rect = self.image.get_rect()
        (self.rect.left, self.rect.top) = location


# creating objects of fixed obstacles

Bombs_obj1 = Bombs([a1, 200])
Bombs_obj2 = Bombs([a2, 300])
Bombs_obj3 = Bombs([a3, 400])
Bombs_obj4 = Bombs([a4, 500])
Bombs_obj5 = Bombs([a5, 600])
Bombs_obj6 = Bombs([a6, 100])

# adding those objects to group

obs_group.add(Bombs_obj1)
obs_group.add(Bombs_obj2)
obs_group.add(Bombs_obj3)
obs_group.add(Bombs_obj4)
obs_group.add(Bombs_obj5)
obs_group.add(Bombs_obj6)


# defining class for player 1

class Player1(pygame.sprite.Sprite):

    def __init__(self, location):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sply1n.png')
        self.rect = self.image.get_rect()
        (self.rect.left, self.rect.top) = location

    # updating the values for player 1

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 1160:
            self.rect.right = 1160
        if self.rect.top < -10:
            self.rect.top = display_height * 0.90
        elif self.rect.bottom > 665:
            self.rect.bottom = 660


# creating object of player 1

player1_obj = Player1([x, y])


# creating class for player 2

class Player2(pygame.sprite.Sprite):

    def __init__(self, location):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('sply2.png')
        self.rect = self.image.get_rect()
        (self.rect.left, self.rect.top) = location

    # updating values for player 2

    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_a]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 1160:
            self.rect.right = 1160
        if self.rect.top < -10:
            self.rect.top = 0
        elif self.rect.bottom > 665:
            self.rect.bottom = display_height * 0.07


# creating object for player 2

player2_obj = Player2([x2, y2])


# defining function to quit game

def quitgame():
    pygame.quit()
    quit()


def unpause():
    global pause
    pause = False


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return (textSurface, textSurface.get_rect())


# defing a function to display messages

# defining values for text in small size

def message_displaysmall(text, x, y):
    text1 = smallText.render(text, True, yellow_text)
    gameDisplay.blit(text1, (x, y))


# defining function for red and white caution lane
# also called safe zone

def caution(x, y):
    gameDisplay.blit(caution2, (x, y))


# defining function to call bomb mines

def bomb(x, y):
    gameDisplay.blit(bomb2, (x, y))


# defininf function for displaying text screens

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 50)
    (TextSurf, TextRect) = text_objects(text, largeText)
    TextRect.center = (display_width / 2, display_height / 2)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)


# defining function to check for player1
# to check if he has crossed obsticle or not
# the simple thing is if object has crossed
# score will be awarded, if fixed obstacle
# player will have +5 and +10 for crossing moving obstacle
# there is time penalty of -1
# the more the player stays the lesser the score he has

def score(
    y_cord,
    playerLife1,
    obs_pass,
    obs_ycord,
    ply_score,
    ):

    if y_cord < obs_ycord and playerLife1 is True and obs_pass:
        if obs_ycord % 100 == 0:
            ply_score += 5
        elif obs_ycord % 100 == 50:
            ply_score += 10
    return ply_score


flag = True


# defining function to check for player2
# to check if he has crossed obstical or not

def scorep2(
    y_cord,
    playerLife2,
    obs_pass,
    obs_ycord,
    ply_score,
    ):

    if y_cord > obs_ycord and playerLife2 is True and obs_pass:
        if obs_ycord % 100 == 0:
            ply_score += 5
        elif obs_ycord % 100 == 50:
            ply_score += 10
    return ply_score


# most importantly defining buttons for
# giving button hovering effect

def button(
    msg,
    x,
    y,
    w,
    h,
    ic,
    ac,
    action=None,
    ):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:

        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    (TextSurf, TextRect) = text_objects(msg, smallText)
    TextRect.center = (x + w / 2, y + h / 2)
    gameDisplay.blit(TextSurf, TextRect)


# this gives the instruction we need
# to tell to player
# if a person stays for a longer time
# he will be having tome penalty
# which means his total score minus
# time spent in playing the game

def game_instructions():
    gameDisplay.fill(black)
    message_displaysmall('For Player 1:', 200, 200)
    message_displaysmall('For Player 2:', 800, 200)
    message_displaysmall('UP ', 200, 225)
    message_displaysmall('DOWN ', 200, 250)
    message_displaysmall('LEFT  ', 200, 275)
    message_displaysmall('RIGHT', 200, 300)
    message_displaysmall(':', 300, 225)
    message_displaysmall(':', 300, 250)
    message_displaysmall(':', 300, 275)
    message_displaysmall(':', 300, 300)
    message_displaysmall('ARROW UP', 400, 225)
    message_displaysmall('ARROW DOWN', 400, 250)
    message_displaysmall('ARROW LEFT', 400, 275)
    message_displaysmall('ARROW RIGHT', 400, 300)

    message_displaysmall('UP', 800, 225)
    message_displaysmall('DOWN', 800, 250)
    message_displaysmall('LEFT', 800, 275)
    message_displaysmall('RIGHT', 800, 300)
    message_displaysmall(':', 900, 225)
    message_displaysmall(':', 900, 250)
    message_displaysmall(':', 900, 275)
    message_displaysmall(':', 900, 300)
    message_displaysmall('W', 1000, 225)
    message_displaysmall('S', 1000, 250)
    message_displaysmall('A', 1000, 275)
    message_displaysmall('D', 1000, 300)
    message_displaysmall(win_msg1, 150, 400)
    message_displaysmall(crash_msg1, 150, 500)

    largeText = pygame.font.Font('freesansbold.ttf', 80)
    (TextSurf, TextRect) = text_objects('Instructions', largeText)
    TextRect.center = (display_width / 2, display_height / 5)
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():

            # print(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button(
            'Start Game',
            350,
            550,
            120,
            50,
            dark_green,
            green,
            game_loop,
            )

        button(
            'QUIT???',
            750,
            550,
            120,
            50,
            dark_red,
            red,
            quitgame,
            )
        pygame.display.update()
        clock.tick(2)


def crash():
    global level, playerLife2, playerLife1, score2, score1, time1, \
        time2, final_scr_pl1, final_scr_pl2, largeText
    gameDisplay.fill(black)
    message_displaysmall('FINAL SCORES', 200, 325)
    message_displaysmall('PLAYER 1:', 300, 400)
    message_displaysmall(str(final_scr_pl1), 425, 400)
    message_displaysmall('PLAYER 2:', 300, 450)
    message_displaysmall(str(final_scr_pl2), 425, 450)
    if final_scr_pl1 > final_scr_pl2:
        message_displaysmall(win_msg2, 500, 500)
    elif final_scr_pl2 > final_scr_pl1:
        message_displaysmall(win_msg3, 500, 500)
    else:
        message_displaysmall(win_msg4, 100, 500)
    largeText = pygame.font.Font('freesansbold.ttf', 80)
    (TextSurf, TextRect) = text_objects('Game Over', largeText)
    TextRect.center = (display_width // 2, display_height // 3)
    gameDisplay.blit(TextSurf, TextRect)

    level = 3
    playerLife1 = True
    playerLife2 = True
    score1 = 0
    score2 = 0
    final_scr_pl2 = 0
    final_scr_pl1 = 0
    time1 = [0, 0, 0, 0]
    time2 = [0, 0, 0, 0]
    while True:
        for event in pygame.event.get():

            # print(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button(
            'Play Again',
            350,
            600,
            120,
            50,
            dark_green,
            green,
            game_loop,
            )
        button(
            'QUIT???',
            750,
            600,
            100,
            50,
            dark_red,
            red,
            quitgame,
            )
        pygame.display.update()
        clock.tick(2)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        (TextSurf, TextRect) = text_objects("Hey!!! It's PyGame",
                largeText)
        TextRect.center = (display_width // 2, display_height // 3)
        gameDisplay.blit(TextSurf, TextRect)

        button(
            'GO!!!',
            350,
            550,
            100,
            50,
            dark_green,
            green,
            game_loop,
            )
        button(
            'QUIT???',
            750,
            550,
            100,
            50,
            dark_red,
            red,
            quitgame,
            )
        button(
            'Instructions',
            550,
            550,
            130,
            50,
            yellow_text,
            yellow,
            game_instructions,
            )
        pygame.display.update()
        clock.tick(2)


def game_loop():
    pygame.mixer.music.play(-1)
    thing_speed = 7
    gameExit = False
    while not gameExit:
        gameDisplay.blit(bgimg, (0, 0))
        caution(0, 100)
        caution(0, 200)
        caution(0, 300)
        caution(0, 400)
        caution(0, 500)
        caution(0, 600)
        gameDisplay.blit(cannon, (0, 150))
        gameDisplay.blit(cannon, (0, 250))
        gameDisplay.blit(cannon, (0, 350))
        gameDisplay.blit(cannon, (0, 450))
        gameDisplay.blit(cannon, (0, 550))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        global playerLife1, playerLife2, player1_obj, player2_obj
        global level, prev_level
        global obs_of_pass1, obs_of_pass2
        prev_level = level
        if level <= 0:
            pygame.quit()
            quit()
        if playerLife1 is False and playerLife2 is False:
            thing_speed = thing_speed + 10

            level = level - 1
            player1_obj.rect.x = display_width * 0.48
            player1_obj.rect.y = display_height * 0.90
            player2_obj.rect.x = display_width * 0.48
            player2_obj.rect.y = display_height * 0.07
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
            playerLife1 = True
            playerLife2 = True

        if player2_obj.rect.y > 620 and level > 0 or player1_obj.rect.y \
            < 0 and level > 0:
            thing_speed = thing_speed + 10
            level = level - 1
            player1_obj.rect.x = display_width * 0.48
            player1_obj.rect.y = display_height * 0.90
            player2_obj.rect.x = display_width * 0.48
            player2_obj.rect.y = display_height * 0.035
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
            playerLife1 = True
            playerLife2 = True

        global score1, score2
        message_displaysmall('END', 580, 10)
        message_displaysmall('START', 560, 680)
        message_displaysmall('LEVEL:', 10, 10)
        message_displaysmall(str(4 - level), 80, 10)
        message_displaysmall('PLAYER1:', 200, 10)
        message_displaysmall('PLAYER2:', 1000, 10)
        message_displaysmall(str(score1), 300, 10)
        message_displaysmall(str(score2), 1100, 10)
        message_displaysmall('Total Time Taken By Player 1:', 50, 660)
        message_displaysmall(str(time1[3]), 375, 660)

        message_displaysmall('Total Time Taken By Player 2:', 800, 660)
        message_displaysmall(str(time2[3]), 1125, 660)

        temp1 = score1
        score1 = score(player1_obj.rect.y, playerLife1,
                       obs_of_pass1[0], 600, score1)
        if temp1 != score1:
            obs_of_pass1[0] = False
        temp1 = score1
        score1 = score(player1_obj.rect.y, playerLife1,
                       obs_of_pass1[2], 500, score1)
        if temp1 != score1:
            obs_of_pass1[2] = False
        temp1 = score1
        score1 = score(player1_obj.rect.y, playerLife1,
                       obs_of_pass1[4], 400, score1)
        if temp1 != score1:
            obs_of_pass1[4] = False
        temp1 = score1
        score1 = score(player1_obj.rect.y, playerLife1,
                       obs_of_pass1[6], 300, score1)
        if temp1 != score1:
            obs_of_pass1[6] = False
        temp1 = score1
        score1 = score(player1_obj.rect.y, playerLife1,
                       obs_of_pass1[8], 200, score1)

        if temp1 != score1:
            obs_of_pass1[8] = False
        temp1 = score1
        score1 = score(player1_obj.rect.y, playerLife1,
                       obs_of_pass1[10], 100, score1)
        if temp1 != score1:
            obs_of_pass1[10] = False

        temp1 = score1
        score1 = score(player1_obj.rect.y, playerLife1,
                       obs_of_pass1[1], 550, score1)
        if temp1 != score1:
            obs_of_pass1[1] = False

        temp1 = score1
        score1 = score(player1_obj.rect.y, playerLife1,
                       obs_of_pass1[3], 450, score1)
        if temp1 != score1:
            obs_of_pass1[3] = False

        temp1 = score1
        score1 = score(player1_obj.rect.y, playerLife1,
                       obs_of_pass1[5], 350, score1)
        if temp1 != score1:
            obs_of_pass1[5] = False

        temp1 = score1
        score1 = score(player1_obj.rect.y, playerLife1,
                       obs_of_pass1[7], 250, score1)
        if temp1 != score1:
            obs_of_pass1[7] = False

        temp1 = score1
        score1 = score(player1_obj.rect.y, playerLife1,
                       obs_of_pass1[9], 150, score1)
        if temp1 != score1:
            obs_of_pass1[9] = False

        temp2 = score2
        score2 = scorep2(player2_obj.rect.y, playerLife2,
                         obs_of_pass2[0], 100, score2)
        if temp2 != score2:
            obs_of_pass2[0] = False

        temp2 = score2
        score2 = scorep2(player2_obj.rect.y, playerLife2,
                         obs_of_pass2[2], 200, score2)
        if temp2 != score2:
            obs_of_pass2[2] = False

        temp2 = score2
        score2 = scorep2(player2_obj.rect.y, playerLife2,
                         obs_of_pass2[4], 300, score2)
        if temp2 != score2:
            obs_of_pass2[4] = False

        temp2 = score2
        score2 = scorep2(player2_obj.rect.y, playerLife2,
                         obs_of_pass2[6], 400, score2)
        if temp2 != score2:
            obs_of_pass2[6] = False

        temp2 = score2
        score2 = scorep2(player2_obj.rect.y, playerLife2,
                         obs_of_pass2[8], 500, score2)
        if temp2 != score2:
            obs_of_pass2[8] = False

        temp2 = score2
        score2 = scorep2(player2_obj.rect.y, playerLife2,
                         obs_of_pass2[10], 600, score2)
        if temp2 != score2:
            obs_of_pass2[10] = False

        temp2 = score2
        score2 = scorep2(player2_obj.rect.y, playerLife2,
                         obs_of_pass2[1], 150, score2)
        if temp2 != score2:
            obs_of_pass2[1] = False

        temp2 = score2
        score2 = scorep2(player2_obj.rect.y, playerLife2,
                         obs_of_pass2[3], 250, score2)
        if temp2 != score2:
            obs_of_pass2[3] = False

        temp2 = score2
        score2 = scorep2(player2_obj.rect.y, playerLife2,
                         obs_of_pass2[5], 350, score2)
        if temp2 != score2:
            obs_of_pass2[5] = False

        temp2 = score2
        score2 = scorep2(player2_obj.rect.y, playerLife2,
                         obs_of_pass2[7], 450, score2)
        if temp2 != score2:
            obs_of_pass2[7] = False
        temp2 = score2
        score2 = scorep2(player2_obj.rect.y, playerLife2,
                         obs_of_pass2[9], 550, score2)
        if temp2 != score2:
            obs_of_pass2[9] = False

        obs_obj1.update(thing_speed)
        gameDisplay.blit(obs_obj1.surf, obs_obj1.rect)
        obs_obj2.update(thing_speed)
        gameDisplay.blit(obs_obj2.surf, obs_obj2.rect)
        obs_obj3.update(thing_speed)
        gameDisplay.blit(obs_obj3.surf, obs_obj3.rect)
        obs_obj4.update(thing_speed)
        gameDisplay.blit(obs_obj4.surf, obs_obj4.rect)
        obs_obj5.update(thing_speed)
        gameDisplay.blit(obs_obj5.surf, obs_obj5.rect)
        gameDisplay.blit(Bombs_obj1.image, Bombs_obj1.rect)
        gameDisplay.blit(Bombs_obj2.image, Bombs_obj2.rect)
        gameDisplay.blit(Bombs_obj3.image, Bombs_obj3.rect)
        gameDisplay.blit(Bombs_obj4.image, Bombs_obj4.rect)
        gameDisplay.blit(Bombs_obj5.image, Bombs_obj5.rect)
        gameDisplay.blit(Bombs_obj6.image, Bombs_obj6.rect)
        pressed_keys = pygame.key.get_pressed()
        if playerLife1 is True:
            player1_obj.update(pressed_keys)
            gameDisplay.blit(player1_obj.image, player1_obj.rect)
        pressed_keys = pygame.key.get_pressed()
        if playerLife2 is True:
            player2_obj.update(pressed_keys)
            gameDisplay.blit(player2_obj.image, player2_obj.rect)

        if pygame.sprite.spritecollide(player1_obj, obs_group, False):
            playerLife1 = False
            player1_obj.kill()
            player1_obj = Player1([x, y])

        if pygame.sprite.spritecollide(player2_obj, obs_group, False):
            playerLife2 = False
            player2_obj.kill()
            player2_obj = Player2([x2, y2])
        global previous_sec
        if pygame.time.get_ticks() - previous_sec > 1000:
            previous_sec = pygame.time.get_ticks()
            if playerLife1:
                time1[3 - level] += 1
            if playerLife2:
                time2[3 - level] += 1

        # print(time1)
        # print(time2)

        global final_scr_pl1, final_scr_pl2

        time1[3] = time1[0] + time1[1] + time1[2]
        time2[3] = time2[0] + time2[1] + time2[2]
        final_scr_pl1 = score1 - time1[3]
        final_scr_pl2 = score2 - time2[3]

        # I need to display this on screen

        if level == 0:
            crash()

        pygame.display.update()


        # clock.tick(100)

message_display('Welcome To PyGame By Bhaskar Joshi')
game_intro()

game_loop()
pygame.quit()
quit()
