import pygal
from die import Die

if __name__ == '__main__':
    die_1 = Die()
    die_2 = Die()

    results = []
    # for roll_num in range(1000):
    #     result = die_1.roll() + die_2.roll()
    #     results.append(result)
    results = [int(die_1.roll()) + int(die_2.roll()) for roll_num in range(1000)]

    # 分析结果
    # frequencies = []
    # max_result = die_1.num_sides + die_2.num_sides
    # for value in range(2, max_result+1):
    #     frequency = results.count(value)
    #     frequencies.append(frequency)

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    frequencies = [results.count(value) for value in range(2, max_result+1)]

    # Make some rolls, and store results in a list.
    # results = [die.roll() for roll_num in range(1000)]

    # Analyze the results.
    # frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

    # 对结果进行可视化
    hist = pygal.Bar()  # 创建条形图实例

    hist.title = 'Results of rolling two D6s 1000 times'
    hist.x_labels = list(range(2, max_result+1))
    hist.x_title = 'Result'
    hist.y_title = 'Frequency of Result'

    # 将一系列值添加到图表中，并给添加的值指定的标签
    hist.add('Dx + Dy', frequencies)
    hist.render_to_file('dice_visual.svg')   # 生成的图表具有交互性