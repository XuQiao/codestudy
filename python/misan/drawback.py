#coding=utf-8
import itchat, re, time, os, shutil
from itchat.content import *
from prettytable import PrettyTable

msg_list = []

def ClearTimeOutMsg():
    for msg in msg_list:
        if time.time() - msg.get('msg_time') > 130.0:
            if msg.get('msg_type') == 'Picture' \
                    or msg.get('msg_type') == 'Recording' \
                    or msg.get('msg_type') == 'Video' \
                    or msg.get('msg_type') == 'Attachment':
                print(u'要删除的文件: ',msg.get('msg_content'))
                os.remove(msg['msg_content'])
            msg_list.remove(msg)

@itchat.msg_register([TEXT, PICTURE, MAP, CARD, SHARING, RECORDING, ATTACHMENT, VIDEO, FRIENDS], isGroupChat = False)
def Revocation(msg):
    mytime = time.localtime()
    msg_time_touser = mytime.tm_year.__str__() \
            + '/' + mytime.tm_mon.__str__() \
            + '/' + mytime.tm_mday.__str__() \
            + ' ' + mytime.tm_hour.__str__() \
            + ':' + mytime.tm_min.__str__() \
            + ':' + mytime.tm_sec.__str__()
    print("msg_time_touser = %s" % msg_time_touser)
    msg_id = msg['MsgId']
    msg_time = msg['CreateTime']
    msg_from = itchat.search_friends(userName=msg['FromUserName']).get('NickName')
    msg_type = msg['Type']
    msg_content = None
    msg_url = None
    
    if msg_type == 'Text' or msg_type == 'Friends':
        msg_content = msg['Text']
    elif msg_type == 'Picture' or msg_type == 'Recording' or msg_type == 'Attachment' or msg_type == 'Video':
        msg_content = msg['FileName']
        msg['Text'](msg['FileName'])
    elif msg_type == 'Card':
        msg_content = msg['RecommendInfo']['NickName'] + u'的名片'
    elif msg_type == 'Map':
        x, y, location = re.search('<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*', msg['OriContent']).group(1, 2, 3)

        if location is None:
            msg_content = u'纬度->' + x.__str__() + u'经度->' + y.__str__()
        else:
            msg_content = u'' + location
    elif msg_type == 'Sharing':
        msg_content = msg['Text']
        msg_url = msg['Url']
    
    msg_dict = {'msg_id': msg_id, 'msg_type': msg_type, 'msg_from': msg_from, 'msg_time': msg_time, 'msg_time_touser': msg_time_touser, 'msg_content': msg_content, 'msg_url': msg_url}
    msg_list.append(msg_dict)
    print('msg_list saved is: ')
    print(msg_list)
    ClearTimeOutMsg()

@itchat.msg_register([TEXT, PICTURE, MAP, CARD, SHARING, RECORDING, ATTACHMENT, VIDEO, FRIENDS], isGroupChat = True)
def Revocation(msg):
    mytime = time.localtime()
    msg_time_touser = mytime.tm_year.__str__() \
            + '/' + mytime.tm_mon.__str__() \
            + '/' + mytime.tm_mday.__str__() \
            + ' ' + mytime.tm_hour.__str__() \
            + ':' + mytime.tm_min.__str__() \
            + ':' + mytime.tm_sec.__str__()
    print("msg_time_touser = %s" % msg_time_touser)
    msg_id = msg['MsgId']
    msg_time = msg['CreateTime']
    chatroom = itchat.search_chatrooms(userName=msg['FromUserName'])
    msg_chatfrom = None
    if chatroom: msg_chatfrom = chatroom.get('NickName')
    msg_from = msg['ActualNickName']
    msg_type = msg['Type']
    msg_content = None
    msg_url = None
    
    if msg_type == 'Text' or msg_type == 'Friends':
        msg_content = msg['Text']
    elif msg_type == 'Picture' or msg_type == 'Recording' or msg_type == 'Attachment' or msg_type == 'Video':
        msg_content = msg['FileName']
        msg['Text'](msg['FileName'])
    elif msg_type == 'Card':
        msg_content = msg['RecommendInfo']['NickName'] + u'的名片'
    elif msg_type == 'Map':
        x, y, location = re.search('<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*', msg['OriContent']).group(1, 2, 3)

        if location is None:
            msg_content = u'纬度->' + x.__str__() + u'经度->' + y.__str__()
        else:
            msg_content = u'' + location
    elif msg_type == 'Sharing':
        msg_content = msg['Text']
        msg_url = msg['Url']
    
    msg_dict = {'msg_id': msg_id, 'msg_type': msg_type, 'msg_chatfrom': msg_chatfrom, 'msg_from': msg_from, 'msg_time': msg_time, 'msg_time_touser': msg_time_touser, 'msg_content': msg_content, 'msg_url': msg_url}
    msg_list.append(msg_dict)
    print('msg_list saved is ')
    print(msg_list)
    ClearTimeOutMsg()

