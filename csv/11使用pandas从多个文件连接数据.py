#!/usr/bin/env python3
# 基本过程就是将每个输入文件读取到pandas 数据框中，将所有数据框追加到一个数据框列表，然后使用concat 函数将所有数据框连接成一个数据框。
# concat 函数可以使用axis 参数来设置连接数据框的方式，axis=0 表示从头到尾垂直堆叠，axis=1 表示并排地平行堆叠。
import pandas as pd
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path,'sales_*'))

all_data_frames = []
for file in all_files:
	data_frame = pd.read_csv(file, index_col=None)
	all_data_frames.append(data_frame)
data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)

data_frame_concat.to_csv(output_file, index = False)

# 基本过程就是将每个输入文件读取到pandas数据框中，将所有数据框追加到一个数据框列表，然后使用concat 函数将所有数据框连接成一个数据框。
# concat 函数可以使用axis参数来设置连接数据框的方式，axis=0表示从头到尾垂直堆叠，axis=1 表示并排地平行堆叠。

