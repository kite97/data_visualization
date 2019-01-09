# coding=gbk

import pygal

from die import Die

# 创建两个D6骰子
die_1 = Die()
die_2 = Die()

# 掷骰子多次，并将结果存储到一个列表中
results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]

# 分析结果
labels = []
for value1 in range(1,die_1.num_sides+1):
    for value2 in range(1,die_2.num_sides+1):
        labels.append(value1 * value2)
labels = list(set(labels))
labels.sort()
frequencies = [results.count(value) for value in labels]

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [str(value) for value in labels]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 * D6', frequencies)
hist.render_to_file('dice_visual.svg')
