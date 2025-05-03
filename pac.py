import pygame
import heapq
import time

TILE_SIZE = 60
GRID_WIDTH = 5
GRID_HEIGHT = 5
SCREEN_WIDTH = GRID_WIDTH * TILE_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * TILE_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GRAY = (100, 100, 100)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man A* Pathfinding")

grid = [
    [' ', ' ', ' ', '%', ' '],
    [' ', '%', ' ', '%', ' '],
    [' ', '%', ' ', ' ', ' '],
    [' ', '%', ' ', '%', ' '],
    ['%', '%', ' ', ' ', 'F']
]

start = (0, 0)
goal = (4, 4)

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for dx, dy in DIRECTIONS:
            neighbor = (current[0] + dx, current[1] + dy)

            if neighbor in g_score:
                continue

            if 0 <= neighbor[0] < GRID_HEIGHT and 0 <= neighbor[1] < GRID_WIDTH and grid[neighbor[0]][neighbor[1]] != '%':
                g_score[neighbor] = g_score[current] + 1
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
                came_from[neighbor] = current

    return []


def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    return path[::-1]


def draw_grid():
    screen.fill(WHITE)
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            x, y = col * TILE_SIZE, row * TILE_SIZE
            if grid[row][col] == '%':
                pygame.draw.rect(screen, GRAY, (x, y, TILE_SIZE, TILE_SIZE))
            elif (row, col) == goal:
                pygame.draw.circle(screen, RED, (x + TILE_SIZE // 2, y + TILE_SIZE // 2), TILE_SIZE // 3)
            pygame.draw.rect(screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 1)


def move_pacman(path):
    for pos in path:
        draw_grid()
        x, y = pos[1] * TILE_SIZE, pos[0] * TILE_SIZE
        pygame.draw.circle(screen, YELLOW, (x + TILE_SIZE // 2, y + TILE_SIZE // 2), TILE_SIZE // 3)
        pygame.display.update()
        time.sleep(0.5)


path = a_star(grid, start, goal)

running = True
while running:
    draw_grid()
    pygame.display.update()

    if path:
        move_pacman(path)
        path = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
