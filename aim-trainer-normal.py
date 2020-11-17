import random
import pygame
from pygame import mixer
import keyboard
import math


# Defining Screen and Screen Variables and Initializing
pygame.init()

width = 1600
height = 840
display = pygame.display.set_mode((width, height))  # Screen/Window


# Colors
black = (0, 0, 0)
white = (255, 255, 255)
purple = (128, 0, 128)
grey = (128, 128, 128)
sky = (0, 0, 220)
blue = (85, 206, 255)
orange = (255, 127, 80)
red = (200, 0, 0)
light_red = (255, 0, 0)
green = (0, 200, 0)
light_green = (0, 255, 0)
colors = [white, purple, grey, blue, sky, orange, red, green]


# Sounds and bg music
bg = mixer.Sound('aim trainer assets/normal-bg.mp3')  # load the bg music
bg.play(0)  # play the music once
shot = mixer.Sound('aim trainer assets/normal-shot.mp3')


# Globals
font = pygame.font.SysFont('malgungothic', int(width/28))  # The score text font
end_font = pygame.font.SysFont('sylfaen', int(width/20))

clock = pygame.time.Clock()  # To set the frame rate
max_time = 60  # timer in seconds for the game
show_seconds = True

score = 0
show_score = True

loop_count = 0


# Main Game Loop
# Show the first circle
cx = random.randint(20, width - 14)
cy = random.randint(120, height - 14)
width_of_circle = random.randint(7, 14)
pygame.draw.circle(display, random.choice(colors), (cx, cy), width_of_circle)

start_ticks = pygame.time.get_ticks()  # Timer start
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if keyboard.is_pressed('q'):
        pygame.quit()
        quit()

    # Timer
    seconds = round((pygame.time.get_ticks() - start_ticks) / 1000, 1)  # calculate how many seconds
    if seconds >= max_time:
        show_seconds = False  # Make sure that the timer and the score do not show up on the screen anymore
        show_score = False

        end_score = end_font.render(f'You hit {round(score / 5)} targets! Nice!', True, green)
        display.fill(black)
        display.blit(end_score, (int(width / 4), (height / 2 - 50)))  # Show the score in the middle of the screen

        loop_count += 1
        if loop_count >= 900:  # if loop goes 14 times
            pygame.quit()
            quit()


    # Score
    score_text = font.render(f'{score}', True, blue)  # Rendering the font but not putting it onto the screen yet
    timer = font.render(f'{seconds}', True, red)
    if show_score:
        display.blit(score_text, (width-100,30))  # Now putting it onto the screen at the top right
    if show_seconds:
        pygame.draw.rect(display, black, (50, 30, int(width/32)+65, int(width/32)+20))  # Rectangle over the timer to prevent clumping of the numbers
        display.blit(timer, (50, 30))


    # Checking if circle has been clicked on
    # Mouse position
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]

    # Square the pos'
    sqx = (x - cx)**2
    sqy = (y - cy)**2

    # get what button on the mouse was clicked
    click = pygame.mouse.get_pressed()

    # If the circle has been clicked on
    if math.sqrt(sqx + sqy) < width_of_circle and click[0] == 1:  # click[0] is 1st mouse button (left click)
        shot.play(0)
        score += 5  # Add 5 to the score
        display.fill(black)  # Redraw the screen
        # Redraw the circle
        cx = random.randint(20, width - 14)
        cy = random.randint(120, height - 14)
        width_of_circle = random.randint(7, 14)
        pygame.draw.circle(display, random.choice(colors), (cx, cy), width_of_circle)


    pygame.display.update()
    clock.tick()  # setting the frame rate (default is 60)
