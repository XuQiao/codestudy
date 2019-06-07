#coding=utf-8
import itchat, time

itchat.auto_login(enableCmdQR=2, hotReload=True)
wish = 'Good afternoon %s'
itchat.get_chatrooms(update=True)

def get_allmembers(chatroomName=''):
    #chatroomName = 'wishgroup'
    chatroom = itchat.get_chatrooms()#name=chatroomName)
#    print chatroom
    for chatrooms in chatroom:
        if u'谢绝' in chatrooms['NickName']:
            print chatrooms
            print chatrooms['NickName'], chatrooms['UserName']
#    if chatroom is None or len(chatroom) == 0:
#        pass
    #    print(u'No chat is found: ' + chatroomName)
'''
    else:
        chatroom = itchat.update_chatroom(chatroom[0]['UserName'])
        for friend in chatroom['MemberList']:
        #    print("friend name is : %s " % (friend['DisplayName'] or friend['NickName']))#, friend['UserName'])
            friend = itchat.search_friends(userName=friend['UserName'])
            if friend is not None:
                pass
         #       print(wish % (friend['DisplayName'] or friend['NickName']))#, friend['UserName'])
            time.sleep(.5)
'''
#get_allmembers(u'Vanderbilt Global')
get_allmembers()
