#!/usr/bin/env python3

# 使用基础Python代码来读写和处理CSV 文件
import sys
# 使用sys 模块的argv 参数，它是一个传递给Python 脚本的命令行参数列表，
# 也就是当你运行脚本时在命令行中输入的内容。
input_file = sys.argv[1]
output_file = sys.argv[2]
# witch语句可以在语句结束时自动关闭文件对象。
with open(input_file, 'r', newline='') as filereader:
	with open(output_file, 'w', newline='') as filewriter:
		# 使用文件对象的readline 方法读取输入文件中的第一行数据，在本例中，第一行是标题行，读入后将其作为字符串并赋给名为header 的变量
		header = filereader.readline()
		# 代码使用string 模块中的strip 函数去掉header 中字符串两端的空格、制表符和换行符，并将处理过的字符串重新赋给header
		header = header.strip()
		# 代码使用string 模块的split 函数将字符串用逗号拆分成列表，列表中的每个值都是一个列标题，最后将列表赋给变量header_list
		header_list = header.split(',')
		print(header_list)
		# 使用filewriter 对象的write 方法将header_list 中的每个值写入输出文件
		# map 函数将str 函数应用于header_list中的每个元素，确保每个元素都是字符串。
		# 然后，join 函数在header_list 中的每个值之间插入一个逗号，将这个列表转换为一个字符串。
		# 在此之后，在这个字符串最后添加一个换行符。
		# 最后，filewriter 对象将这个字符串写入输出文件，作为输出文件的第一行。
		filewriter.write(','.join(map(str,header_list))+'\n')
		# 创建了一个for 循环，在输入文件剩余的各行中迭代
		for row in filereader:
			# 使用strip 函数除去每行字符串两端的空格、制表符和换行符，然后将处理过的字符串重新赋给变量row。
			row = row.strip()
			# 代码用split 函数用逗号将字符串拆分成一个列表，列表中的每个值都是这行中某一列的值，然后，将列表赋给变量row_list
			row_list = row.split(',')
			print(row_list)
			# 将这些值写入输出文件
			filewriter.write(','.join(map(str, row_list))+'\n')