@itchat.msg_register(NOTE, isGroupChat = True)
def SaveMsg(msg):
    if not os.path.exists('.\\Revocation\\'):
        os.mkdir('.\\Revocation\\')
#    if re.search(r'\<replacemsg\>\<\!\[CDATA\[.*撤回了一条消息\]\]\>\<\/replacemsg\>', msg['Content']):
    if re.search(r'revokemsg', msg['Content']):
        old_msg_id = re.search('\<msgid\>(.*?)\<\/msgid\>', msg['Content']).group(1)
        old_msg = next((msg for msg in msg_list if msg['msg_id'] == old_msg_id),None)
        if old_msg:
            msg_send = u"您的好友：" \
                       + old_msg.get('msg_from', None) \
                       + u"  在 [" + old_msg.get('msg_time_touser', None) \
                       + u"] 在 [" + old_msg.get('msg_chatfrom',None) \
                       + u"], 撤回了一条 [" + old_msg['msg_type'] \
                       + u"] 消息, 内容如下:" \
                       + old_msg.get('msg_content', None)
            if old_msg['msg_type'] == "Sharing":
                msg_send += r", 链接: " + old_msg.get('msg_url', None)
            elif old_msg['msg_type'] == 'Picture' \
                    or old_msg['msg_type'] == 'Recording' \
                    or old_msg['msg_type'] == 'Video' \
                    or old_msg['msg_type'] == 'Attachment':
                msg_send += u", 存储在当前目录下Revocation文件夹中"
                shutil.move(old_msg['msg_content'], '.\\Revocation\\')
            print(msg_send)
            itchat.send(msg_send, toUserName='filehelper')

            msg_list.remove(old_msg)
            print('msg_list saved is ')
            print(msg_list)
#        ClearTimeOutMsg()

@itchat.msg_register(NOTE, isGroupChat = False)
def SaveMsg(msg):
    if not os.path.exists('.\\Revocation\\'):
        os.mkdir('.\\Revocation\\')
#    if re.search(r'\<replacemsg\>\<\!\[CDATA\[.*撤回了一条消息\]\]\>\<\/replacemsg\>', msg['Content']):
    if re.search(r'revokemsg', msg['Content']):
        old_msg_id = re.search('\<msgid\>(.*?)\<\/msgid\>', msg['Content']).group(1)
        old_msg = next((msg for msg in msg_list if msg['msg_id'] == old_msg_id),None)
        if old_msg:
            msg_send = u"您的好友：" \
                       + old_msg.get('msg_from', None) \
                       + u"  在 [" + old_msg.get('msg_time_touser', None) \
                       + u"], 撤回了一条 [" + old_msg['msg_type'] \
                       + u"] 消息, 内容如下:" \
                       + old_msg.get('msg_content', None)
            if old_msg['msg_type'] == "Sharing":
                msg_send += r", 链接: " + old_msg.get('msg_url', None)
            elif old_msg['msg_type'] == 'Picture' \
                    or old_msg['msg_type'] == 'Recording' \
                    or old_msg['msg_type'] == 'Video' \
                    or old_msg['msg_type'] == 'Attachment':
                msg_send += u", 存储在当前目录下Revocation文件夹中"
                shutil.move(old_msg['msg_content'], '.\\Revocation\\')
            print(msg_send)
            itchat.send(msg_send, toUserName='filehelper')

            msg_list.remove(old_msg)
            print('msg_list saved is ')
            print(msg_list)
#        ClearTimeOutMsg()

if __name__ == '__main__':
    itchat.auto_login(hotReload=True, enableCmdQR=2)
    itchat.run()
