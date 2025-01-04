import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Create the Game Screen

width, height = 800, 600
screen = pygame.display.set_mode((width, height)) # Creates Screen

pygame.display.set_caption("Hangman")
# icon = pygame.image.load("SpaceInvader.png") # Loads image
# pygame.display.set_icon(icon)

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
    
BIG_RADIUS = 50
BIG_X_Axis = width // 2
BIG_Y_Axis = 320


# Fonts

LETTER_FONT = pygame.font.Font("freesansbold.ttf", 32)
WORD_FONT = pygame.font.Font("freesansbold.ttf", 52)
TITLE_FONT = pygame.font.Font("freesansbold.ttf", 62)

# Load Images

images = []

for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)
    
# Game Variables

hangman_status = 0
multiple_word = ["MUTLI", "TASK", "NICE", "HELLO"]
words = random.choice(multiple_word)
guessed = []

def drawBig():
    screen.fill((WHITE))  # WHITE background
    text = TITLE_FONT.render("HangMan Game", 1, BLACK)
    screen.blit(text, (width/2 - text.get_width()/2, 20))
    pygame.draw.circle(screen, BLACK, (BIG_X_Axis, BIG_Y_Axis), BIG_RADIUS, 3)
    text = LETTER_FONT.render("PLAY", 1, BLACK)
    screen.blit(text, (BIG_X_Axis - text.get_width()/2, BIG_Y_Axis - text.get_height()/2))
    pygame.display.update()
    

# Drawing Function
def draw():
    screen.fill((WHITE))  # WHITE background
    text = TITLE_FONT.render("HangMan Game", 1, BLACK)
    screen.blit(text, (width/2 - text.get_width()/2, 20))
    
    display_word = ""
    for letter in words:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    screen.blit(text, (250, 200))
    
    
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(screen, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            screen.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    
    if hangman_status < len(images):
        screen.blit(images[hangman_status], (50, 100))
    
    pygame.display.update()
    
    
def display_message(message):
    pygame.time.delay(500)
    screen.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    screen.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
    

def main():
    global hangman_status, guessed, words, letters
    hangman_status = 0
    guessed = []
    words = random.choice(multiple_word)
    
    # Reset buttons visibility
    letters = []
    for i in range(26):
        x = startX + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
        y = startY + ((i // 13) * (GAP + RADIUS * 2))
        letters.append([x, y, chr(A + i), True])
    
    FPS = 60
    clock = pygame.time.Clock()
    # Run the Screen and the events performed on the screen
    running = True # When I quit the window I want this to be false so that while loop stops running

    while running:
        
        clock.tick(FPS)
        # Fill the screen with a color to prevent ghosting
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
                            guessed.append(ltr)
                            if ltr not in words:
                                hangman_status += 1
                                if hangman_status == 6:
                                    draw()
                                    pygame.time.delay(500)  # Delay to display the final image
                                    display_message("You Lost")
                                    return
        
        draw()
                                
        won = True
        for letter in words:
            if letter not in guessed:
                won = False
                break
        
        if won:
            display_message("You Won")
            return
            

def menu():
    FPS = 60
    clock = pygame.time.Clock()
    # Run the Screen and the events performed on the screen
    running = True # When I quit the window I want this to be false so that while loop stops running

    while running:
        
        clock.tick(FPS)
        # Fill the screen with a color to prevent ghosting
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # closes the screen
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x_axis, mouse_y_axis = pygame.mouse.get_pos()
                distance = math.sqrt((math.pow(BIG_X_Axis - mouse_x_axis,2)) + (math.pow(BIG_Y_Axis - mouse_y_axis, 2)))
                if distance < BIG_RADIUS:
                    main()
                    
        drawBig()
        
menu()  # Call the menu function to start the game