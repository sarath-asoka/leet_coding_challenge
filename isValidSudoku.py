
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        rs = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
                    rs += [(i,element), (element, j)]
                    print([i , j, element])
                    # print(len(rs),len(set(rs)))
        return [len(res) == len(set(res)),len(rs) == len(set(rs))]

                    


        
board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
sol = Solution()
print(sol.isValidSudoku(board))        