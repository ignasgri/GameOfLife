import pygame
import sys

from colours import dark_blue
# cells= {(c, r): random.choice([True, False]) for c in range(columns) for r in range(rows)}

def draw_grid():
    for x in  range (0, width, cell_size):
        pygame.draw.line(screen, dark_blue, (x, 0), (x, height))
    for y in range (0, height, cell_size):
        pygame.draw.line(screen, dark_blue, (0, y), (width, y))

# def get_cells(population = 100):
#     cells = {(c, r): False for c in range (columns) for r in range (rows)}
#     for i in range (population):
#         col = random.randint(0, columns)
#         row = random.randint(0, rows)
#         cell[col, row] = True
#     return cells

# def get_cells(density=0.2):
#     return {(c,r): random.random() < destiny for c in range (columns) for r in range(rows)}



pygame.init()

colums, rows = 50, 50
cell_size = 10
size = width, height = colums * cell_size, rows * cell_size
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw_grid()

    pygame.display.update()