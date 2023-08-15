#!/usr/bin/env python3
# 在CSV 文件中选取特定列的一种方法是使用你想保留的列的索引值。
# 当你想保留的列的索引值非常容易识别，或者在处理多个输入文件时，各个输入文件中列的位置一致（也就是不会发生改变）的时候，这种方法非常有效。
# 例如，如果你只需要保留数据的第一列和最后一列，那么你可以使用row[0] 和row[-1] 来将每行的第一个值和最后一个值写入文件。
# 在这个示例中，你只想保留供应商姓名和成本这两列。
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
# 创建了一个列表变量my_columns，其中包含了你想保留的两列的索引值。在这个示例中，这两个索引值对应着供应商姓名和成本列。
# 再说一次，应该创建一个包含索引值的变量，然后在代码中引用这个变量。
# 这样，如果索引值需要改变的话，你只需要在一个地方（就是定义my_columns 的地方）修改即可，修改会反映到代码中所有引用my_columns 的地方。
my_columns = [0, 3]

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		for row_list in filereader:
			# 创建了一个空列表变量row_list_output。这个变量保存你在每行中要保留的值。
			row_list_output = []
			# 在my_cloumns 中的各个索引值之间进行迭代。
			for index_value in my_columns:
				# 通过列表的append函数使用每行中my_columns索引位置的值为row_list_output填充元素
				row_list_output.append(row_list[index_value])
			# 上面的3行代码生成了一个列表，列表中包含了每行中你要写入输出文件的值。
			# 创建列表是有用的，因为filewriter 的writerow 方法需要一个字符串序列或数值序列，而列表row_list_out 正是一个字符串序列。

			# 将row_list_output 中的值写入输出文件。
			filewriter.writerow(row_list_output)

# 脚本会对输入文件中的每一行执行这些代码。为了确切地理解这一系列操作，下面来看看第一次外部for循环做了些什么。
# 在本例中，你处理的是输入文件中的第一行（也就是标题行）。第12 行代码创建了空列表变量row_list_output。
# 第13 行代码是一个for 循环，在my_columns 的值之间迭代。
# 第一次循环时，index_value 等于0，所以第14 行代码中的append 函数将row[0]（就是供应商姓名字符串）加入row_list_output。
# 此后，代码回到第13行中的for循环，这一次index_value 等于3。
# 因为index_value 等于3，所以第14 行代码中的append 函数将row[3]（也就是成本字符串）加入row_list_output。
# my_columns 中没有更多的值了，所以第13 行中的for 循环结束，代码前进到第15 行。
# 第15 行代码将row_list_output 中的列表值写入输出文件。
# 然后，代码回到第11 行中的外部for 循环，开始处理输入文件中的下一行。
