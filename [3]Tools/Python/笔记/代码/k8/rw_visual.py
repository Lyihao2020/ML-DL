# 模拟多次随机漫步

import matplotlib.pyplot as plt
from random_walk import RandomWalk

if __name__ == '__main__':
    # 只要程序处于活跃状态，就不断地模拟随机漫步
    while True:
        # 创建一个新的图形对象
        plt.figure()

        # 创建一个RandomWalk实例，并将他包含的点都绘制出来
        rw = RandomWalk()
        rw.fill_walk()

        point_numbers = list(range(rw.num_points))
        plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                    cmap=plt.cm.Blues, edgecolors='none', s=15)

        # 重新绘制起点和终点
        plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=30)
        plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=30)

        plt.title('Random Walk', fontsize=24)
        # plt.xlabel('Value', fontsize=14)
        # plt.ylabel('Value of Random Walk', fontsize=14)

        # plt.tick_params(axis='both', which='major', labelsize=14)

        # 隐藏坐标轴
        plt.axis('off')

        # 显示图形
        plt.show()

        # 保存图片:第一个参数设置文件名，文件将存储到该程序所在目录，第二个指将图标多余的空白裁减掉，如果要保留空白，可省略这个参数
        plt.savefig('rw_visual.png', bbox_inches='tight')

        keep_running = input('Make another walk? (y/n): ')
        if keep_running == 'n':
            break
