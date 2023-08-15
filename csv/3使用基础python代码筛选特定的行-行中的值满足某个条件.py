#!/usr/bin/env python3
# 下面的示例演示了检验行值是否满足两个具体条件的方法，并将满足条件的行的子集写入一个输出文件
# 在这个示例中，保留供应商名字为Supplier Z 或成本大于$600.00 的行，并将结果写入输出文件。
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		# 使用csv 模块的next 函数读出输入文件的第一行，赋给名为header 的列表变量
		header = next(filereader)
		# 代码将标题行写入输出文件
		filewriter.writerow(header)
		for row_list in filereader:
			# 取出每行数据中的供应商名字，并赋给名为supplier 的变量
			# 。这行代码使用
			# 列表索引取出每行数据的第一个值row[0]，然后使用str 函数将其转换为一个字符串。
			# 之后使用strip 函数删除字符串两端的空格、制表符和换行符。最后，将处理好的字符串赋给变量supplier。
			supplier = str(row_list[0]).strip()
			# 取出每行数据中的成本，并赋给名为cost的变量。
			# 这行代码使用列表索引取出每行数据的第四个值row[3]，然后使用str函数将其转换为一个字符串。
			# 在此之后，使用strip函数从字符串中删除美元符号。接着使用replace函数从字符串中删除逗号。
			# 最后，将处理好的字符串赋给变量cost。
			cost = str(row_list[3]).strip('$').replace(',', '')
			# 创建了一个if 语句，来检验每行中的这两个值是否满足条件。
			# 具体来说，这里想筛选出供应商名字为Supplier Z 或者成本大于$600.00 的那些行。
			# if 和or 之间的第一个条件检验变量supplier 中的值是否为Supplier Z。
			# or 和冒号之间的第二个条件检验变量cost 中的值在被转换为浮点数之后，是否大于600.0。
			if supplier == 'Supplier Z' or float(cost) > 600.0:
				# 第16行代码使用filewriter的writerow函数将满足条件的行写入输出文件。
				filewriter.writerow(row_list)