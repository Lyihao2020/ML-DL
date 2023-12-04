# In die.py
# Pygal来生成可缩放的矢量图形文件，他们会自动缩放，以适应观看者的屏幕
from random import randint

class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个骰子数"""
        return str(randint(1, self.num_sides))