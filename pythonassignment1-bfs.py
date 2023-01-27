from collections import deque


def solve(board):
    # Given dimensions for the board 
    m, n = len(board), len(board[0])
    # Creating a queue
    queue = deque()
    # We traverse the borders of the board and add cells with entry 'O', to the queue
    # Then traverse from indices [0][0] to [m-1][0] and from [0][n-1] to [m-1][n-1]
    for i in range(m):
        if board[i][0] == 'O':
            queue.append((i, 0))
        if board[i][n-1] == 'O':
            queue.append((i, n-1))
    # Now traversing from index [m-1][0] to [m-1][n-1] and [0][0] to [0][n-1]
    for j in range(n):
        if board[0][j] == 'O':
            queue.append((0, j))
        if board[m-1][j] == 'O':
            queue.append((m-1, j))
    # Implementation of Breadth First Search using Queue loaded above 
    while queue:
        # Popinng the vertices from left end of queue and explore it.
        r, c = queue.popleft()
        # If we come across any 'O' in border we mark it as N as we cannot capture it.
        if 0 <= r < m and 0 <= c < n and board[r][c] == 'O':
            board[r][c] = 'N'
            # We explore its surrounding cells and repeat the manpulation
            queue.append((r-1, c)) # Upper cell
            queue.append((r+1, c)) # Lower cell
            queue.append((r, c-1)) # Left cell
            queue.append((r, c+1)) # Right cell
    # Now traverse the entire board, if we find N change it to O else we change it to X.
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'N':
                board[i][j] = 'O'
            else:
                board[i][j] = 'X'

m = int(input("Enter no of columns = "))
n = int(input("Enter no of rows = "))

board = [[""]*m]*n # creating board
print(board)

for i in range(m):
    for j in range(n):
        board[j][i] = input(f"Enter value in the {i}, {j} th positon\n")

# Default board input  
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print("Using Breadth First Search")
print("\nBoard before captures")
for x in board:
   for y in x:
      print(y,end = " ")
   print()

solve(board)
print("\nBoard after captures - ")
for x in board:
   for y in x:
      print(y,end = " ")
   print()