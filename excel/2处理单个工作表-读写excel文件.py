#!/usr/bin/env python3
import sys
from xlrd import open_workbook
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]
# 实例化一个xlwt Workbook 对象，以使我们可以将结果写入用于输出的Excel文件。
output_workbook = Workbook()
# 使用xlwt 的add_sheet 函数为输出工作簿添加一个工作表jan_2013_output。
output_worksheet = output_workbook.add_sheet('jan_2013_output')
# 使用xlrd 的open_workbook 函数打开用于输入的工作簿，并将结果赋给一个workbook 对象。
with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2013')
	# 创建了行与列索引值上的for循环语句，使用range函数和worksheet对象的nrows属性和ncols属性，在工作表的每行和每列之间迭代。
	for row_index in range(worksheet.nrows):
		for column_index in range(worksheet.ncols):
			# 使用xlwt 的write 函数和行与列的索引将每个单元格的值写入输出文件的工作表。
			output_worksheet.write(row_index, column_index, worksheet.cell_value(row_index, column_index))
# 保存并关闭输出工作簿
output_workbook.save(output_file)