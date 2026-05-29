from typing import List
from collections import defaultdict


#  Hash Set tc - n2, sc n2
def isValidSudoku(self, board: List[List[str]]) -> bool:
    squares= defaultdict(set) 
    rows = defaultdict(set) 
    cols = defaultdict(set) 

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (
                board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in squares[(r // 3, c // 3)]
            ):
                return False

            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[r//3,c//3].add(board[r][c])
    
    return True

#Bitmask - tc n2, sc n
def isValidSudoku1(self, board: List[List[str]]) -> bool:
    rows = [0] * 9
    cols = [0] * 9
    squares = [0] * 9

    for r in range(9):
        for c in range(9):
            if board[r][c]=='.':
                continue
            
            val = int(board[r][c]) - 1
            if (1 << val) & rows[r]:
                return False
            if (1<< val) & cols[c]:
                return False
            if (1<< val) & squares[(r//3)*3+ (c//3)]:
                return False
            
            rows[r] |= (1<<val)
            cols[c] |= (1<<val)
            squares[(r//3)*3 + (c//3)] |= (1<<val)
            
    return True