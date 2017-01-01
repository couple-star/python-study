#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

lists=[3, 2, -5, 6, 4, 0, 9, -7, 0, 1]
# while True:
#     num=raw_input('please input the numbers, input q if you want to stop: ')
#     if num=='q':
#         break
#     else:
#         nums=eval(num)
#         lists.append(nums)
#print lists
# sort=sorted(lists, cmp=lambda x,y : cmp(x, y))
# print sort
#
# for j in range(len(sort)):
#     i=sort.index(0)
#     sort.pop(i)
#     sort.append(0)
# print sort
# lists.sort(cmp=lambda x, y: -1 if y == 0 else (x - y) / abs(x - y))
lists.sort()
lists.sort(cmp=lambda x, y: -1 if y == 0 else 1)
print lists