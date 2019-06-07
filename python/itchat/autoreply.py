#coding=utf-8
import itchat, requests

@itchat.msg_register(itchat.content.TEXT)
def reply(msg):
    reply = msg['Text']
    friend = itchat.search_friends(userName = msg['FromUserName'])
    ownAccount = itchat.get_friends(update=True)[0]
    if friend['UserName'] == ownAccount['UserName']:
        return u'Own account'
    elif friend is None:
        return u'Not a friend'
    return reply # or defaultReply


itchat.auto_login(hotReload=True, enableCmdQR=0)
itchat.run()
