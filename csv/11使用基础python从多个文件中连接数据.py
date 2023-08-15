#!/usr/bin/env python3
# pandas 中的read_csv 函数可以直接指定输入文件不包含标题行，并可以提供一个列标题列表。
import csv
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

first_file = True
for input_file in glob.glob(os.path.join(input_path,'sales_*')):
	print(os.path.basename(input_file))
	with open(input_file, 'r', newline='') as csv_in_file:
		# 使用'a' 代替'w' 以追加的方式打开输出文件，以使每个输入文件中的数据可以追加（也就是添加）到输出文件中。
		# 如果使用可写方式，从一个输入文件中输出的数据会覆盖掉前一个输入文件中的数据，最后的输出文件会只包含最后处理的那个输入文件中的数据。
		with open(output_file, 'a', newline='') as csv_out_file:
			filereader = csv.reader(csv_in_file)
			filewriter = csv.writer(csv_out_file)
			# if-else语句根据第9行代码中创建的first_file变量来区分当前文件是第一个输入文件，还是其后的输入文件。
			# 在输入文件中做这个区分的目的是将标题行仅写入输出文件一次。if代码块处理第一个输入文件，将包括标题行的所有行写入输出文件。
			# else 代码块处理所有余下的输入文件，使用next方法将每个文件中的标题行赋给一个变量（这样就可以在后面的处理过程中跳过标题行），
			# 然后将其余数据行写入输出文件。
			if first_file:
				for row in filereader:
					filewriter.writerow(row) 	# 将这些列表值写入输出文件的第一行
				first_file = False
			else:
				header = next(filereader)
				for row in filereader:
					filewriter.writerow(row) 	# 将所有数据行写入输出文件，放在标题行下面
