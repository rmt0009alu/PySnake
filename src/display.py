import pygame

class Display:
    def __init__(self, width, height, cell_size):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake Game")
        self.cell_size = cell_size

        # Load images
        self.snake_image = pygame.image.load("./img/snake_body.png").convert_alpha()
        self.food_image = pygame.image.load("./img/food.png").convert_alpha()

        # Scale images to cell size
        self.snake_image = pygame.transform.scale(self.snake_image, (cell_size, cell_size))
        self.food_image = pygame.transform.scale(self.food_image, (cell_size, cell_size))

        self.font = pygame.font.SysFont("Arial", 24)

    def draw_background(self, color):
        self.screen.fill(color)

    def draw_snake(self, snake_body):
        for segment in snake_body:
            self.screen.blit(self.snake_image, segment)

    def draw_food(self, food_position):
        self.screen.blit(self.food_image, food_position)

    def display_text(self, text, position, color):
        rendered_text = self.font.render(text, True, color)
        self.screen.blit(rendered_text, position)

    def update(self):
        pygame.display.flip()
