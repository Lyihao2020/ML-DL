import pygal

from die import Die

if __name__ == '__main__':

    die_1 = Die(6)
    die_2 = Die(6)
    die_3 = Die(6)

    results = []
    for roll_num in range(50000):
        result = die_1.roll() + die_2.roll() + die_3.roll()
        results.append(result)

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
    for value in range(3, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)

    hist = pygal.Bar()

    hist.title = 'Results of rolling three D6 50000 times.'
    hist.x_labels = list(range(3, max_result+1))
    hist.x_title = 'Result'
    hist.y_title = 'Frequency of Result'

    hist.add('Three D6', frequencies)
    hist.render_to_file('three_dice.svg')