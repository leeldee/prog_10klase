# Import the necessary libraries
import pygame

# Initialize the game
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))

# Set the title and icon
pygame.display.set_caption("Blue Rectangle Jumper")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Set up the blue rectangle
blue_rectangle = pygame.Rect(100, 450, 50, 50)

# Set up the green rectangles
green_rectangles = []
for i in range(5):
    green_rectangles.append(pygame.Rect(i * 200, 500, 50, 50))

# Set up the background
background = pygame.image.load('background.png')

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game state
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and blue_rectangle.bottom == 450:
        blue_rectangle.y -= 100

    # Check for collisions
    for green_rectangle in green_rectangles:
        if blue_rectangle.colliderect(green_rectangle):
            running = False

    # Draw the game
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (0, 0, 255), blue_rectangle)
    for green_rectangle in green_rectangles:
        pygame.draw.rect(screen, (0, 255, 0), green_rectangle)
    pygame.display.update()

# Clean up before exiting
pygame.quit()