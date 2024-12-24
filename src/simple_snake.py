import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Setup the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Snake and Food Initialization
snake = [(100, 100), (80, 100), (60, 100)]  # Snake body parts as (x, y)
direction = "RIGHT"  # Initial movement direction
food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
        random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)

# Game Variables
running = True
speed = 10

# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Control the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Move the snake
    x, y = snake[0]  # Head of the snake
    if direction == "UP":
        y -= CELL_SIZE
    elif direction == "DOWN":
        y += CELL_SIZE
    elif direction == "LEFT":
        x -= CELL_SIZE
    elif direction == "RIGHT":
        x += CELL_SIZE
    new_head = (x, y)

    # Check collisions
    if (
        x < 0 or x >= WIDTH or
        y < 0 or y >= HEIGHT or
        new_head in snake
    ):
        running = False  # Game over

    # Add new head and check food collision
    snake.insert(0, new_head)
    if new_head == food:
        food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
    else:
        snake.pop()  # Remove the tail if no food eaten

    # Draw everything
    screen.fill(BLACK)  # Background color
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))  # Food
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))  # Snake

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
