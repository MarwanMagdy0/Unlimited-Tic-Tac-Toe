from utiles import *
last_state = "x"
only_play_on = [None, None]
def func(cell:Button):
    global last_state, only_play_on
    if grid_by_grid[cell.row][cell.col] !="":
        return
    if last_state == "x":
        last_state = "o"
    else:
        last_state = "x"
    grid_by_grid[cell.row][cell.col] = last_state
    only_play_on = [cell.row%3, cell.col%3]

WIDTH  = 1000
HEIGHT = 1000
surface = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Unlimited Tic Tac Toe")
grids = [[ Button(surface, row*WIDTH/9, col*HEIGHT/9, WIDTH/9, HEIGHT/9, func, row, col) for col in range(9)] for row in range(9)]
grid_by_grid = [["" for _ in range(9)] for _ in range(9)]
bigger_grid = [["" for _ in range(3)] for _ in range(3)]
bigger_grid_buttons = [[Button(surface, row*WIDTH/3, col*HEIGHT/3, WIDTH/3, HEIGHT/3, func, row, col, 150) for col in range(3)] for row in range(3)]
while True:
    clock.tick(60)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    whole_game_state = get_game_state(bigger_grid)
    if whole_game_state =="":
        surface.fill((255,255,255))
    else:
        pygame.display.set_caption(f"{whole_game_state} wines the game")
        continue
    empty_cells = 0
    for row in range(9):
        for col in range(9):
            if (row//3 == only_play_on[0] and col//3 == only_play_on[1]) and bigger_grid[row//3][col//3]=="":
                grids[row][col].disabled = False
                if grid_by_grid[row][col] =="":
                    empty_cells +=1
            else:
                grids[row][col].disabled = True

            if only_play_on[0] is None:
                grids[row][col].disabled = False
                if grid_by_grid[row][col] =="":
                    empty_cells +=1

            if bigger_grid[row//3][col//3]=="":
                grids[row][col].update(grid_by_grid[row][col])

            elif bigger_grid[row//3][col//3]=="x" or bigger_grid[row//3][col//3]=="o":
                bigger_grid_buttons[row//3][col//3].update(bigger_grid[row//3][col//3])


    if empty_cells==0:
        only_play_on = [None, None]
    
    for row in range(0,WIDTH+1,WIDTH//3):
        for col in range(0,HEIGHT+1,HEIGHT//3):
            pygame.draw.line(surface,BORDER_COLOR,(0,col),(WIDTH,col), 5)
            pygame.draw.line(surface,BORDER_COLOR,(row,0),(row,HEIGHT), 5)
    
    bigger_grid = get_new_bigger_grid(grid_by_grid)

