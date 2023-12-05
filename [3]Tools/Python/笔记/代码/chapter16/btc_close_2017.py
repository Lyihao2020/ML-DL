# coding: utf-8

# ## 16.2 制作收盘价走势图：JSON 格式
# 在本节中，你将下载JSON格式的收盘价数据，并使用`json`模块来处理它们。
# Pygal提供了一个适合初学者使用的绘图工具，可以用它对收盘价数据进行可视化，以探索价格的特征。

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
try:
    # Python 2.x 版本
    from urllib2 import urlopen
except ImportError:
    # Python 3.x 版本
    from urllib.request import urlopen  # 1
import json
import requests
import pygal
import math
from itertools import groupby


json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url)  # 2
# 读取数据
req = response.read()
# 将数据写入文件
with open('btc_close_2017_urllib.json', 'wb') as f:  # 3
    f.write(req)
# 加载json格式
file_urllib = json.loads(req.decode('utf8'))  # 4
print(file_urllib)


json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)  # 1
# 将数据写入文件
with open('btc_close_2017_request.json', 'w') as f:
    f.write(req.text)  # 2, 可以直接读取文件数据，返回格式是字符串
file_requests = req.json()  # 3


print(file_urllib == file_requests)


# 将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)  # 1

# 打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))  # 1
    print("{} is month {} week {}, {}, the close price is {} RMB".format(
        date, month, week, weekday, close))


# 创建5个列表，分别存储日期和收盘价
dates = []
months = []
weeks = []
weekdays = []
close = []
# 每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

# 第一个参数使x标签顺时针旋转20度，第二个参数告诉程序不用显示所有的x轴坐标
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)  # ①
line_chart.title = '收盘价（¥）'
line_chart.x_labels = dates
N = 20  # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]  # ②配置该参数使x轴坐标每隔20天显示一次
# 第一个冒号 : 在第一个 :: 之前表示切片的起始索引。由于未指定（在第一个冒号之前），它默认为列表的开头。
# 第二个冒号 : 在第二个 :: 之后表示切片的结束索引。由于未指定（在第二个冒号之后），它默认为列表的末尾。
# N 在 :: 之后表示步长，也就是在切片中每隔 N 个元素包含一个元素。
line_chart.add('收盘价', close)
line_chart.render_to_file('收盘价折线图（¥）.svg')


line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价对数变换（¥）'
line_chart.x_labels = dates
N = 20  # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]  # ①
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('收盘价对数变换折线图（¥）.svg')
line_chart


# 数据配对和排序： zip(x_data, y_data) 将 x_data 和 y_data 中的元素一一配对，然后 sorted 函数对这些配对进行排序。结果是一个按照 x 值排序的配对列表。
# 分组： groupby 函数按照每个配对的第一个元素（x 值）对排序后的配对进行分组。在循环中，x 是唯一的 x 值，而 y 是一个可迭代的对象，包含相同 x 值的一组配对。
# 提取 Y 值列表： 列表推导式 [v for _, v in y] 用于提取分组中所有的 y 值，形成一个名为 y_list 的列表。
# 计算平均 Y 值： sum(y_list) / len(y_list) 计算 y_list 中所有值的平均值，并将 x 值和平均 y 值的配对 [x, sum(y_list) / len(y_list)] 添加到 xy_map 列表中。
# 解包结果： [*zip(*xy_map)] 将 xy_map 列表解包，分别得到两个元组：x_unique 包含唯一的 x 值，y_mean 包含相应的平均 y 值。
# 首先，zip(*xy_map) 将 xy_map 中的元素进行转置。假设 xy_map 中包含多个内部列表，每个内部列表的第一个元素是 x 值，第二个元素是对应的平均 y 值。
# zip(*xy_map) 将这些内部列表转置，使得第一个元组包含所有 x 值，第二个元组包含所有平均 y 值。
# 然后，[*zip(*xy_map)] 则使用 * 操作符对转置后的元组进行解包。这会将元组中的元素分别解包成一个新的列表。所以，最终的结果是两个列表，一个包含所有 x 值，另一个包含所有平均 y 值。

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):  # 2
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])  # 3
    x_unique, y_mean = [*zip(*xy_map)]  # 4
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart

def generate_html(file_path):
    with open(file_path, 'w', encoding='utf8') as html_file:
        html_file.write(
            '<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
        for svg in [
                '收盘价折线图（¥）.svg', '收盘价对数变换折线图（¥）.svg', '收盘价月日均值（¥）.svg',
                '收盘价周日均值（¥）.svg', '收盘价星期均值（¥）.svg'
        ]:
            html_file.write(
                '    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))  # 1
        html_file.write('</body></html>')

if __name__ == '__main__':
    idx_month = dates.index('2017-12-01')
    line_chart_month = draw_line(
        months[:idx_month], close[:idx_month], '收盘价月日均值（¥）', '月日均值')
    line_chart_month

    idx_week = dates.index('2017-12-11')
    line_chart_week = draw_line(
        weeks[1:idx_week], close[1:idx_week], '收盘价周日均值（¥）', '周日均值')
    line_chart_week

    idx_week = dates.index('2017-12-11')
    wd = ['Monday', 'Tuesday', 'Wednesday',
          'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
    line_chart_weekday = draw_line(
        weekdays_int, close[1:idx_week], '收盘价星期均值（¥）', '星期均值')
    line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    line_chart_weekday.render_to_file('收盘价星期均值（¥）.svg')
    line_chart_weekday

    generate_html('收盘价Dashboard.html')
