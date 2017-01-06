#!/usr/bin/env python
# -*- coding: utf-8 -*-
# excel 读写链接http://www.jb51.net/article/60510.htm
#http://blog.csdn.net/erlang_hell/article/details/51992928, different version excel solution

import xlrd

data=xlrd.open_workbook('/Users/yujing/Desktop/excel_exercise.xlsx', formatting_info=True)#打开excel文件

table=data.sheets()[1]
table=data.sheet_by_index(1)
table=data.sheet_by_name(u'sheet2')#以上三种都是打开sheet

row=table.row_values(1)
for i in row:
    print i                        #print row or column elements

#column=table.col_values(1)
#for j in column:
#    print j

nrows=table.nrows
print nrows

#ncolumns=table.ncols
#print ncolumns                 #get the number of rows and columns

cell_A1=table.cell(0,0).value
print cell_A1                   #print cell content

print table.cell(1,0).ctype    #excel type: 0 is null, 1 is string, 2 is number, 3 is date, 4 is booleam, 5 is error

#print table.merged_cells


