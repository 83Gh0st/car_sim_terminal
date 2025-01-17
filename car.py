import pygame
import random
import time

# Constants
WIDTH = 400
HEIGHT = 600
CAR_WIDTH = 30
CAR_HEIGHT = 40
FPS = 60
CAR_SPEED = 10
OBSTACLE_SPEED = 5
ITEM_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHT_GRAY = (211, 211, 211)

# Initialize pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Fonts
font = pygame.font.SysFont("Arial", 36)
small_font = pygame.font.SysFont("Arial", 24)

# Game state
car_x = WIDTH // 2 - CAR_WIDTH // 2
car_y = HEIGHT - CAR_HEIGHT - 10
score = 0
game_over = False
obstacles = []
items = []

def draw_car(x, y):
    """Draw the car."""
    pygame.draw.rect(screen, BLUE, (x, y, CAR_WIDTH, CAR_HEIGHT), border_radius=5)

def draw_obstacles(obstacles):
    """Draw obstacles."""
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle, border_radius=5)

def draw_items(items):
    """Draw items."""
    for item in items:
        pygame.draw.circle(screen, YELLOW, (item[0], item[1]), 10)

def draw_score(score):
    """Display the score."""
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def draw_game_over():
    """Display the Game Over screen."""
    game_over_text = font.render("GAME OVER", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))

    restart_text = small_font.render("Press 'R' to Restart or 'Q' to Quit", True, WHITE)
    screen.blit(restart_text, (WIDTH // 2 - 150, HEIGHT // 2 + 10))

def update_obstacles():
    """Update the obstacles and handle collisions."""
    global game_over, obstacles
    for obstacle in obstacles:
        obstacle.y += OBSTACLE_SPEED  # Update the y position of each obstacle
    obstacles[:] = [obstacle for obstacle in obstacles if obstacle.y < HEIGHT]  # Remove off-screen obstacles

    # Collision detection
    for obstacle in obstacles:
        if obstacle.colliderect(pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT)):
            game_over = True

def update_items():
    """Update items and handle collection."""
    global score, items
    for item in items:
        item[1] += ITEM_SPEED  # Update the y position of each item
    items[:] = [item for item in items if item[1] < HEIGHT]  # Remove off-screen items

    # Collect items
    for item in items:
        if car_x < item[0] + 10 and car_x + CAR_WIDTH > item[0] and car_y < item[1] + 10 and car_y + CAR_HEIGHT > item[1]:
            score += 10
            items.remove(item)

def handle_input():
    """Handle user input."""
    global car_x
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= CAR_SPEED
    if keys[pygame.K_RIGHT] and car_x < WIDTH - CAR_WIDTH:
        car_x += CAR_SPEED

def main():
    """Main game loop."""
    global score, game_over, car_x, car_y, obstacles, items

    clock = pygame.time.Clock()
    while True:
        screen.fill(LIGHT_GRAY)  # Fill the screen with a light gray background

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        if not game_over:
            handle_input()

            # Update game state
            update_obstacles()
            update_items()

            # Add new obstacles and items
            if random.randint(0, 10) < 2:
                obstacle_x = random.randint(0, WIDTH - CAR_WIDTH)
                obstacles.append(pygame.Rect(obstacle_x, 0, CAR_WIDTH, CAR_HEIGHT))  # Use pygame.Rect for obstacles

            if random.randint(0, 20) == 0:
                item_x = random.randint(0, WIDTH - 20)
                items.append([item_x, 0])

            # Draw everything
            draw_car(car_x, car_y)
            draw_obstacles(obstacles)
            draw_items(items)
            draw_score(score)
        else:
            draw_game_over()

        pygame.display.update()
        clock.tick(FPS)

        # Handle key input after game over
        if game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                # Restart the game
                game_over = False
                score = 0
                car_x = WIDTH // 2 - CAR_WIDTH // 2
                obstacles = []
                items = []
            elif keys[pygame.K_q]:
                pygame.quit()
                return

if __name__ == "__main__":
    main()
