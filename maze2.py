def SolveMaze(maze):
    column = 0
    row = 0
    lastMove = '<>'
    while row < (len(maze)):
        # print(row)
        print('Current Position: maze[' + str(column) + '][' + str(row) + '] ' + lastMove)
        for col in range(len(maze[row])):
            if maze[row][column] == 1:
                if column + 1 < len(maze[row]) and maze[row][column + 1] == 1 and lastMove != '←':
                    column += 1
                    row -= 1
                    lastMove = '→'
                elif row + 1 < len(maze) and column + 1 < len(maze[row]) and maze[row + 1][column + 1] == 1:
                    column += 1
                    lastMove = '↓→'
                elif row + 1 < len(maze) and maze[row + 1][column] == 1 and lastMove != '↑':    
                    lastMove = '↓'
                elif row - 1 >= 0 and column + 1 < len(maze[row]) and maze[row - 1][column + 1] == 1:    
                    row -= 2
                    column += 1
                    lastMove = '↑→'
                elif row - 1 >= 0 and maze[row - 1][column] == 1 and lastMove != '↓':     
                    row -=  2    
                    lastMove = '↑'
                elif column - 1 >= 0 and row + 1 <len(maze) and maze[row + 1][column - 1] == 1 and lastMove != '↑→':
                    column -= 1
                    lastMove = '←↓'
                if len(maze) - 1 == row:
                    return True
                else:
                    break
            else:
                return False
        row += 1

def PrintMaze(maze):
    print(maze)
    
    
def main():
    maze = [
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1]
    ]
    # maze = [
    #     [1, 0],
    #     [0, 1],
    #     [1, 1],
    #     [1, 0],
    #     [1, 1]
 
    # ]

    PrintMaze(maze)

    if SolveMaze(maze):
        print('solution exists')
    else:
        print('solution does not exist')

if __name__ == "__main__":
    main()
