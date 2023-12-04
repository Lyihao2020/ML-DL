import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# plt.plot(squares, linewidth=5)
plt.plot(input_value, squares, linewidth=5)

# 设置图标标题，并给坐标轴加上标签
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=24)
plt.ylabel('Square of Value', fontsize=24)

# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)
plt.show()
