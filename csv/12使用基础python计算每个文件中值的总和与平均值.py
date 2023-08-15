#!/usr/bin/env python3
import csv
import glob
import os
import string
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]
# 创建了一个输出文件的列标题列表
output_header_list = ['file_name', 'total_sales', 'average_sales']

csv_out_file = open(output_file, 'a', newline='')
filewriter = csv.writer(csv_out_file)
# 将标题行写入输出文件
filewriter.writerow(output_header_list)

for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	with open(input_file, 'r', newline='') as csv_in_file:
		filereader = csv.reader(csv_in_file)
		# 创建了一个空列表，保存要写入输出文件中的每行输出。
		output_list = [ ]
		# 将输入文件的文件名追加到output_list 中
		output_list.append(os.path.basename(input_file))
		# 使用next 函数除去每个输入文件的标题行
		header = next(filereader)
		total_sales = 0.0
		number_of_sales = 0.0
		# 在每个输入文件的数据行之间迭代。
		for row in filereader:
			# 使用列表索引取出销售额这列中的值，并赋给变量sale_amount
			sale_amount = row[3]
			# 使用str 函数确保sale_amount 中的值是一个字符串，然后使用strip 函数和replace 函数除去值中的美元符号和逗号。
			# 此后使用float 函数将这个值转换为浮点数，并将这个值加到total_sales 中的值上。
			total_sales += float(str(sale_amount).strip('$').replace(',',''))
			number_of_sales += 1.0
		# 用total_sales 中的值除以number_of_sales 中的值，为输入文件计算出平均销售额，然后将这个数值格式化成具有两位小数的数值，
		# 并转换成字符串，赋给变量average_sales。
		average_sales = '{0:.2f}'.format(total_sales / number_of_sales)
		# 将总销售额作为第二个值添加到output_list中。列表中的第一个值是输入文件的名字。
		output_list.append(total_sales)
		# 将平均销售额作为第三个值添加到output_list 中
		output_list.append(average_sales)
		# 将output_list 中的值写入输出文件。
		filewriter.writerow(output_list)
csv_out_file.close()
