import pygame
from settings import *
from paddle import Paddle
from ball import Ball

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 50)

# Jugadores
left_paddle = Paddle(30, HEIGHT // 2 - 50)
right_paddle = Paddle(WIDTH - 50, HEIGHT // 2 - 50)

# Pelota
ball = Ball()

# Puntajes
left_score = 0
right_score = 0

running = True

while running:
    clock.tick(FPS)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Teclas
    keys = pygame.key.get_pressed()

    # Jugador izquierda
    if keys[pygame.K_w]:
        left_paddle.move(True)

    if keys[pygame.K_s]:
        left_paddle.move(False)

    # Jugador derecha
    if keys[pygame.K_UP]:
        right_paddle.move(True)

    if keys[pygame.K_DOWN]:
        right_paddle.move(False)

    # Movimiento pelota
    ball.move()

    # Colisiones
    ball.collide(left_paddle)
    ball.collide(right_paddle)

    # Punto jugador derecho
    if ball.x < 0:
        right_score += 1
        ball.reset()

    # Punto jugador izquierdo
    if ball.x > WIDTH:
        left_score += 1
        ball.reset()

    # Dibujar
    screen.fill(BLACK)

    left_paddle.draw(screen)
    right_paddle.draw(screen)

    ball.draw(screen)

    # Línea central
    pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)

    # Puntajes
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)

    screen.blit(left_text, (WIDTH // 4, 20))
    screen.blit(right_text, (WIDTH * 3 // 4, 20))

    pygame.display.update()

pygame.quit()