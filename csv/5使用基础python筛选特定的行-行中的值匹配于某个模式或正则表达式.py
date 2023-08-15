#!/usr/bin/env python3
# 下面的示例演示了如何检验某个值是否匹配特定的模式，并将具有这种值的行写入输出文件。
# 在这个示例中，保留发票编号由“001-”开头的行，并将结果写入一个输出文件。
import csv
import re
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
# 使用re模块的compile函数创建一个名为pattern的正则表达式变量。r表示将单引号之间的模式当作原始字符串来处理。
# 元字符?P<my_pattern_group> 捕获了名为<my_pattern_group> 的组中匹配了的子字符串，以便在需要时将它们打印到屏幕或写入文件。
# 这里要搜索的实际模式是^001-.*。插入符号（^）是一个特殊符号，表示只在字符串开头搜索模式。
# 所以，字符串需要以“001-”开头。句点. 可以匹配任何字符，除了换行符。
# 所以除换行符之外的任何字符都可以跟在“001-”后面。
# 最后，* 表示重复前面的字符0次或更多次。
# .* 组合在一起用来表示除换行符之外的任意字符可以在“001-”后面出现任意次。
# 更通俗的说法是：字符串在“-”后面可以包含任意值，只要字符串开始于“001-”，就会匹配正则表达式。
# 最后，参数re.I 告诉正则表达式进行大小写敏感的匹配。此参数在这个示例中不是太重要，因为模式是数值型的，
# 但是它说明了在模式中包含字符并且需要进行大小写敏感的匹配时，应该如何设置参数。
pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)

with open(input_file, 'r', newline='') as csv_in_file:
	with open(output_file, 'w', newline='') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		filewriter.writerow(header)
		for row_list in filereader:
			# 使用列表索引从行中取出发票编号，并赋给变量invoice_number。在下一行中，将在这个变量中寻找模式。
			invoice_number = row_list[1]
			# 使用re 模块的search 函数在invoice_number 的值中寻找模式。
			# 如果模式出现在invoice_number值中，下一行代码就将这行写入输出文件。
			if pattern.search(invoice_number):
				filewriter.writerow(row_list)