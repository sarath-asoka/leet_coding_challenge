
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        r = []
        for i in range(len(board)):
            for j in range(len(board)):
                element = board[i][j]
                if element != '.':
                    print(element)
                    


        
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
sol = Solution()
print(sol.isValidSudoku(board))        