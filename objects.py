from constants import *
import pygame
from math import sqrt
from numpy import dot
import random
from colors import *


class Balls():
    trail = True
    balls = list()

    def __init__(self, name, color, radius, thicc, posx, posy, sound="metalmicrowave.wav", muted=False):
        Balls.balls.append(self)
        self.name = name
        self.color = color
        self.trail_color = color
        self.radius = radius
        self.thicc = thicc
        self.posx = posx
        self.posy = posy
        self.sound = f"audio/{sound}"
        self.muted = muted
        self.velx = 0
        self.vely = 0
        self.acc = g / fps
        self.track = list()

    def drawball(self, screen):
        pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius, self.thicc)

    def collision_handling(self):
        vel = sqrt(self.velx**2 + self.vely**2)
        # vel = 2 if vel >= 2 else vel

        x, y = centx, centy  # center of cirlce
        ballx, bally = self.posx, self.posy
        velx, vely = self.velx, self.vely
        # center to ball is the distance between ball's center and the ring's center
        center_to_ball = sqrt((x - ballx)**2 + (y - bally)**2)

        if center_to_ball >= (bigr - self.radius):
            # play bounce sound effect
            if not self.muted:
                pygame.mixer.Sound.play(pygame.mixer.Sound(self.sound))

            while sqrt((x - self.posx)**2 + (y - self.posy)**2) > (bigr - self.radius):
                step = 0.2
                # moving the ball backwawrds in dir of velocity by small steps
                self.posx += -self.velx * step / vel
                self.posy -= -self.vely * step / vel

            normal = ballx - x, bally - y
            normal_mag = center_to_ball  # sqrt(normal[0]**2 + normal[1]**2)
            n = normal[0] / normal_mag, normal[1] / normal_mag
            nx, ny = n[0], n[1]

            d = velx, -vely  # incident
            dx, dy = d[0], d[1]

            reflected = dx - 2 * dot(n, d) * nx, dy - 2 * dot(n, d) * ny

            self.velx = reflected[0]
            self.vely = -reflected[1]

            # a shitty fix to speed's gradual loss

            # r_size = sqrt(self.velx**2 + self.vely**2)
            # self.velx = reflected[0]*vel/r_size
            # self.vely = -reflected[1]*vel/r_size

    def motion(self):

        self.velx += 0
        self.vely += self.acc

        self.posx += self.velx
        self.posy -= self.vely

        every = 2
        period = 5
        if frames % every == 0 and Balls.trail:
            self.track.append((self.posx, self.posy))
        if Balls.trail is False:
            self.track.clear()
        elif len(self.track) > fps * period / every / (len(self.balls) * 0.01) :  # 240:
            while len(self.track) > fps * period / every / (len(self.balls) * 0.01) :
                self.track.pop(0)

    def add_ball(muted):
        random_color = main_colors[random.randint(0, len(main_colors) - 1)]
        random_radius = random.randint(5, 20)
        random_x_offset = random.randint(10, 50)
        random_y_offset = random.randint(10, 50)
        Balls(str(random_color), random_color, random_radius, 0, 400 + random_x_offset, 150 + random_y_offset, "golf_ball.wav", muted)
        Balls.balls[-1].vely = random.randint(1, 5) * random.choice((-1, 1))
        Balls.balls[-1].velx = random.randint(1, 2) * random.choice((-1, 1))
