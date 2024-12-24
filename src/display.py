import pygame

class Display:
    def __init__(self, width, height, cell_size):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Snake Game")
        self.cell_size = cell_size
        self.font = pygame.font.SysFont("Arial", 24)

    def draw_background(self, color):
        self.screen.fill(color)

    def draw_snake(self, snake_body, color):
        for segment in snake_body:
            pygame.draw.rect(self.screen, color, (*segment, self.cell_size, self.cell_size))

    def draw_food(self, food_position, color):
        pygame.draw.rect(self.screen, color, (*food_position, self.cell_size, self.cell_size))

    def display_text(self, text, position, color):
        rendered_text = self.font.render(text, True, color)
        self.screen.blit(rendered_text, position)

    def update(self):
        pygame.display.flip()
