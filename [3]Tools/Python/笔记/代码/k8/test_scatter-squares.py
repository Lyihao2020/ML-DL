# 练习
import  matplotlib.pyplot as plt

# x_values = list(range(1, 6))
# y_values = [x**3 for x in x_values]

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 5000, 0, 125000000000])

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds,
            edgecolors='none', s=40)

plt.savefig('test_squares_plot.png', bbox_inches='tight')
plt.show()