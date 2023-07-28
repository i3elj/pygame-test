import pygame
from ball import Ball
from config import HEIGHT, WIDTH


def main():
    pygame.init()
    screen = pygame.display.set_mode((HEIGHT, WIDTH))
    clock = pygame.time.Clock()
    running = True

    ball = Ball()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        ball.pos.y -= 1

        screen.fill("black")

        mouse_pos = pygame.mouse.get_pos()
        ball.draw(screen)
        ball.update(mouse_pos[0], mouse_pos[1])

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
