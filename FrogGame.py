import pygame, sys, random
from Frog import Frog
from bus import Bus
from log import Log
from street import Street
from river import River

# Initialize pygame instance variables
pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])

# Create a tuple and set that to the screen dimensions
SCREEN_DIM = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(SCREEN_DIM)

# Set up a caption (goes on the top of the screen)
pygame.display.set_caption("Frog Game!")

# Set up framerate
CLOCK = pygame.time.Clock()
FPS = 60

# set up RGB values for colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (28, 128, 28)
YELLOW = (100, 85, 0)
BROWN = (118, 92, 72)
GRAY = (175, 175, 175)
BLUE = (0, 0, 175)

# create frog object
frog = Frog()

# create streets
streets = []
number_of_buses = 3
street_height = 400
for _ in range(2):
    streets.append(Street(street_height, 'Left', random.randint(1, number_of_buses)))
    streets.append(Street(street_height - 40, 'Right', random.randint(1, number_of_buses)))
    street_height -= 80

# create rivers
rivers = []
number_of_logs = 3
river_height = 200
for _ in range(2):
    rivers.append(River(river_height, 'Left', random.randint(1, number_of_logs)))
    rivers.append(River(river_height - 30, 'Right', random.randint(1, number_of_logs)))
    river_height -= 60

# score variables
high_score = 0
current_best = 0
score = 0

# font and displaying score
FONT = pygame.font.SysFont('Corbel',35)
MENU_BIG = pygame.font.SysFont('Corbel',60)
MENU_MED = pygame.font.SysFont('Corbel',25)
MENU_SMALL = pygame.font.SysFont('Corbel',15)
MENU_IMAGE = pygame.image.load('resources/menu_image.png')

START_MENU = True
END_MENU = False

while True:

    while START_MENU:
        CLOCK.tick(15)
        SCREEN.fill(GREEN)
        name = MENU_BIG.render('FROG ROAD', True, WHITE)
        instructions = MENU_SMALL.render('Press Space To Start', True, WHITE)
        SCREEN.blit(name, (75, 130))
        SCREEN.blit(instructions, (180, 210))
        SCREEN.blit(MENU_IMAGE, (145, 260))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    START_MENU = False

    while END_MENU:
        CLOCK.tick(15)
        SCREEN.fill(GREEN)
        thx = MENU_MED.render('Thanks for Playing!', True, WHITE)
        scores = MENU_MED.render('Your Final Score: %d' % (score + current_best), True, WHITE)
        instructions = MENU_SMALL.render('Press \'Space\' To Play Again', True, WHITE)
        SCREEN.blit(thx, (85, 120))
        SCREEN.blit(scores, (70, 180))
        SCREEN.blit(instructions, (130, 240))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    END_MENU = False
                    current_best = 0
                    score = 0
                    frog.lives = 3

        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                frog.move_up()
            elif event.key == pygame.K_DOWN:
                frog.move_down()
            elif event.key == pygame.K_LEFT:
                frog.move_left()
            elif event.key == pygame.K_RIGHT:
                frog.move_right()
    CLOCK.tick(FPS)
    SCREEN.fill(BLACK)

    if 475 - frog.rect.top > current_best:
        current_best = 475 - frog.rect.top

        # draw the streets and create the buses
    for street in streets:
        SCREEN.fill(GRAY, street.rect)
        for bus in street.buses:
            SCREEN.blit(bus.image, bus.rect)
            SCREEN.fill(YELLOW, bus.rect)
            bus.move()
            if frog.rect.colliderect(bus.rect):
                frog.reset_position()

        # Act on rivers and logs
    frog_on_log = False  # new
    for river in rivers:
        # Draw River
        SCREEN.fill(BLUE, river.rect)

        # Log
        for log in river.logs:
            SCREEN.blit(log.image, log.rect)
            SCREEN.fill(YELLOW, log.rect)
            log.move()
            if frog.rect.colliderect(log.rect):
                frog.move_on_log(log)
                frog_on_log = True  # new

        # Collided with River and not a Log - new
        if not frog_on_log and frog.rect.colliderect(river.rect):
            frog.reset_position()

     # updates current best
    if 475 - frog.rect.top > current_best:
        current_best = 475 - frog.rect.top

    # updates high score
    if score + current_best >= high_score:
        high_score = score + current_best

    # resets frog and updates score
    if frog.rect.top <= 60:
        frog.reset_position()
        frog.lives += 1
        score += 1000 + current_best
        current_best = 0

    if frog.lives < 1:
        END_MENU = True

    score_text = FONT.render("Score: " + str(score + current_best), True, WHITE)
    high_score_text = FONT.render("High Score: " + str(high_score), True, WHITE)
    lives_text = FONT.render("Lives: " + str(frog.lives), True, WHITE)

    SCREEN.blit(score_text, (5, 0))
    SCREEN.blit(high_score_text, (5, 20))
    SCREEN.blit(lives_text, (5, 40))

    SCREEN.blit(frog.image, frog.rect)
    SCREEN.fill(GRAY, frog.rect)


    pygame.display.flip()
