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

workbook.save('/Users/yujing/Desktop/Excel_Workbook2.xls') #save excel

##--------------Attributes of the FontObject----------------
#font.bold = True # May be: True, False
#font.italic = True # May be: True, False
#font.struck_out = True # May be: True, False
#font.underline = xlwt.Font.UNDERLINE_SINGLE # May be:UNDERLINE_NONE, UNDERLINE_SINGLE, UNDERLINE_SINGLE_ACC,UNDERLINE_DOUBLE, UNDERLINE_DOUBLE_ACC
#font.escapement = xlwt.Font.ESCAPEMENT_SUPERSCRIPT # May be:ESCAPEMENT_NONE, ESCAPEMENT_SUPERSCRIPT, ESCAPEMENT_SUBSCRIPT
#font.family = xlwt.Font.FAMILY_ROMAN # May be: FAMILY_NONE,FAMILY_ROMAN, FAMILY_SWISS, FAMILY_MODERN, FAMILY_SCRIPT,FAMILY_DECORATIVE
#font.charset = xlwt.Font.CHARSET_ANSI_LATIN # May be:CHARSET_ANSI_LATIN, CHARSET_SYS_DEFAULT, CHARSET_SYMBOL,CHARSET_APPLE_ROMAN, CHARSET_ANSI_JAP_SHIFT_JIS,CHARSET_ANSI_KOR_HANGUL, CHARSET_ANSI_KOR_JOHAB,CHARSET_ANSI_CHINESE_GBK, CHARSET_ANSI_CHINESE_BIG5,CHARSET_ANSI_GREEK, CHARSET_ANSI_TURKISH, CHARSET_ANSI_VIETNAMESE,CHARSET_ANSI_HEBREW, CHARSET_ANSI_ARABIC, CHARSET_ANSI_BALTIC,CHARSET_ANSI_CYRILLIC, CHARSET_ANSI_THAI, CHARSET_ANSI_LATIN_II,CHARSET_OEM_LATIN_I
#font.colour_index = ?
#font.get_biff_record = ?
#font.height = 0x00C8 # C8 in Hex (in decimal) = 10 points inheight.
#font.name = ?
#font.outline = ?
#font.shadow = ?

##--------------enter a date----------------
#import xlwt
#import datetime
#workbook = xlwt.Workbook()
#worksheet = workbook.add_sheet('My Sheet')
#style = xlwt.XFStyle()
#style.num_format_str = 'M/D/YY' # Other options: D-MMM-YY, D-MMM,MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss,[h]:mm:ss, mm:ss.0
#worksheet.write(0, 0, datetime.datetime.now(), style)
#workbook.save('Excel_Workbook.xls')

