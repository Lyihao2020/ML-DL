import pygal

from die import Die

if __name__ == '__main__':

    die_1 = Die(6)
    die_2 = Die(10)

    results = []
    for roll_num in range(50000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # 创建条形图实例
    hist = pygal.Bar()

    hist.title = 'Results of rolling a D6 and a D10 50000 times.'
    hist.x_labels = list(range(2, max_result+1))
    hist.x_title = 'Result'
    hist.y_title = 'Frequency of Result'

    hist.add('D6 + D10', frequencies)
    hist.render_to_file('different_dice.svg')