def solve(board):
    # Dimensions for the board 
    m=len(board)
    n=len(board[0])
    # Defining a function for dfs
    def dfs(m,n):
        # Base condition, we do nothing if we find 'X' or if limit exceeds
        if n <0 or m<0 or n == len(board[0]) or m == len(board) or board[m][n]!='O':
            return
        # Else we change it to N
        board[m][n]='N'
        # We explore its directions and repeat the manpulation
        dfs(m+1,n) # Lower cell
        dfs(m,n+1) # Right cell
        dfs(m-1,n) # Upper cell
        dfs(m,n-1) # Left cell
    # We traverse every element present on the board, if we find 'O' we move it to dfs
    for i in range(m):
        for j in range(n):
            #If element is 'O' and is on the borders of the board we move it to dfs
            if (board[i][j]=='O' and (i in [0,m-1] or j in [0,n-1])):
                dfs(i,j)
    # Now traverse the entire board, if we find N, change it to O else we change it to X.
    for i in range(m):
        for j in range(n):
            if board[i][j]=='O':
                board[i][j]='X'
            if board[i][j]=='Y':
                board[i][j]='O' 

m = int(input("Enter no of columns = "))
n = int(input("Enter no of rows = "))

board = [[""]*m]*n # creating board
print(board)

for i in range(m):
    for j in range(n):
        board[j][i] = input(f"Enter value in the {i}, {j} th positon\n")

# Default board input  
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print("Solution using Breadth First Search")
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