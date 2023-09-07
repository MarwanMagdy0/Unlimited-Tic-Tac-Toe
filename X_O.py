from utiles import *
last_state = "x"
only_play_on = [None, None]
def func(cell:Button):
    global last_state, only_play_on
    if last_state == "x":
        last_state = "o"
    else:
        last_state = "x"
    grid_by_grid[cell.row][cell.col] = last_state
    only_play_on = [cell.row%3, cell.col%3]

WIDTH  = 1000
HEIGHT = 1000
surface = pygame.display.set_mode((WIDTH, HEIGHT))

grids = [[ Button(surface, row*WIDTH/9, col*HEIGHT/9, WIDTH/9, HEIGHT/9, func, row, col) for col in range(9)] for row in range(9)]
grid_by_grid = [["" for _ in range(9)] for _ in range(9)]
while True:
    pygame.display.update()
    surface.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for row in range(9):
        for col in range(9):
            print((row//3 , only_play_on[0] , col//3 , only_play_on[1]))
            grids[row][col].update(grid_by_grid[row][col])
            if (row//3 == only_play_on[0] and col//3 == only_play_on[1]):
                grids[row][col].disabled = False
            else:
                grids[row][col].disabled = True
            if only_play_on[0] is None:
                grids[row][col].disabled = False
    
    for row in range(0,WIDTH+1,WIDTH//3):
        for col in range(0,HEIGHT+1,HEIGHT//3):
            pygame.draw.line(surface,BORDER_COLOR,(0,col),(WIDTH,col), 5)
            pygame.draw.line(surface,BORDER_COLOR,(row,0),(row,HEIGHT), 5)
