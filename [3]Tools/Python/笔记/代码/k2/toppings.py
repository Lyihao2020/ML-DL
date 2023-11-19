# 检查特殊元素

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print(f'Adding {requested_topping}.')

print("\nFinished making your pizza!")

print('--------------------------')

# 上述代码存在问题
# 需要确定开始的数组不是空数组

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print('Sorry, we are out of green peppers right now.')
        else:
            print(f'Adding {requested_topping}.')
    print("\nFinished making your pizza!")
else:
    print('Are you sure you want a plain pizza?')

print('--------------------------')

# 面对复杂情况，我们采用两个数组进行测试

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping not in available_toppings:
            print(f'Sorry, we are out of {requested_topping} right now.')
        else:
            print(f'Adding {requested_topping}.')
    print("\nFinished making your pizza!")
else:
    print('Are you sure you want a plain pizza?')

print('--------------------------')