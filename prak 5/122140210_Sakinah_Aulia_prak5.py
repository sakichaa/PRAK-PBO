import pygame
import sys
import random

# Inisialisasi Pygame
pygame.init()

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Konstanta-konstanta
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

# Membuat kelas untuk ular
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        self.grow = False

    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= CELL_SIZE
        elif self.direction == "DOWN":
            y += CELL_SIZE
        elif self.direction == "LEFT":
            x -= CELL_SIZE
        elif self.direction == "RIGHT":
            x += CELL_SIZE
        self.body.insert(0, (x, y))
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def grow_snake(self):
        self.grow = True

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

# Membuat kelas untuk makanan
class Food:
    def __init__(self):
        self.position = self.randomize_position()

    def randomize_position(self):
        x = random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE
        y = random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE
        return x, y

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

# Membuat kelas game
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != "DOWN":
                        self.snake.direction = "UP"
                    elif event.key == pygame.K_DOWN and self.snake.direction != "UP":
                        self.snake.direction = "DOWN"
                    elif event.key == pygame.K_LEFT and self.snake.direction != "RIGHT":
                        self.snake.direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and self.snake.direction != "LEFT":
                        self.snake.direction = "RIGHT"

            # Periksa tabrakan dengan makanan
            if self.snake.body[0] == self.food.position:
                self.snake.grow_snake()
                self.food.position = self.food.randomize_position()

            # Periksa tabrakan dengan dinding
            if (
                self.snake.body[0][0] < 0 or self.snake.body[0][0] >= WIDTH or
                self.snake.body[0][1] < 0 or self.snake.body[0][1] >= HEIGHT
            ):
                running = False

            # Periksa tabrakan dengan tubuh ular sendiri
            if self.snake.body[0] in self.snake.body[1:]:
                running = False

            # Gerakkan dan gambar ular
            self.snake.move()
            self.screen.fill(WHITE)
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            pygame.display.flip()

        pygame.quit()
        sys.exit()

# Main function
def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
