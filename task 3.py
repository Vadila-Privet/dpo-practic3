import pygame
import time

G = 9.8

t = 0
dt = 0.01


class Robot:
    y = 0
    vy0 = 10
    vy = 0

    size_x = 10
    size_y = 10

    trace = []

    def move(self, y):
        self.y = y

    def calc_vy(self, t, G):
        self.vy = self.vy0 - G * t

    def calc_y(self, t, G):
        self.y = self.vy0 * t - (G * t ** 2) / 2


robot = Robot()

screen_x = 500
screen_y = 500

pygame.init()
screen = pygame.display.set_mode((screen_x, screen_y))

pygame.font.init()
my_font = pygame.font.SysFont(None, 30)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    while robot.y >= 0:
        robot.calc_vy(t, G)
        robot.calc_y(t, G)

        robot.trace.append({
            "vy": robot.vy,
            "y": robot.y
        })

        screen.fill(color=(0, 0, 0))

        pygame.draw.rect(surface=screen, color=(0, 255, 0), rect=pygame.Rect(250, screen_y - robot.y * 100, 10, 10))

        text_vy = f'vy = {round(robot.vy, 3)}'
        text_y = f'y = {round(robot.y, 3)}'

        text_surface_vy = my_font.render(text_vy, False, (255, 255, 255))
        screen.blit(text_surface_vy, (0, 0))

        text_surface_y = my_font.render(text_y, False, (255, 255, 255))
        screen.blit(text_surface_y, (0, 30))

        pygame.display.flip()

        t += dt

        time.sleep(dt)

    pygame.draw.rect(surface=screen, color=(0, 255, 0), rect=pygame.Rect(250, screen_y - robot.size_y, 10, 10))
    pygame.display.flip()

for point in robot.trace:
    print(point['vy'], point['y'])


