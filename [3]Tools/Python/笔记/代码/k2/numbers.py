# 创建数值列表

for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

# 列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares)

squares = [value ** 3 for value in range(1, 21, 2)]
print(squares)


