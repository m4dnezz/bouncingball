import pygame
import os
from colors import bg, all_colors, main_colors, whitest
from objects import Balls
from constants import fps, width, height, bigr, frames
import random
import numpy as np
from drawing import aacirlce

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

number_of_balls = 1
for i in range(1, number_of_balls + 1):
    random_color = main_colors[random.randint(0, len(main_colors) - 1)]
    random_radius = random.randint(5, 20)
    random_x_offset = random.randint(10, 50)
    random_y_offset = random.randint(10, 50)
    Balls(str(random_color), random_color, random_radius, 0, 400 + random_x_offset, 150 + random_y_offset, "golf_ball.wav")
    Balls.balls[-1].vely = random.randint(1, 2) * random.choice((-1, 1))
    Balls.balls[-1].velx = random.randint(1, 2) * random.choice((-1, 1))

# redball   = Balls("red ball", red, 8, 0, width//2-bigr+20, height//2-59, "bm.wav")
# redball   = Balls("red ball", golden, 8, 0, width//2-bigr+10, height//2, "golf_ball.wav")
# redball.vely = -5
# greenball = Balls("green ball", algeablue, 8, 0, width//2+bigr-20, height//2-50, "golf_ball.wav")
# yellowball = Balls("green ball", magenta2, 8, 0, width//3, height//2,"trm.wav")
# blueball = Balls("green ball", blue, 8, 0, width*2//3+5, height//2, "trm.wav")
# greenball = Balls("green ball", green, 12, 0, width//2+70, height//2-60)

pause = False
start_sim = False
muted = False

while start_sim is False:
    screen.fill(bg)
    screen.blit(background, [0, 0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                start_sim = True
    pygame.display.update()
    clock.tick(fps)


while True:
    screen.fill(bg)
    aacirlce(bigr, width // 2, height // 2, whitest, 1)

    for ball in Balls.balls:
        if len(ball.track) > 2 and Balls.trail:
            pygame.draw.aalines(screen, ball.trail_color, False, ball.track, 2)
    for ball in Balls.balls:
        ball.drawball(screen)
        if not pause:
            ball.wall_collision()
            ball.motion()
            ball.ball_collision()
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
            if event.key == pygame.K_c:
                Balls.balls[0].trail_color = all_colors[random.randint(0, len(all_colors) - 1)]
            if event.key == pygame.K_PLUS:
                if np.linalg.norm(np.subtract((Balls.balls[0].posx, Balls.balls[0].posy), (width // 2, height // 2))) + Balls.balls[0].radius * 1.1 + 5 < bigr:
                    Balls.balls[0].radius *= 1.1
            if event.key == pygame.K_MINUS:
                Balls.balls[0].radius /= 1.1
            if event.key == pygame.K_UP:
                Balls.balls[0].vely *= 1.1
            if event.key == pygame.K_DOWN:
                Balls.balls[0].vely /= 1.1
            if event.key == pygame.K_b:
                Balls.add_ball(muted)
            if event.key == pygame.K_m:
                if not muted:
                    for b in Balls.balls:
                        b.muted = True
                    muted = True
                elif muted:
                    for b in Balls.balls:
                        b.muted = False
                    muted = False
            if event.key == pygame.K_ESCAPE:
                quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            if event.button == 1:
                if np.linalg.norm(np.subtract(pygame.mouse.get_pos(), (width // 2, height // 2))) + Balls.balls[0].radius + 5 < bigr:
                    Balls.balls[0].posx, Balls.balls[0].posy = pygame.mouse.get_pos()
                    Balls.balls[0].velx, Balls.balls[0].vely = 0.0001, 0.0001  # Avoid division with 0
                    Balls.balls[0].track = list()

    pygame.display.update()
    clock.tick(fps)
    frames += 1


# TODO: Everything only works with one ball, no collisions between balls
# TODO: Mute button
# TODO: Remove balls from sim
# TODO: Spawned balls not muted
# TODO: Display number of balls
# TODO: Shorten trail depending on balls? Laggy with many balls
