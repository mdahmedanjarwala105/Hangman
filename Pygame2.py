import pygame
import math

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

# colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Button Variables

RADIUS = 20
GAP = 15
letters = []
startX = round((width - (RADIUS * 2 + GAP) * 13) / 2)
startY = 400
A = 65

for i in range(26):
    x = startX + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = startY + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Fonts

LETTER_FONT = pygame.font.Font("freesansbold.ttf", 32)

# Load Images

images = []

for i in range(6):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)
    
# Game Variables

hangman_status = 0

# Drawing Function
def draw():
    screen.fill((WHITE))  # Black background
    
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(screen, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            screen.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    
    screen.blit(images[hangman_status], (150, 100))
    
    pygame.display.update()

# Run the Screen and the events performed on the screen
running = True # When I quit the window I want this to be false so that while loop stops running

while running:
    
    clock.tick(FPS)
    # Fill the screen with a color to prevent ghosting
    
    draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # closes the screen
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x_axis, mouse_y_axis = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    distance = math.sqrt((math.pow(x - mouse_x_axis,2)) + (math.pow(y - mouse_y_axis, 2)))
                    if distance < RADIUS:
                        letter[3] = False
            
    
pygame.quit()
