#!/usr/bin/env python3
# 下面的示例演示了检验行值是否是集合成员的方法，并将具有集合中的值的行写入到输出文件。
# 在这个示例中，是要保留那些购买日期属于集合{'1/20/14', '1/30/14'} 的行，并将结果写入输出文件。
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
# 创建了一个名为important_dates 的列表变量，其中包含两个特定日期，这个变量就是你的集合。
# 创建包含特定值的变量，然后在代码中引用变量，这种编写代码的方式非常有用。
# 使用了这种方式，如果变量值发生了变化，你只需在一个地方修改代码（就是定义变量的地方），
# 变量值的变化就会反映到代码中所有引用该变量的地方。
important_dates = ['1/20/14', '1/30/14']

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		filewriter.writerow(header)
		for row_list in filereader:
			# 取出每一行的购买日期，并将其赋给变量a_date。从行列表的索引值row[4]可知，购买日期在第5列。
			a_date = row_list[4]
			# 创建了一个if 语句来检验a_date 变量中的购买日期是否属于important_dates 这个集合。
			# 如果变量值在集合中，下一行代码就将这一行写入输出文件。
			if a_date in important_dates:
				filewriter.writerow(row_list)
