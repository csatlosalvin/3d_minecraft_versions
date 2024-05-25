import os

# Világ paraméterek
WIDTH, HEIGHT = 20, 10
EMPTY = '.'
BLOCK = '#'
STEVE = 'S'

# Világ inicializálása
world = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Steve kezdő pozíciója
steve_x, steve_y = WIDTH // 2, HEIGHT // 2
world[steve_y][steve_x] = STEVE

def print_world():
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in world:
        print(''.join(row))
    print("\nUse WASD to move, P to place a block, R to remove a block, Q to quit.")

def move_steve(dx, dy):
    global steve_x, steve_y
    new_x, new_y = steve_x + dx, steve_y + dy
    if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT:
        if world[new_y][new_x] == EMPTY:
            world[steve_y][steve_x] = EMPTY
            steve_x, steve_y = new_x, new_y
            world[steve_y][steve_x] = STEVE

def place_block():
    if 0 <= steve_x < WIDTH and 0 <= steve_y < HEIGHT:
        world[steve_y][steve_x] = BLOCK

def remove_block():
    if 0 <= steve_x < WIDTH and 0 <= steve_y < HEIGHT:
        if world[steve_y][steve_x] == BLOCK:
            world[steve_y][steve_x] = EMPTY

while True:
    print_world()
    command = input("Enter command: ").strip().lower()
    if command == 'w':
        move_steve(0, -1)
    elif command == 'a':
        move_steve(-1, 0)
    elif command == 's':
        move_steve(0, 1)
    elif command == 'd':
        move_steve(1, 0)
    elif command == 'p':
        place_block()
    elif command == 'r':
        remove_block()
    elif command == 'q':
        break
