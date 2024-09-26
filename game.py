# Hello World Comment
import pygame

# Initialize Pygame
pygame.init()
# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pixel Game")

# Set up colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)

# Define the character (pixel art style)
character_size = 50  # Make the "pixel" size bigger for a pixelated feel
character_x = SCREEN_WIDTH // 2
character_y = SCREEN_HEIGHT // 2

# Game loop
'''running = True
while running:
    screen.fill(WHITE)  # Fill background with white

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw character (a simple green square as placeholder)
    pygame.draw.rect(screen, GREEN, (character_x, character_y, character_size, character_size))
    
    # Update display
    pygame.display.flip()

# Quit the game
pygame.quit()'''
speed = 5

# Game loop
running = True
while running:
    screen.fill(WHITE)  # Fill background with white

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move the character with arrow keys
    if keys[pygame.K_LEFT]:
        character_x -= speed
    if keys[pygame.K_RIGHT]:
        character_x += speed
    if keys[pygame.K_UP]:
        character_y -= speed
    if keys[pygame.K_DOWN]:
        character_y += speed

    # Draw character
    pygame.draw.rect(screen, GREEN, (character_x, character_y, character_size, character_size))
    
    # Update display
    pygame.display.flip()

pygame.quit()
'''
# Load sprite
character_sprite = pygame.image.load("character.png")
character_sprite = pygame.transform.scale(character_sprite, (character_size, character_size))  # Resize for pixel art

# Inside the game loop, replace this:
screen.blit(character_sprite, (character_x, character_y))  # Draw the character sprite'''