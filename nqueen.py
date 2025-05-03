class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]

    def is_safe(self, row, col):
        # Check left side of row
        for i in range(col):
            if self.board[row][i]:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j]:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, self.n), range(col, -1, -1)):
            if self.board[i][j]:
                return False

        return True

    def solve_n_queens_util(self, col):
        if col >= self.n:
            return True

        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                if self.solve_n_queens_util(col + 1):
                    return True
                self.board[i][col] = 0  # Backtrack

        return False

    def solve(self):
        if not self.solve_n_queens_util(0):
            return "No solution exists"
        return self.board

    def print_solution(self):
        for row in self.board:
            print(" ".join("Q" if cell else "_" for cell in row))


# Example usage
n = 8  # Change the value of n as required
solver = NQueens(n)
solution = solver.solve()
if isinstance(solution, str):
    print(solution)
else:
    solver.print_solution()
