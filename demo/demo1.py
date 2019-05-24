#!/usr/bin/python3
import sys

import demo.demo2
import demo.demo3

# 输出语句
print("hello world!")
print(sys.version)
demo2 = demo.demo2
demo2.func1()
demo.demo3.demo3().say()
demo.demo3.demo4().say()
demo.demo3.demo4().say1()

# 元数据类型 相当于不可该的list
tup1 = ('g', 'g')
print(tup1[1:])


# fuck 代码块和块之间要间隔两行
# 函数
def func(msg):
    print(msg)


# 函数调用
func("hello world")

num = 100


def func2():
    num = 200
    print(num)


func2()
print(num)  # 没有被修改


def func3():
    global num
    num = 300
    print(num)


func3()
print(num)  # 使用global修改了全局变量


# 可变参数列表 不建议使用
def func4(*args):
    result = ''
    for x in args:
        result += x
    return result


