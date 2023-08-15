#!/usr/bin/env python3
# 当你想保留的列的标题非常容易识别，或者在处理多个输入文件时，各个输入文件中列的位置会发生改变，但标题不变的时候，这种方法非常有效。
# 举例来说，假设你只需要保留发票号码列和购买日期列。
# 此示例中，需要先单独处理一下标题行，识别出相应标题行对应的索引值。
# 然后你可以使用索引值保留每行中的值，这些值和要保留的列标题具有同样的索引值。
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
# 创建了一个列表变量my_columns，其中包含了两个字符串，即要保留的两列的名字
my_columns = ['Invoice Number', 'Purchase Date']
# 创建了一个空列表变量my_columns_index，要使用两个保留列的索引值来填充它。
my_columns_index = []

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		# 在filereader对象上使用next函数从输入文件中读出第一行，并保存在列表变量header中
		header = next(filereader)
		# 初始化在列标题的索引值中迭代的for循环。
		for index_value in range(len(header)):
			# 码使用if语句和列表索引来检验每个列标题是否在my_columns中。
			# 例如，第一次for 循环时，index_value等于0，所以if 语句检验header[0]（也就是第一个列标题供应商姓名）是否在my_columns 中。
			# 因为供应商姓名不在my_columns 中，所以代码不会对这个值执行。
			if header[index_value] in my_columns:
				# 将这列的索引值加入到my_columns_index列表中
				my_columns_index.append(index_value)
		# 将my_columns 中的两个字符串写入输出文件
		filewriter.writerow(my_columns)
		# 下面的代码处理输入文件中余下的数据行
		for row_list in filereader:
			# 创建一个空列表row_list_output 来保存你要在每一行中保留的值。
			row_list_output = []
			# for循环在my_columns_index中的索引值之间迭代。
			for index_value in my_columns_index:
				# 将数据行中具有这些索引值的值加入row_list_output。
				row_list_output.append(row_list[index_value])
			# 将row_list_output 中的值写入输出文件。
			filewriter.writerow(row_list_output)
