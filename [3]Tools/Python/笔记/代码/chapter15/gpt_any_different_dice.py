from random import randint
import matplotlib.pyplot as plt
import pygal


class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个骰子数"""
        return randint(1, self.num_sides)


def simulate_dice_rolls(die_1, die_2, num_rolls=50000):
    results_1 = [die_1.roll() for _ in range(num_rolls)]
    results_2 = [die_2.roll() for _ in range(num_rolls)]
    results_sum = [result_1 + result_2 for result_1, result_2 in zip(results_1, results_2)]
    return results_1, results_2, results_sum


def plot_dice_rolls(results_sum):
    plt.plot(results_sum, label='Die 1 + Die 2', color='blue', linestyle='-')
    plt.xlabel('Roll Number')
    plt.ylabel('Die Sum')
    # 添加图例
    plt.legend()    # label
    plt.title('Simulated Dice Rolls')
    plt.show()


def simulate_random_walk(results_sum):
    cumulative_sum = [sum(results_sum[:i + 1]) for i in range(len(results_sum))]
    return cumulative_sum


def plot_random_walk(cumulative_sum):
    plt.plot(cumulative_sum)
    plt.xlabel('Roll Number')
    plt.ylabel('Cumulative Sum')
    plt.title('Random Walk of Rolling Dice')
    plt.show()


def create_pygal_bar_chart(num_sides_1, num_sides_2, frequencies):
    hist = pygal.Bar()
    hist.title = f'Results of rolling a D{num_sides_1} and a D{num_sides_2} 50000 times.'
    hist.x_labels = list(range(2, len(frequencies) + 2))
    hist.x_title = 'Result'
    hist.y_title = 'Frequency of Result'
    hist.add(f'D{num_sides_1} + D{num_sides_2}', frequencies)
    hist.render_to_file('gpt_any_different_dice.svg')


if __name__ == '__main__':
    num_sides_1 = int(input('Please enter the num_sides of the first die: '))
    die_1 = Die(num_sides_1)

    num_sides_2 = int(input('Please enter the num_sides of the second die: '))
    die_2 = Die(num_sides_2)

    results_1, results_2, results_sum = simulate_dice_rolls(die_1, die_2)

    plot_dice_rolls(results_sum)

    cumulative_sum = simulate_random_walk(results_sum)
    plot_random_walk(cumulative_sum)

    frequencies = [results_sum.count(value) for value in range(2, die_1.num_sides + die_2.num_sides + 1)]
    create_pygal_bar_chart(num_sides_1, num_sides_2, frequencies)
