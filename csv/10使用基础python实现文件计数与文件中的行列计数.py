#!/usr/bin/env python3
# glob 模块可以定位匹配于某个特定模式的所有路径名。模式中可以包含Unixshell 风格的通配符，比如*。
# 在上面这个具体示例中，要搜索的模式是'sales_*'。这个模式表示要搜索所有文件名以sales_ 开头并且下划线后面可以是任意字符的文件。
# 因为你创建了3 个输入文件，所以应该知道使用这段代码可以识别出这3个文件，它们的文件名都是以sales_开头的，下划线后面是不同的月份。

# os模块包含了用于解析路径名的函数。例如，os.path.basename(path) 返回path 的基本文件名。
# 即，如果path 是C:\Users\Clinton\Desktop\my_input_file.csv，那么os.path.basename(path) 返回my_input_file.csv。
import csv
import glob
import os
import sys

input_path = sys.argv[1]

file_counter = 0
# 将数据处理扩展到多个文件中的关键语句。此行代码创建了一个for循环，在一个输入文件集合中迭代，
# 并使用glob模块和os模块中的函数创建了一个输入文件列表以供处理。
# os 模块中的os.path.join()函数将函数圆括号中的两部分连接在一起。
# input_path是包含输入文件的文件夹的路径，'sales_*' 代表任何以模式'sales_'开头的文件名。

# glob模块中的glob.glob() 函数将'sales_*' 中的星号（*）转换为实际的文件名。
# 在这个示例中，glob.glob() 函数和os.path.join() 函数创建了一个包含3 个输入文件的列表：
# ['C:\Users\Clinton\Desktop\sales_january_2014.csv',
# 'C:\Users\Clinton\Desktop\sales_february_2014.csv',
# 'C:\Users\Clinton\Desktop\sales_march_2014.csv']
# 然后，这行开头的for 循环语句对于列表中每个输入文件执行下面缩进的各行代码。
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	row_counter = 1
	with open(input_file, 'r', newline='') as csv_in_file:
		filereader = csv.reader(csv_in_file)
		header = next(filereader)
		for row in filereader:
			row_counter += 1
	# 打印出每个输入文件的文件名、文件中的行数、文件中的列数。print 语句中的制表符\t不是必需的，但是在各列之间放上一个制表符可以对齐这3列。
	# 这行代码使用{} 占位符将3 个值传入print 语句。
	# 对于第一个值，使用os.path.basename() 函数从完整路径名中抽取出基本文件名。
	# 对于第二个值，使用row_counter 变量来计算每个输入文件中的总行数。
	# 最后，对于第三个值，使用内置的len 函数计算出列表变量header 中的值的数量，这个列表变量中包含了每个输入文件的列标题列表。
	# 我们使用这个值作为每个输入文件中的列数。
	print('{0!s}: \t{1:d} rows \t{2:d} columns'.format(\
	os.path.basename(input_file), row_counter, len(header)))
	# 使用file_counter 变量中的值显示出脚本处理的文件的数量。
	file_counter += 1
print('Number of files: {0:d}'.format(file_counter))
