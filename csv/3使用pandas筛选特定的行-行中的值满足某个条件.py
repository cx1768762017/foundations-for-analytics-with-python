#!/usr/bin/env python3
# pandas 提供了一个loc 函数，可以同时选择特定的行与列。你需要在逗号前面设定行筛选条件，在逗号后面设定列筛选条件。
# 下面的loc 函数中的条件设置为：Supplier Name 列中姓名包含Z，或者Cost 列中的值大于600.0，并且需要所有的列。
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)
data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name']\
.str.contains('Z')) | (data_frame['Cost'] > 600.0), :]

data_frame_value_meets_condition.to_csv(output_file, index=False)