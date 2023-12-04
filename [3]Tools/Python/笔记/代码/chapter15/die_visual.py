import pygal
from die import Die

if __name__ == '__main__':
    die = Die()

    results = []
    for roll_num in range(1000):
        result = die.roll()
        results.append(result)

    # 分析结果
    frequencies = []
    for value in range(1, die.num_sides+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    print(frequencies)

    # 对结果进行可视化
    hist = pygal.Bar()  # 创建条形图实例

    hist.title = 'Results of rolling one D6 1000 times'
    hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.x_title = 'Result'
    hist.y_title = 'Frequency of Result'

    # 将一系列值添加到图表中，并给添加的值指定的标签
    hist.add('D6', frequencies)
    hist.render_to_file('die_visual.svg')   # 生成的图表具有交互性