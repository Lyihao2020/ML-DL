# 在字典中存储列表

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print('You ordered a ' + pizza['crust'] + '-crust pizza ' +
      'with the following toppings.')

for topping in pizza['toppings']:
    print(topping, end='\t')

prompt = "\nPlease enter the ingredients of pizza: "

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(f'We will add {message} to the pizza.')