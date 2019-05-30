#!/usr/bin/env python3
import sys, os
import pygame

# Initialize pygame
pygame.init()

# Set window width and height based on display size
width = int((pygame.display.Info().current_w)/2)
height = int((pygame.display.Info().current_h)/2)
size = width, height

# Set speed of bouncing ball--how far the ball should move in each frame
speed = [2, 2]

# Define black with RBG settings of 0, 0, 0
black = 0, 0, 0  

# Create a screen, setting size from above.
screen = pygame.display.set_mode(size)

# Set path to assets folder and load the ball.gif file
assets = os.path.join(os.pardir, "assets")
ball = pygame.image.load(os.path.join(assets, "ball.gif"))

# Get size of the rectangle enclosing the ball.
ballrect = ball.get_rect()

# Start an infinite while loop.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
            
    # Move the ballrect the distance indicated by speed. 
    ballrect = ballrect.move(speed)

    # Handle running into edges of screen
    if ballrect.left < 0 or ballrect.right > width: # Ball hits a left/right side 
        speed[0] = -speed[0] # Change left/right motion to oposit direction
    if ballrect.top < 0 or ballrect.bottom > height: # Ball hits a top/bottom side
        speed[1] = -speed[1] # Change up/down motion to oposite direction

    # Erase the screen by filling with black (defined above as 0, 0, 0)
    screen.fill(black)

    # Blit the new ball position to the screen
    screen.blit(ball, ballrect)

    # Flip the screen with the new ball position.
    pygame.display.flip()

pygame.quit()