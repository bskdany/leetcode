class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      cells = [set() for i in range(9)]
      row_seen = [set() for i in range(9)]
      col_seen = [set() for i in range(9)]

      for row_i in range(len(board)):
        for col_i in range(len(board)):
          val = board[row_i][col_i]
          if(val == "."):
            continue

          square_i = (row_i // 3)*3 + col_i // 3

          if val in cells[square_i] or val in col_seen[col_i] or val in row_seen[row_i]:
            return False
          cells[square_i].add(val)
          col_seen[col_i].add(val)
          row_seen[row_i].add(val)

      return True
