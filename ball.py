import pygame
from settings import *

class Ball:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2

        self.dx = BALL_SPEED
        self.dy = BALL_SPEED

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Rebote arriba y abajo
        if self.y - BALL_RADIUS <= 0:
            self.dy *= -1

        if self.y + BALL_RADIUS >= HEIGHT:
            self.dy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), BALL_RADIUS)

    def collide(self, paddle):
        paddle_rect = paddle.rect

        if paddle_rect.collidepoint(self.x - BALL_RADIUS, self.y):
            self.dx *= -1

        if paddle_rect.collidepoint(self.x + BALL_RADIUS, self.y):
            self.dx *= -1
            