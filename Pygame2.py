import pygame

# Initialize Pygame
pygame.init()

# Create the Game Screen

width, height = 800, 600
screen = pygame.display.set_mode((width, height)) # Creates Screen

pygame.display.set_caption("Hangman")
# icon = pygame.image.load("SpaceInvader.png") # Loads image
# pygame.display.set_icon(icon)

FPS = 60
clock = pygame.time.Clock()

# Load Images

images = []

for i in range(6):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)
    
# Game Variables

hangman_status = 0

# Run the Screen and the events performed on the screen
running = True # When I quit the window I want this to be false so that while loop stops running

while running:
    
    clock.tick(FPS)
    # Fill the screen with a color to prevent ghosting
    screen.fill((0, 255, 0))  # Black background
    
    screen.blit(images[hangman_status], (150, 100))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # closes the screen
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            
    pygame.display.update()
pygame.quit()
