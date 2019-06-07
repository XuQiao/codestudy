#coding=utf-8
import itchat, requests
key = '8edce3ce905a4c1dbb965e6b35c3834d'
def get_response(msg):
# Turing response
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key' : key,
        'info' : msg,
        'usedid' : 'wechat-robot',
        }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received ' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply

itchat.auto_login(hotReload=True, enableCmdQR=2)
itchat.run()
