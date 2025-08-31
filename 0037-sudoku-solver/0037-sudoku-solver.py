class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(board, row, col, c):
            for i in range(9):
                if board[row][i] == c: return False
                if board[i][col] == c: return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c: 
                    return False
            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for c in map(str, range(1, 10)):
                            if isValid(board, i, j, c):
                                board[i][j] = c
                                if solve(board): return True
                                board[i][j] = '.'
                        return False
            return True

        solve(board)