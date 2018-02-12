import curses #it may be a package to open a new window
from random import randrange, choice
from collections import defaultdict
# first you must import some package
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']#初始化数组的一种方式，里面
# 可以使用for循环初始化
# ord 函数是系统自带的函数，将转换为char
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
actions_dict = dict(zip(letter_codes, actions * 2))
# zip函数是一个合并函数
# a = [1,2,3] b = [4,5,6]
# zip(a,b) = [(1,4), (2,5), (3,6)]

# 定义一个函数来转换用户按键时间
def get_user_action(keyboard):
    char = 'N'
    # 如果用户输入的不是定义的键，一直要求用户输入
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]

# 转换

def transpose(field):
    return [list(row) for row in zip(*field)]
# 翻转
def invert(field):
    return [row[::-1] for row in field]

class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        # 类的初始化函数、相当于定义属性
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0
        self.hightscore = 0
        self.reset()

    def reset(self):
        if self.score > self.hightscore:
            self.hightscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()

    def move(self, direction):
        def move_row_left(row):
            def tighten(row):
                new_row = [i for i in row if i != 0]
