import matplotlib.pyplot as plt
from random_walk import RandomWalk
# ScalarMappable 用于创建映射关系，Normalize 用于规范化数值
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

if __name__ == '__main__':
    # 创建一个RandomWalk实例，并将他包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))

    # Create a ScalarMappable to map values to colors
    # 创建一个ScalarMappable对象，用于将数值映射到颜色
    # 这里使用蓝色色图(cmap=plt.cm.Blues)，并设置归一化对象norm
    # Normalize 类是 Matplotlib 的一部分，用于将数据值归一化到 [0, 1] 范围内。默认情况下，它对数据进行线性缩放。
    # norm = Normalize()
    # 颜色覆盖整个路径
    norm = Normalize(vmin=0, vmax=len(rw.x_values))
    # ScalarMappabl是Matplotlib中的一个对象，用于将数据值与颜色关联起来。
    # 通常用于将一系列数据值映射到一个颜色映射上。
    # cmap = plt.cm.Blues指定要使用的颜色映射。
    # 在这种情况下，是一个蓝色颜色映射。你可以根据需要选择不同的颜色映射。
    # norm = norm设置颜色映射的标准化方式，确保数据值正确映射到颜色映射上。
    sm = ScalarMappable(cmap=plt.cm.Blues, norm=norm)
    # 这一行将一个空数组设置给ScalarMappable对象。
    # 这样做的目的是使用一个空数组初始化ScalarMappable。
    # 稍后，你将使用漫步的点的索引更新这个数组，以获得相应的颜色。
    sm.set_array([])

    # Plotting the gradient line
    for i in range(1, len(rw.x_values)):
        # 通过循环绘制渐变线条，sm.to_rgba(i) 将索引 i 映射为对应颜色
        # rw.x_values[i - 1:i + 1] 和 rw.y_values[i - 1:i + 1] 是当前点和前一个点的坐标，用于定义线段。
        # color = sm.to_rgba(i) 设置线段的颜色。这里使用了ScalarMappable对象的to_rgba方法，将漫步的索引i映射到颜色。由于我们在之前的步骤中已经设置了
        # ScalarMappable的数据数组为空，因此这里i实际上对应于漫步的点的索引。
        plt.plot(rw.x_values[i-1:i+1], rw.y_values[i-1:i+1], linewidth=2, color=sm.to_rgba(i))

    # Adding a colorbar to show the progression
    # 添加颜色条，用于显示漫步的进展。label 参数设置颜色条的标签
    plt.colorbar(sm, label='Walk Progression')

    # Marking the start and end points
    # The scatter plots appear behind the lines. To place them on top of the lines, we can use the zorderargument.
    # Plot elements with higher zorder values are placed on top of elements with lowerzorder values.
    plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=60, zorder=2)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=60, zorder=2)

    # Annotating the start point
    plt.annotate('Start', xy=(rw.x_values[0], rw.y_values[0]), xytext=(20, -20),
                 textcoords='offset points', arrowprops=dict(facecolor='green', arrowstyle='wedge,tail_width=0.5'))

    # Annotating the end point
    plt.annotate('End', xy=(rw.x_values[-1], rw.y_values[-1]), xytext=(-20, 20),
                 textcoords='offset points', arrowprops=dict(facecolor='red', arrowstyle='wedge,tail_width=0.5'))
    #
    # xytext = (rw.x_values[-1] - 50, rw.y_values[-1] - 50)：这一部分指定了注释文本的文本位置，即注释文本离标注点的偏移。
    # 在这里，通过将x和y的坐标都减去50，将文本位置设置在标注点的左上方。
    # 如果你希望注释文本位于其他方向，可以调整这里的偏移值，例如(rw.x_values[-1] + 50, rw.y_values[-1] + 50)就会使得文本位于标注点的右下方
    #
    # textcoords = 'offset points'：这一部分指定了文本坐标的类型，即使用相对于数据点的偏移坐标。
    #
    # arrowprops = dict(facecolor='black', arrowstyle='wedge,tail_width=0.7')：这一部分定义了箭头的属性。
    # facecolor指定箭头的颜色为黑色，arrowstyle指定箭头的样式为楔形，tail_width = 0.7控制箭头的尾巴宽度。

    plt.title('Random Walk', fontsize=24)
    plt.axis('off')

    plt.savefig('plot_rw_visual.png', bbox_inches='tight')
    plt.show()
