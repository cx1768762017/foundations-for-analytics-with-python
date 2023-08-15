#!/usr/bin/env python3
import csv
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        # 创建了列表变量header_list，其中包含了要作为列标题的5 个字符串
        header_list = ['Supplier Name', 'Invoice Number','Part Number', 'Cost', 'Purchase Date']
        # 将这些列表值写入输出文件的第一行
        filewriter.writerow(header_list)
        for row in filereader:
            # 将所有数据行写入输出文件，放在标题行下面
            filewriter.writerow(row)