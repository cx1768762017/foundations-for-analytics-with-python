#!/usr/bin/env python3
import sys
from xlrd import open_workbook

input_file = sys.argv[1]
# 使用open_workbook 函数打开一个Excel 输入文件，并赋给一个名为workbook的对象。
# workbook 对象中包含了工作簿中所有可用的信息，所以可以使用这个对象从工作簿中得到单独的工作表。
workbook = open_workbook(input_file)
# 打印出工作簿中工作表的数量
print('Number of worksheets:', workbook.nsheets)
# 在工作簿中的所有工作表之间迭代。workbook 对象的sheets 方法可以识别出工作簿中所有的工作表。
for worksheet in workbook.sheets():
	# 在屏幕上打印出每个工作表的名称和每个工作表中行与列的数量。print 语句使用worksheet 对象的name 属性来确定每个工作表的名称。
	# 同样，它使用nrows 和ncols属性来分别确定每个工作表中行与列的数量。
	print("Worksheet name:", worksheet.name, "\tRows:", \
			worksheet.nrows, "\tColumns:", worksheet.ncols)

