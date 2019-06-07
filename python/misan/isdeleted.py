#coding=utf-8
import itchat, time
itchat.auto_login(enableCmdQR=2, hotReload=True)
chatroomUserName = '1234567'
chatroom = None
def get_chatroom():
    global chatroom
    if chatroom is None:
        itchat.get_chatrooms(update=True)
        chatrooms = itchat.search_chatrooms(chatroomUserName);
        if chatrooms:
            return chatrooms[0]
        else:
            chatroom = itchat.create_chatroom(itchat.get_friends()[1:4], topic=chatroomUserName)
            if chatroom['BaseResponse']['ErrMsg'] == '':
                chatroom['UserName']=chatroomUserName
                return chatroom
    else:
        return chatroom

def get_friend_status(friend):
    ownAccount = itchat.get_friends(update=True)[0]
    if friend['UserName'] == ownAccount['UserName']:
        return u'Own account'
    elif itchat.search_friends(userName=friend['UserName']) is None:
        return u'Not a friend'
    else:
        room = chatroom or get_chatroom()
        r = itchat.add_member_into_chatroom(room['UserName'], [friend])
#       r = itchat.update_chatroom(chatroom)
        if r['BaseResponse']['ErrMsg'] == u'请求成功':
            if len(r['MemberList']) == 0:
                return u'No member in the chatroom'
            else:
                status = r['MemberList'][0]['MemberStatus']
                itchat.delete_member_from_chatroom(room['UserName'], [friend])
                return { 3: u'该好友已经将你加入黑名单。',
                         4: u'该好友已经将你删除。', }.get(status,u'该好友仍旧与你是好友关系。')
#                if status == 3:
#                    return u'该好友已经将你加入黑名单。'
#                elif status == 4:
#                    return u'该好友已经将你删除。'
#                else:
#                    return get(status) + u'该好友仍旧与你是好友关系。'
        else:
            return r['BaseResponse']['ErrMsg'] + u'无法获取好友状态，预计已经达到接口调用限制'

@itchat.msg_register(itchat.content.CARD)
def get_friend(msg):
    ownAccount = itchat.get_friends(update=True)[0]
    if msg['ToUserName'] != ownAccount['UserName']: return
    friendStatus = get_friend_status(msg['RecommendInfo'])
    itchat.send(friendStatus)

itchat.send('start analysis')
itchat.run()

#onefriend = itchat.search_friends(nickName='Iwen Chia')[0]
#msg = get_friend_status(onefriend)
#print(msg)

#for friend in itchat.get_friends():
#    msg = get_friend_status(friend)
#    print((friend['NickName'] or friend['UserName']) + ': ' + msg)
#itchat.run()
