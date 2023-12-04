# CSV文件：一系列以逗号分隔的值
# 文件头格式并非总是一致的，空格和单位可能出现在奇怪的地方，很常见但不会带来任何问题
# 很多的数据集都会缺失数据，数据格式不正确或是数据本身不正确
# 在有些情况下，需要使用continue来跳过一些数据，或是用remove()或del()将已提取数据删除
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f_object:
    reader = csv.reader(f_object)
    head_row = next(reader) # next 返回文件的下一行
    # print(head_row)

    for index, column_header in enumerate(head_row):
        print(index, column_header)

    print('\n')

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            high = int(row[1])
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data!')
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)


    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red')
    plt.plot(dates, lows, c='blue')
    plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.3)

    # 设置图形样式
    plt.title('Daily high and low temperature - 2014.\nDeath Valley, CA', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate() # 绘制斜的日期标签，以防止重叠
    plt.ylabel('Temperature(F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.ylim(10, 120)   # 限制y轴坐标

    plt.show()