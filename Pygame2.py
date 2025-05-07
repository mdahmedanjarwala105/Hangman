import pygame
import math
import random

# import nltk --> this needs to be import so that we can download all the words in nltk
from nltk.corpus import words

# Download the words dataset if not already done
# nltk.download('words') --> we are downloading all the words which are there in dictionary

# Get all the words from the NLTK words corpus
all_words = words.words()

# Initialize an empty list to store filtered words
WORDS = []

# Iterate through each word in the all_words list
for word in all_words:
    # Check if the length of the word is between 3 and 7
    if len(word) >= 3 and len(word) <= 7:
        # Convert the word to uppercase and Append the uppercase word to the filtered_words list
        WORDS.append(word.upper())

# Initialize Pygame
pygame.init()

# Create the Game Screen

width, height = 800, 600
screen = pygame.display.set_mode((width, height))  # Creates Screen

# Create Title and Icon
pygame.display.set_caption("Hangman")
icon = pygame.image.load("man.png")  # Loads image
pygame.display.set_icon(icon)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Button Variables
RADIUS = 20
GAP = 15
startX = round((width - (RADIUS * 2 + GAP) * 13) / 2)
startY = 400
A = 65

# Play Button Variables
BIG_RADIUS = 50
BIG_X_Axis = width // 2
BIG_Y_Axis = 320

# Fonts
LETTER_FONT = pygame.font.Font("freesansbold.ttf", 32)
WORD_FONT = pygame.font.Font("freesansbold.ttf", 52)
TITLE_FONT = pygame.font.Font("freesansbold.ttf", 62)

# Load Hangman Images
images = []

for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)


# Function to draw the menu screen
def drawBig():
    screen.fill((WHITE))  # WHITE background
    text = TITLE_FONT.render("HangMan Game", 1, BLACK)
    screen.blit(text, (width / 2 - text.get_width() / 2, 20))
    pygame.draw.circle(screen, BLACK, (BIG_X_Axis, BIG_Y_Axis), BIG_RADIUS, 3)
    text = LETTER_FONT.render("PLAY", 1, BLACK)
    screen.blit(
        text, (BIG_X_Axis - text.get_width() / 2, BIG_Y_Axis - text.get_height() / 2)
    )
    pygame.display.update()


# Function to draw the game screen
def draw():
    screen.fill((WHITE))  # WHITE background
    text = TITLE_FONT.render("HangMan Game", 1, BLACK)
    screen.blit(text, (width / 2 - text.get_width() / 2, 20))

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
            screen.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    if hangman_status < len(images):
        screen.blit(images[hangman_status], (50, 100))

    pygame.display.update()


# Function to display a message when the game is won or lost
def display_message(message):
    pygame.time.delay(500)
    screen.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    screen.blit(
        text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2)
    )
    pygame.display.update()
    pygame.time.delay(3000)


# Main game function
def main():
    global hangman_status, guessed, words, letters, multiple_word
    hangman_status = 0
    guessed = []
    words = random.choice(WORDS)

    # Buttons and It's visibility
    letters = []
    for i in range(26):
        x = startX + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
        y = startY + ((i // 13) * (GAP + RADIUS * 2))
        letters.append([x, y, chr(A + i), True])

    FPS = 60
    clock = pygame.time.Clock()
    # Run the Screen and the events performed on the screen
    running = True  # When I quit the window I want this to be false so that while loop stops running

    while running:

        clock.tick(FPS)
        # Fill the screen with a color to prevent ghosting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # closes the screen
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x_axis, mouse_y_axis = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        distance = math.sqrt(
                            (math.pow(x - mouse_x_axis, 2))
                            + (math.pow(y - mouse_y_axis, 2))
                        )
                        if distance < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in words:
                                hangman_status += 1
                                if hangman_status == 6:
                                    draw()
                                    pygame.time.delay(
                                        500
                                    )  # Delay to display the final image
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


# Menu function to display the start screen
def menu():
    FPS = 60
    clock = pygame.time.Clock()
    # Run the Screen and the events performed on the screen
    running = True  # When I quit the window I want this to be false so that while loop stops running

    while running:

        clock.tick(FPS)
        # Fill the screen with a color to prevent ghosting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # closes the screen
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x_axis, mouse_y_axis = pygame.mouse.get_pos()
                distance = math.sqrt(
                    (math.pow(BIG_X_Axis - mouse_x_axis, 2))
                    + (math.pow(BIG_Y_Axis - mouse_y_axis, 2))
                )
                if distance < BIG_RADIUS:
                    main()

        drawBig()  # Draw the menu screen


menu()  # Call the menu function to start the game
