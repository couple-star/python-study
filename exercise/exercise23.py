#leecode 463. Island Perimeter
#You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

a=[[0,0,0,1,0,0],
   [0,0,1,1,1,0],
   [0,0,0,1,0,0]]
b=0
num=0
print a

for i in a:
    i[:] = [0] + i + [0]
x = [0 for _ in a[0]]
a[:] = [x] + a + [x]

print a

for i in range(0,len(a)):
     for j in range(0,len(a[0])):
         if a[i][j]==1:
             num += 1
             if a[i-1][j]==1:
                 b+=1
             if a[i+1][j]==1:
                 b+=1
             if a[i][j-1]==1:
                 b+=1
             if a[i][j+1]==1:
                 b+=1
print b
print 4*num

perimeter=4*num-b

print perimeter



