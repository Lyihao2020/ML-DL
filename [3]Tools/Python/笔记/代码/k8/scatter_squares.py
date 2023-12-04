import matplotlib.pyplot as plt

# plt.scatter(2, 4, s=200): 这行代码使用 scatter 函数创建一个散点图
# 坐标点为 (2, 4)，s=200 指定了散点的大小为200。
# plt.scatter(2, 4, s=200)

# 使用plt.scatter绘制一系列的点
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=100)

# 自动计算数据
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, s=40)   # 蓝色点和黑色轮廓
# 删除数据点的轮廓
# plt.scatter(x_values, y_values, edgecolors='none', s=40)
# plt.scatter(x_values, y_values, color='red', edgecolors='none', s=40)
# 或者使用RGB模式来标记颜色：其中包含三个0-1之间的小数值，分别代表红色，绿色，蓝色分量，越接近0，颜色越深，越接近1，颜色越浅
# plt.scatter(x_values, y_values, color=(0, 0, 0.8), edgecolors='none', s=40)
# colors = [(0, 0, 0.8)] * len(x_values)  # 创建一个包含相同颜色值的列表
# plt.scatter(x_values, y_values, c=colors, edgecolors='none', s=40)

# 颜色映射：一系列颜色，从起始颜色渐变到结束颜色
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# c值设置为了一个y值列表，cmap告诉他用什么颜色映射，将y值较小设置为浅蓝色，y值较大设置为深蓝色
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolors='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14): 这行代码设置刻度标记的大小
# 其中 axis='both' 表示设置 x 和 y 轴的刻度
# which='major' 表示设置主要刻度，labelsize=14 表示刻度标签的字体大小为 14。
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
# plt.axis([0, 1100, 0, 1100000])

# 保存的文件是一片空白的原因可能是由于 plt.savefig 被放置在 plt.show() 之后。
# plt.show() 会显示图形窗口，然后程序会等待用户关闭图形窗口后再继续执行。
# 因此，如果 plt.savefig 在 plt.show() 之后执行，保存的是空白图，因为图形窗口已经关闭。
# 保存图片:第一个参数设置文件名，文件将存储到该程序所在目录，第二个指将图标多余的空白裁减掉，如果要保留空白，可省略这个参数
plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()


"""
在 Matplotlib 中，轴上的刻度可以分为两种类型：主要刻度和次要刻度。
主要刻度是相对较长的刻度，通常用于标识轴上的主要数据点。次要刻度则相对较短，用于标识轴上的次要数据点。

在 `plt.tick_params` 
函数中，`which` 参数用于指定要设置的刻度类型。
具体来说，`which='major'` 表示设置主要刻度的参数。
这就意味着在 `plt.tick_params` 中设置的参数（比如 `labelsize=14`）将应用于轴上的主要刻度标签和刻度线。

示例代码中的这一行：

```python
plt.tick_params(axis='both', which='major', labelsize=14)
```

表明设置 x 轴和 y 轴上的主要刻度，其中刻度标签的字体大小被设置为 14。
 这有助于调整图表的外观，使刻度标签更易读。如果你想调整次要刻度的参数，可以将 `which` 参数设置为 `'minor'`。例如：

```python
plt.tick_params(axis='both', which='minor', labelsize=10)
```

这将设置轴上的次要刻度标签的字体大小为 10。
"""