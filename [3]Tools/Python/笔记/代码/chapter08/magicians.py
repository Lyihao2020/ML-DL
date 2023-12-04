# 练习

def show_magicians(magicians):
    print('Magicians are as followed.')
    for magician in magicians:
        print(magician)

# def make_great(magicians):
#     # for magician in magicians:
#     #     magician = 'The Great ' + magician
#     #
#     # 函数默认传递的是参数的引用，但在函数内对参数进行赋值不会影响原始列表。
#     # 为了修改原始列表，你可以通过修改传入参数的方式。以下是修正后的代码：
#     # for i in range(len(magicians)):
#     #     magicians[i] = 'The Great ' + magicians[i]
#     current_magicians = []
#     for magician in magicians:
#         current_magicians.append('The Great ' + magician)
#     return current_magicians
#
#
# magicians = ['alex', 'max', 'jenny', 'joe']
# current_magicians = make_great(magicians[:])
# show_magicians(magicians)
# show_magicians(current_magicians)

# def make_great(magicians, current_magicians):
#     for i in range(len(magicians)):
#         magicians[i] = 'the Great ' + magicians[i]
#         current_magicians.append(magicians[i])
#
# current_magicians = []
# magicians = ['alex', 'max', 'jenny', 'joe']
# make_great(magicians[:], current_magicians)
# show_magicians(magicians)
# show_magicians(current_magicians)

# 或者
def make_great(magicians, current_magicians):
    for i in range(len(magicians)):
        magicians[i] = 'the Great ' + magicians[i]
    # current_magicians = magicians
    # current_magicians赋值为magicians的引用，而不是创建一个新的列表。这导致
    # current_magicians和magicians指向相同的列表，因此对magicians的修改也会影响
    # 因为传入的是切片，所以在函数结束时，切片释放，导致current_magicians指向对象也一并被释放
    # 所以需要两者独立，采用切片的形式进行复制
    
    current_magicians[:] = magicians  # 使用切片来复制列表

current_magicians = []
magicians = ['alex', 'max', 'jenny', 'joe']
make_great(magicians[:], current_magicians)
show_magicians(magicians)
show_magicians(current_magicians)

