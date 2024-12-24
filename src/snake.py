class Snake:
    def __init__(self, cell_size):
        self.body = [(100, 100), (80, 100), (60, 100)]  # Initial snake segments
        self.direction = "RIGHT"  # Initial direction
        self.cell_size = cell_size

    def move(self):
        x, y = self.body[0]  # Get the head position
        if self.direction == "UP":
            y -= self.cell_size
        elif self.direction == "DOWN":
            y += self.cell_size
        elif self.direction == "LEFT":
            x -= self.cell_size
        elif self.direction == "RIGHT":
            x += self.cell_size
        new_head = (x, y)
        self.body.insert(0, new_head)  # Add new head
        return new_head

    def grow(self):
        # The snake grows naturally by keeping the tail after eating food
        pass

    def shrink(self):
        self.body.pop()  # Remove the tail to maintain length

    def set_direction(self, direction):
        # Prevent the snake from turning back on itself
        opposites = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if direction != opposites.get(self.direction):
            self.direction = direction

    def check_collision(self, head_position, width, height):
        # Check if the snake hits walls or itself
        x, y = head_position
        return (
            x < 0 or x >= width or
            y < 0 or y >= height or
            head_position in self.body[1:]  # Head collides with the body
        )
