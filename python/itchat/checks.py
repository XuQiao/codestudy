# needs, interesting applications
# given a friend, check what groups this friend are in
# given a group, check what friends are in a group
# check if two friends are mutual friends
# give a sticker to friends from special group
#coding=utf-8
import itchat, time, random
import pandas as pd

def findgroups(friendname):
    chatrooms = itchat.get_chatrooms(update=True)
#    chatrooms = itchat.search_chatrooms(chatroomUserName);
#    chatrooms = pd.DataFrame(chatrooms)
    #print(chatrooms.iloc[0])
    if chatrooms is not None:
       # print chatrooms
        pass
    else:
        print("Cannot find the chatroom: ")
        return None
    friends = itchat.search_friends(name=friendname, userName=None, remarkName=None, nickName=None,wechatAccount=None)
    for friend in friends:
        for chatroom in chatrooms:
            print chatroom
            if friend in chatroom['self']:
                print 'friend ' + friend['username'] + ' is in ' + chatroom['username']
    print friend

def findfriends(group):
    pass

def checkmutual(friendA, friendB):
    pass

def sticker(group):
    pass

def main():
    findgroups('Grace')

if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    main()
