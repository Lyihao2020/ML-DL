# 练习

alien_color = 'red'
score = 0

if alien_color == 'green':
    score = 5
    print(score)
elif alien_color == 'yellow':
    score = 10
    print(score)
elif alien_color == 'red':
    score = 15
    print(score)
else:
    print('Invalid input!')

print('--------------------------')

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'red', 'points': 10}
alien_2 = {'color': 'yellow', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print('--------------------------')

aliens = []

"""代码错误，重复引用了同一个对象，导致一更改全部一起更改
new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
for alien_number in range(30):
    aliens.append(new_alien)
"""
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

"""或者也可以
import copy

aliens = []

new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
for alien_number in range(30):
    aliens.append(copy.copy(new_alien))

# ... 其余的代码保持不变

aliens = []

new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
for alien_number in range(30):
    aliens.append(new_alien.copy())

# ... 其余的代码保持不变

"""

for alien in aliens[:]:
    print(alien)
print('...')

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 15
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)
print('.....')

print('Total number of aliens: ' + str(len(aliens)))

print('--------------------------')



