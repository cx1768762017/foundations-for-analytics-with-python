#!/usr/bin/env python3
import pandas as pd
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path,'sales_*'))
all_data_frames = []
for input_file in all_files:
	data_frame = pd.read_csv(input_file, index_col=None)
	
	total_sales = pd.DataFrame([float(str(value).strip('$').replace(',','')) \
						for value in data_frame.loc[:, 'Sale Amount']]).sum()
	
	average_sales = pd.DataFrame([float(str(value).strip('$').replace(',','')) \
						for value in data_frame.loc[:, 'Sale Amount']]).mean()

	data = {'file_name': os.path.basename(input_file),
			'total_sales': total_sales,
			'average_sales': average_sales}
	
	all_data_frames.append(pd.DataFrame(data, columns=['file_name', 'total_sales', 'average_sales']))

data_frames_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)

data_frames_concat.to_csv(output_file, index = False)

# pandas 提供了可以用来计算行和列统计量的摘要统计函数，比如sum 和mean。下面的代码
# 演示了如何对于多个文件中的某一列计算这两个统计量（总计和均值），并将每个输入文
# 件的计算结果写入输出文件。

# 使用列表生成式将销售额这一列中带美元符号的字符串转换为浮点数，然后使用数据框函
# 数将这个对象转换为一个DataFrame，以便可以使用这两个函数计算列的总计和均值。
# 因为输出文件中的每行应该包含输入文件名，以及文件中销售额的总计和均值，所以可以
# 将这3 种数据组合成一个文本框，使用concat 函数将这些数据框连接成为一个数据框，然
# 后将这个数据框写入输出文件。