import matplotlib.pyplot as plt

# plt.scatter(2, 4, s=200): 这行代码使用 scatter 函数创建一个散点图
# 坐标点为 (2, 4)，s=200 指定了散点的大小为200。
plt.scatter(2, 4, s=200)
# 设置图表标题并给坐标轴加上标签
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14): 这行代码设置刻度标记的大小
# 其中 axis='both' 表示设置 x 和 y 轴的刻度
# which='major' 表示设置主要刻度，labelsize=14 表示刻度标签的字体大小为 14。
plt.tick_params(axis='both', which='major', labelsize=14)
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