#coding=utf-8
import itchat, requests
@itchat.msg_register('Note')
def redpocket(msg):
    if any(s in msg['Text'] for s in (u'红包', u'转账')):
        return u'谢谢老板!'

itchat.auto_login(hotReload=False, enableCmdQR=2)
itchat.run()
