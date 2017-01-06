#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://blog.csdn.net/ngforever/article/details/14225495
#http://www.jb51.net/article/60510.htm

import xlwt

workbook = xlwt.Workbook()
my_sheet=workbook.add_sheet(u'my_worksheet',cell_overwrite_ok=True) #创建sheet, overwrite is allowed
my_sheet.write(0, 0, label = 'yujing') #cell 中写入元素

row0=[u'业务', u'状态', u'北京', u'上海', u'广州', u'深圳', u'状态小计', u'合计'] #raw, column 中写内容
column0 = [u'机票', u'船票', u'火车票', u'汽车票', u'其它']
for i in range(0,len(row0)):
    my_sheet.write(0,i,row0[i])
for j in range(1,len(column0)):
    my_sheet.write(j,0,column0[j])


#确定输入内容的格式
font = xlwt.Font() # Create the Font
font.name = 'Times New Roman' #字体
font.bold = True     #是否加粗
font.underline = True #是否下划线
font.italic = True  #是否斜体

borders= xlwt.Borders() #边界
borders.left= 6
borders.right= 6
borders.top= 6
borders.bottom= 6

style = xlwt.XFStyle() # Create the Style，初始化样式
style.font = font # Apply the Font to the Style
style.borders=borders

my_sheet.write(2, 3, label = 'Unformatted value')
my_sheet.write(2, 4, label='Formatted yujing',style=style) # Apply theStyle to the Cell

workbook.save('Excel_Workbook2.xls') #save excel