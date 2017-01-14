#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time:  O(m * n)
# Space: O(1)

# Given an 2D board, count how many different battleships are in it.
# The battleships are represented with 'X's, empty slots are represented with '.'s.
# You may assume the following rules:
#
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words,
# they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column),
# where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships -
# there are no adjacent battleships.
#
# Example:
# X..X
# ...X
# ...X
# In the above board there are 2 battleships.
# Invalid Example:
# ...X
# XXXX
# ...X
# This is not a valid board - as battleships will always have a cell separating between them.
# Your algorithm should not modify the value of the board.


# board=[['.', 'x', 'x', 'x', 'x'],['.', '.', '.', '.', '.'],['.', '.', 'x', 'x', '.']]
# board=[['x', 'x', '.', '.', '.'],['.', 'x', 'x', 'x', 'x'],['.', 'x', '.', '.', '.'],['.', 'x', 'x', 'x', '.']]
# countBattleships()
board = ["X..X","...X","...X"]


# def countBattleships(self, board):

# board = [[''.join(i)] for i in board]
for i in board:
    print i

n = len(board)
m = 0
for j in range(n):
    string = board[j][0]  # stri, 一行的情况,如：...X
    lenth = len(string)
    if string[lenth - 1] == 'x':
        m += 1
    for i in range(lenth - 1):
        if string[i] == 'x':
            if string[i + 1] == '.':
                m += 1
print m

