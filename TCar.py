import pygame
import time


win = pygame.display.set_mode((800, 450))
pygame.display.set_caption("ТСar")
bg = pygame.image.load('Bg_title/фон_1.jpg')
title = pygame.image.load('Bg_title/title.png')
x = 10
y = 240


class Road:
    def __init__(self):
        self.image = pygame.image.load('Road_car/55356.png')


class Car:
    def __init__(self, speed):
        self.image = pygame.image.load('Road_car/Car_2.png')
        self.speed = speed


class TrafficLight:
    def __init__(self, condition=True):
        self.img_green = pygame.image.load('traffic_light/Green.png')
        self.img_green = pygame.transform.scale(self.img_green, (150, 300))
        self.img_yellow = pygame.image.load('traffic_light/Yellow.png')
        self.img_yellow = pygame.transform.scale(self.img_yellow, (150, 300))
        self.img_red = pygame.image.load('traffic_light/Red.png')
        self.img_red = pygame.transform.scale(self.img_red, (150, 300))
        self.color = ''
        self.sec = 0
        self.condition = condition

    def change_color(self):
        while True:
            self.sec += 1
            if self.sec <= 400:
                self.color = self.img_green
                self.condition = True
                return self.color
            elif 400 < self.sec <= 550:
                self.color = self.img_yellow
                self.condition = True
                return self.color
            elif 550 < self.sec <= 1050:
                self.color = self.img_red
                self.condition = False
                return self.color
            else:
                self.sec = 0
            time.sleep(1)


road = Road()
car = Car(5)
traffic_light = TrafficLight()


def draw_window():
    win.blit(bg, (0, 0))
    win.blit(title, (250, 0))
    win.blit(traffic_light.change_color(), (550, 10))
    img_car = car.image
    img_road = road.image
    img_car = pygame.transform.scale(img_car, (200, 150))
    img_road = pygame.transform.scale(img_road, (200, 200))  # Уменьшение картинки
    img_road = pygame.transform.rotate(img_road, 90)  # Переворот картинки
    for i in range(0, 600 + 1, 200):
        win.blit(img_road, (i, 250))
    win.blit(img_car, (x, y))

    pygame.display.update()


run = True
while run:

    pygame.time.delay(10)
    draw_window()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_RIGHT] and traffic_light.condition == True) or \
            (keys[pygame.K_RIGHT] and x not in range(400, 450)):
        x = x + car.speed

    if (keys[pygame.K_LEFT] and traffic_light.condition == True) or (keys[pygame.K_LEFT] and x < 540):
        x = x - car.speed + 0.4*car.speed
    if x > 800:
        x = -100
    if x < -100:
        x = 800
