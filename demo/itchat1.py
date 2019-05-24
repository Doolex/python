# encoding=utf-8
import itchat

'''
爬点微信数据
'''


def lc():
    print("Finish Login!")


def ec():
    print("exit")


itchat.auto_login(loginCallback=lc, exitCallback=ec)

friends = itchat.get_friends()  # 获取用户信息
rooms = itchat.get_chatrooms()  # 没有获取到全部的群，经测试需要保存到通讯录才能够获取到数据
for friend in rooms:
    itchat.send("test", friend['UserName'])
