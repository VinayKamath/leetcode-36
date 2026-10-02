# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 21:15:18 2026

@author: vinay
"""

from typing import List

board = [["1","2",".",".","3",".",".",".","."],
         ["4",".",".","5",".",".",".",".","."],
         [".","9","8",".",".",".",".",".","3"],
         ["5",".",".",".","6",".",".",".","4"],
         [".",".",".","8",".","3",".",".","5"],
         ["7",".",".",".","2",".",".",".","6"],
         [".",".",".",".",".",".","2",".","."],
         [".",".",".","4","1","9",".",".","8"],
         [".",".",".",".","8",".",".","7","9"]]


def isValidSudoku(board: List[List[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = {}

    for r in range(9):
        for c in range(9):

            value = board[r][c]

            if value == ".":
                continue

            box = (r // 3, c // 3)

            if value in rows[r]:
                return False

            if value in cols[c]:
                return False

            if box in boxes and value in boxes[box]:
                return False

            rows[r].add(value)
            cols[c].add(value)

            if box not in boxes:
                boxes[box] = set()

            boxes[box].add(value)

    return True

isValidSudoku(board)

