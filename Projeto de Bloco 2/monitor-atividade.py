import pygame
import psutil
from collections import namedtuple

# Game init
pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 24)

# Coordinates
Coordinate = namedtuple('Coordinate', ['x', 'y'])

# Configs
screenSize = Coordinate(x=800, y=600)
screen = pygame.display.set_mode(screenSize)

# Change title
pygame.display.set_caption('Monitor de Atividades')

# Colors
background = (232,232,232)
backgroundContrast = (196,182,182)
darkBlue = (48,71,94)
white = (255,255,255)
black = (0,0,0)
darkGrey = (34,40,49)
red = (240,84,84)
colors = [background, black, darkBlue, darkGrey, white]

def memory_usage():
    memory = psutil.virtual_memory()
    memory_total = round(psutil.virtual_memory().total/(1024*1024*1024), 2)

    width = screen.get_width() - 2 * 20
    percentage_used = width * memory.percent/100

    pygame.draw.rect(screen, backgroundContrast, (20, 50, width, 70))
    pygame.draw.rect(screen, darkBlue, (20, 50, percentage_used, 70))
    text = font.render(f"Uso de memória (total: {str(memory_total)}GB): {memory.percent}%", 1, darkBlue)
    screen.blit(text, (20, 30))

def cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)

    width = screen.get_width() - 2 * 20
    percentage_used = width * cpu_percent/100

    pygame.draw.rect(screen, backgroundContrast, (20, 170, width, 70))
    pygame.draw.rect(screen, darkGrey, (20, 170, percentage_used, 70))
    text = font.render(f"Uso de CPU: {cpu_percent}%", 1, darkGrey)
    screen.blit(text, (20, 150))

def disk_usage():
    hard_drive = psutil.disk_usage('.')
    hard_drive_percent = hard_drive.percent

    width = screen.get_width() - 2 * 20
    percentage_used = width * hard_drive_percent/100

    pygame.draw.rect(screen, backgroundContrast, (20, 290, width, 70))
    pygame.draw.rect(screen, darkBlue, (20, 290, percentage_used, 70))
    text = font.render(f"Uso de Disco: {hard_drive_percent}%", 1, darkBlue)
    screen.blit(text, (20, 270))

# Game loop
running = True
clock = pygame.time.Clock()
counter = 0

while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if counter == 60:
        # paint the screen
        screen.fill(background)
        memory_usage()
        cpu_usage()
        disk_usage()
        counter = 0

    # Update the display
    pygame.display.update()

    # Update the display
    clock.tick(150)
    counter += 1

pygame.display.quit()
