# 字典

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# 如果你射杀了这个外星人，你会获得多少点数
new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points!')

# 添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0['speed'] = 'medium'
print('Original x-position: ' + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] += x_increment
print('New x-position: ' + str(alien_0['x_position']))

# 使用 del 删除键值对，但需要知道字典名和需要删除的键
del alien_0['points']
print(alien_0)
