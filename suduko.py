
class Sudoku:
    def __init__(self, board):
        self.board = board
        self.size = 9
        self.stack = []

    def is_valid(self, row, col, num):
        for x in range(self.size):
            if self.board[row][x] == num or self.board[x][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[i + start_row][j + start_col] == num:
                    return False
        return True
    
    def find_empty(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return (i, j)
        return None
    
    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                self.stack.append((row, col, num))

                if self.solve():
                    return True

                self.board[row][col] = 0
                self.stack.pop()
        
        return False
    
    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) for num in row))

# Example usage:
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
sudoku = Sudoku(board)
sudoku.print_board()
print("\nSolving Sudoku...\n")
sudoku.solve()
print("\nSudoku solved:\n")
sudoku.print_board()