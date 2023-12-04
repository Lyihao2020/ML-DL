# 作业练习

sandwich_orders = ['pastrami', 'BLT Sandwich', 'pastrami', 'Club Sandwich', 'pastrami', 'Reuben Sandwich', 'Ham and Cheese Sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f'I made you {current_sandwich}.')
    finished_sandwiches.append(current_sandwich)

print('\nThese sandwiches are finished.')
for finished_sandwich in finished_sandwiches:
    print(f'\t{finished_sandwich}')

print('\nPastrami is sold out.')
while 'pastrami' in finished_sandwiches:
    finished_sandwiches.remove('pastrami')

print(finished_sandwiches)

