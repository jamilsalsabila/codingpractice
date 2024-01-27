from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    row = len(board)
    col = len(board[0])


print(exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
