#!/usr/bin/env python3
# 要使用基础Python选取特定行，这里使用row_counter变量来跟踪行编号，以便可以识别和选取想保留的行。
# 从前面的示例中，你已经知道了要保留13行数据。在下面的if代码块中，你可以看到你要写入输出文件中的行就是行索引大于等于3并小于等于15的行。
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
# 这里使用row_counter 变量和一个if 语句来保留需要的行，跳过那些不需要的头部和尾部内容。
# 对于输入文件的前3 行，因为row_counter 小于3，所以不执行if 代码块，并将row_counter 的值增加1。
# 对于输入文件的最后3 行，row_counter 大于15，所以也不执行if 代码块，并将row_counter 的值增加1。
# 要保留的行在无用的头部和尾部之间。对于这些行,row_counter在3和15之间。if 代码块处理这些行并将它们写入输出文件。
# 在列表生成式中使用string模块的strip函数除去每行两端的空格、制表符和换行符。
# 如果想看看row_counter 变量的值和每行的内容，可以在现有的writerow 语句上面加上一个print 语句,
# 比如print(row_counter, [value.strip() for value in row])。
row_counter = 0
with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		for row in filereader:
			if row_counter >= 3 and row_counter <= 15:
				filewriter.writerow([value.strip() for value in row])
			row_counter += 1
