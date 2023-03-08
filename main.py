import pygame
from objects.ball import Ball
from funcs import *
balls_sp = []


def draw_line(pos):
    if pos[1] >= screen_height - 100 or pos == [10000000000, 10000000]:
        return
    k, b = get_k_and_b((x0, y0), pos)
    final = (-b // k, 0)
    pygame.draw.line(screen, pygame.Color("white"), (x0, y0), final, width=1)


def spawn_balls(pos):
    balls_sp.append(Ball((x0, y0), pos, screen, screen_size))


if __name__ == '__main__':
    pygame.init()
    screen_size = screen_width, screen_height = 1000, 1000
    screen = pygame.display.set_mode(screen_size)
    screen.fill(pygame.Color('black'))
    running = True
    clock = pygame.time.Clock()
    pos = [10000000000, 10000000]
    x0 = screen_width // 2
    y0 = screen_height - 100
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN and pos[1] < y0:
                spawn_balls(pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    y0 -= 100
                    y0 -= 100
                    if y0 <= 0:
                        y0 = 0
                        balls_sp.clear()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y0 += 100
                    if y0 >= screen_height:
                        y0 = screen_height
                elif event.key == pygame.K_c:
                    balls_sp.clear()

        clock.tick(600)
        pygame.display.flip()
        screen.fill(pygame.Color('black'))
        pygame.draw.line(screen, pygame.Color('white'), (0, y0), (screen_width, y0), width=3)
        if pos[1] < y0:
            draw_line(pos)
        if balls_sp:
            for ball in balls_sp:
                ball.move(y0)
                ball.render()
    pygame.quit()