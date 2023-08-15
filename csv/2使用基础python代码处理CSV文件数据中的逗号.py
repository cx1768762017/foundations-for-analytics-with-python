#!/usr/bin/env python3
# 使用基础python代码处理CSV文件数据中的逗号
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		# 使用csv 模块中的reader 函数创建了一个文件读取对象，名为filereader，可以使用这个对象来读取输入文件中的行
		filereader = csv.reader(csv_in_file, delimiter=',')
		# 使用csv 模块的writer 函数创建了一个文件写入对象，名为filewriter，可以使用这个对象将数据写入输出文件
		filewriter = csv.writer(csv_out_file, delimiter=',')
		# 这些函数中的第二个参数（就是delimiter=','）是默认分隔符，所以如果你的输入文件和输出文件都是用逗号分隔的，
		# 就不需要指定这个参数。这里指定了这个分隔符参数，是为了防备你处理的输入文件或要写入的输出文件具有不同的分隔符，
		# 例如，分号（;）或制表符（\t）。

		for row_list in filereader:
			# 使用filewriter 对象的writerow 函数来将每行中的列表值写入输出文件
			filewriter.writerow(row_list)
