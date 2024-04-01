from pygame.gfxdraw import circle
# from reflection import arrow, yellow
from drawing import aacirlce
import pygame
import os
import time as t
from math import acos, atan2, sin, cos, sqrt, pi
# import math
from test import dot
from colors import *
from objects import Balls
from constants import *

# Game presets
start_time = t.time()


# Centers window
x, y = 1360 - width, 40
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing balls")
clock = pygame.time.Clock()

background = pygame.image.load("img/start_img.png")

# initialize pygame mixer and load audio file
pygame.mixer.init()
# pygame.mixer.music.load('audio/golf_ball.wav')  # audio options [golfball, ground_impact, metalmicrowave, golf_ball]

# font = pygame.font.Font('freesansbold.ttf', 15)

# redball   = Balls("red ball", red, 8, 0, width//2-bigr+20, height//2-59, "bm.wav")
redball   = Balls("red ball", golden, 8, 0, width//2-bigr+10, height//2, "golf_ball.wav")
redball.vely = -5
# greenball = Balls("green ball", algeablue, 8, 0, width//2+bigr-20, height//2-50, "golf_ball.wav")
# yellowball = Balls("green ball", magenta2, 8, 0, width//3, height//2,"trm.wav")
# blueball = Balls("green ball", blue, 8, 0, width*2//3+5, height//2, "trm.wav")
# greenball = Balls("green ball", green, 12, 0, width//2+70, height//2-60)

pause = False
start_sim = False 


while start_sim is False:
    
    screen.fill(bg)
    screen.blit(background, [0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                start_sim = True
    


    pygame.display.update()
    clock.tick(fps)


while True:

    # draw_cricle(yellow, 2, 0, width//2, height//2)
    # draw(red, height//3, 3, width//2, height//2)
    

    screen.fill(bg)
    aacirlce(bigr, width//2, height//2, whitest, 1)

    for ball in Balls.balls:
        if len(ball.track)> 2 and Balls.trail:
            pygame.draw.aalines(screen, ball.color, False, ball.track, 2)
    for ball in Balls.balls:
        ball.drawball(screen)
        if not pause:
            ball.collision_handling()
            ball.motion()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
            if event.key == pygame.K_t:
                Balls.trail = not Balls.trail
                # if trail is False:
                #     for ball in Balls.balls:
                #         ball.track.clear()
    

    pygame.display.update()
    clock.tick(fps)
    frames += 1


























# vel = redball.vel
# arrow(arrow_color, arrow_color, (redball.posx, redball.posy), (redball.posx+vel*10*cos(redball.theta), redball.posy-vel*10*sin(redball.theta)), 1)
# rect = [redball.posx - 15 ,redball.posy-15, 30,30]
# pygame.draw.line(screen, orange, (redball.posx, redball.posy), (redball.posx +25, redball.posy), 2 )
# pygame.draw.rect(screen, yellow, rect, 4)
# draw_cricle(red, 2, 0, redball.posx-15, redball.posy-15)
# pygame.draw.arc(screen, white, rect, 0, redball.theta, 2)
# arrow(arrow_color, arrow_color, (greenball.posx, greenball.posy), (greenball.posx+vel*10*cos(greenball.theta), greenball.posy-vel*10*sin(greenball.theta)), 1)
    
    