import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Object")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Game variables
basket_width = 100
basket_height = 20
basket_x = (WIDTH - basket_width) // 2
basket_y = HEIGHT - basket_height - 10
basket_speed = 10

object_width = 20
object_height = 20
object_x = random.randint(0, WIDTH - object_width)
object_y = -object_height
object_speed = 5

score = 0
font = pygame.font.Font(None, 36)

# Game loop control variables
running = True

# Main game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Update falling object position
    object_y += object_speed

    # Check for collision with the basket
    if (basket_y < object_y + object_height and 
        basket_y + basket_height > object_y and 
        basket_x < object_x + object_width and 
        basket_x + basket_width > object_x):
        score += 1
        object_y = -object_height  # Reset the object to fall again
        object_x = random.randint(0, WIDTH - object_width)

    # Reset the falling object if it goes off screen without being caught
    if object_y > HEIGHT:
        object_y = -object_height
        object_x = random.randint(0, WIDTH - object_width)

    # Drawing everything on the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (basket_x, basket_y, basket_width, basket_height))  # Draw the basket
    pygame.draw.rect(screen, RED, (object_x, object_y, object_width, object_height))      # Draw the falling object

    # Display score
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Frame rate control
    pygame.time.Clock().tick(30)

# Quit Pygame when done
pygame.quit()
