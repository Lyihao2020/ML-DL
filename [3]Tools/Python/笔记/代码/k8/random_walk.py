# 随机漫步：每次行走都完全随机，没有明确方向，结果是由一系列随机决策决定的
from random import choice

import matplotlib.pyplot as plt


class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有漫步都始于[0, 0]
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有的点"""

        # 不断漫步，直到列表到达指定的长度
        while len(self.x_values) < self.num_points:

            # 决定前进的方向以及沿着个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x值与y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

if __name__ == '__main__':
    random_walk = RandomWalk()
    random_walk.fill_walk()

    plt.scatter(random_walk.x_values, random_walk.y_values, c=random_walk.y_values,
                cmap=plt.cm.Reds, edgecolors='none', s=15)

    plt.title('Random Walk', fontsize=24)
    plt.xlabel('Value', fontsize=14)
    plt.ylabel('Value of Random Walk', fontsize=14)

    plt.tick_params(axis='both', which='major', labelsize=14)

    plt.savefig('random_walk.png', bbox_inches='tight')

    plt.show()