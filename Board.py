from typing import List
class Board:
    
    def create_board(self) -> List:
        matrix: List = []
        for _ in range(60):
            temp_row: List = []
            for _ in range(60):
                temp_row.append(0)
            matrix.append(temp_row)
        return matrix

board = Board()
for x in board.create_board():
    print(x)