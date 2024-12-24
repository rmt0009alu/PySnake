import pygame
import random
from snake import Snake
from display import Display

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    speed = 10

    # Initialize Snake and Display
    snake = Snake(CELL_SIZE)
    display = Display(WIDTH, HEIGHT, CELL_SIZE)

    # Initial food position
    food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
            random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)

    # Game variables
    running = True
    score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.set_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.set_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.set_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.set_direction("RIGHT")

        # Move the snake
        new_head = snake.move()

        # Check collisions
        if snake.check_collision(new_head, WIDTH, HEIGHT):
            running = False

        # Check food collision
        if new_head == food:
            score += 1
            food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                    random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
        else:
            snake.shrink()  # Only shrink if no food eaten

        # Draw everything
        display.draw_background(BLACK)
        display.draw_snake(snake.body)
        display.draw_food(food)
        display.display_text(f"Score: {score}", (10, 10), WHITE)
        display.update()

        clock.tick(speed)

    pygame.quit()

if __name__ == "__main__":
    main()
