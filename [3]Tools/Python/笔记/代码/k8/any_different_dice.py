# In any_different_dice.py
from matplotlib import pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
import pygal

# Assuming die.py is in the same directory
from die import Die

if __name__ == '__main__':
    num_sides_1 = int(input('Please enter the num_sides of the first die: '))
    die_1 = Die(num_sides_1)

    num_sides_2 = int(input('Please enter the num_sides of the second die: '))
    die_2 = Die(num_sides_2)

    results = []
    results_1 = []
    results_2 = []
    for roll_num in range(1000):
        result_1 = die_1.roll()
        result_2 = die_2.roll()
        results_1.append(int(result_1))
        results_2.append(int(result_2))
        results.append(int(result_1)+int(result_2))

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    norm = Normalize(vmin=0, vmax=1000)
    sm = ScalarMappable(cmap=plt.cm.Blues, norm=norm)
    sm.set_array([])

    for i in range(1, 1000):
        plt.plot(results_1[i - 1:i + 1], results_2[i - 1:i + 1], linewidth=2, color=sm.to_rgba(i))

    plt.colorbar(sm, label='Walk Progression of rolling dice.')

    plt.scatter(results_1[0], results_2[0], c='green', edgecolors='none', s=30)
    plt.scatter(results_1[-1], results_2[-1], c='red', edgecolors='none', s=30)

    plt.annotate('Start', xy=(results_1[0], results_2[0]), xytext=(20, -20),
                 textcoords='offset points', arrowprops=dict(facecolor='green', arrowstyle='wedge,tail_width=0.5'))

    plt.annotate('End', xy=(results_1[-1], results_2[-1]), xytext=(-20, 20),
                 textcoords='offset points', arrowprops=dict(facecolor='red', arrowstyle='wedge, tail_width=0.5'))

    plt.title('Random Walk of rolling dice.', fontsize=24)
    plt.axis('off')

    plt.savefig('any_different.png', bbox_inches='tight')
    plt.show()

    hist = pygal.Bar()

    hist.title = f'Results of rolling a D{num_sides_1} and a D{num_sides_2} 1000 times.'
    hist.x_labels = list(range(2, max_result + 1))
    hist.x_title = 'Result'
    hist.y_title = 'Frequency of Result'

    hist.add(f'D{num_sides_1} + D{num_sides_2}', frequencies)
    hist.render_to_file('any_different_dice.svg')