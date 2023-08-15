import random

# 生成100个7到12的随机数
numbers = [random.randint(7, 12) for _ in range(100)]

# 统计每个数的数量
count_dict = {}
for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# 打印结果
for num, count in count_dict.items():
    print(f"数值 {num} 出现次数为 {count} 次")
