#coding=utf-8
import itchat, time, random
def get_chatroom(chatroomUserName = '1234567'):
#    itchat.get_chatrooms(update=True)
    chatrooms = itchat.search_chatrooms(chatroomUserName);
    if chatrooms:
        return chatrooms[0]
    else:
        print("Cannot find the chatroom: "+ chatroomUserName)
        return None

def get_newusers(chatroom):
    chatroom = itchat.update_chatroom(chatroom['UserName'])
    newusers = []
    for friend in chatroom['MemberList']:
        #print("friend name is : %s " % (friend['DisplayName'] or friend['NickName']))
        existfriend = itchat.search_friends(userName=friend['UserName'])
        if existfriend is not None:
            print('%s is in the friend list' % (friend['DisplayName'] or friend['NickName']))
            pass
        else:
            newusers.append(friend)
    return newusers

def add_users(chatroom):
    newusers = get_newusers(chatroom)
    #if 'USTC' or u'科大'in chatroom['NickName']:
    #    VerifyContent = u'Hi, I am 徐峤 0804 from %s' % chatroom['NickName']
    #elif u'求职' in chatroom['NickName']:
    #    VerifyContent = 'Hi, I am Qiao Xu 0804 from %s, My LinkedIn address is: https://www.linkedin.com/in/qiao--xu' % chatroom['NickName']
    #else:
    VerifyContent = u'Hi, I am Qiao Xu from %s, 曹教授校友, 现在美国国家实验室' % chatroom['NickName']
    #VerifyContent = u'你好,沃顿论坛小伙伴'
    random.shuffle(newusers) #random shuffle elements
    iadded = 0
    for friend in newusers:
        #if friend['NickName'] != 'test': continue  # a specific name
        add_msg = itchat.add_friend(friend['UserName'], status=2, verifyContent=VerifyContent, autoUpdate=True)
        #print("Adding %s now: %s" % (friend['NickName'], add_msg['BaseResponse']['ErrMsg'].encode('latin-1')))
        try:
            add_msg['BaseResponse']['ErrMsg'].encode('latin-1')
            print("Adding %s now: %s" % (friend['NickName'], add_msg['BaseResponse']['ErrMsg'].encode('latin-1')))
        except:
            print("Adding %s now: %s" % (friend['NickName'], add_msg['BaseResponse']['ErrMsg']))
            pass
        iadded = iadded + 1
        itry = 0
        while add_msg['BaseResponse']['ErrMsg'] != u'请求成功':  # api limitation, only 10 at a time
        #while add_msg['BaseResponse']['ErrMsg'].encode('latin-1') == '操作太频繁，请稍后再试。':  # api limitation, only 10 at a time
            itry = itry + 1
            time.sleep(100)
            add_msg = itchat.add_friend(friend['UserName'], status=2, verifyContent=VerifyContent, autoUpdate=True)
            print('retry %s time' % itry)
        time.sleep(30)
    return iadded

def main():
    #for chatroom in itchat.get_chatrooms(update=True):
    #    print ('%s : %s members' % (chatroom['NickName'], len(chatroom['MemberList'])))

    #chatroom = get_chatroom("")
    #chatroom = get_chatroom(u'琪石朋友圈')
    #chatroom = get_chatroom(u'纳城华人帮')
    #chatroom = get_chatroom('USTC-AAGNY-Summit')
    #chatroom = get_chatroom(u'USTC-GAAG 简历书写\找工作群')
    #chatroom = get_chatroom(u'USTC-GAAG Fintech\区块链群')
    #chatroom = get_chatroom(u'USTC-GAAG 科大学生实习招聘群')
    #chatroom = get_chatroom(u'石溪租房群#2')
    #chatroom = get_chatroom(u'琪石2017高级会员群')
    #chatroom = get_chatroom(u'2017 USTC春节聚会')
    #chatroom = get_chatroom(u'3月4号LICAA义工答谢会')
    chatroom = get_chatroom(u'区块链经济和金融')
    #chatroom = get_chatroom(u'长岛科大人')
    #chatroom = get_chatroom(u'科大纽约校友求职内推群')
    #chatroom = get_chatroom(u'USTC-StonyBrook')
    #chatroom = get_chatroom(u'USTC-ALUM 近代物理系(4系)校友群')
    #chatroom = get_chatroom(u'春季求职Workshop')
    #chatroom = get_chatroom(u'LICAA1群(谢绝商业宣传)')
    #chatroom = get_chatroom(u'大石溪华人家园群')
    #chatroom = get_chatroom(u'LICAA1\u7fa4(\u8c22\u7edd\u5546\u4e1a\u5ba3\u4f20)')
    #chatroom = get_chatroom(u'独立谣一起躁狼嗨')
    #chatroom = get_chatroom(u'\u72ec\u7acb\u8c23\u4e00\u8d77\u8e81\u6d6a\u55e83\u20e3\ufe0f')
    #chatroom = get_chatroom(u'Dr. Colleagues')
    #chatroom = get_chatroom(u'沃顿开心创造群')

#        if not chatroom is None and 'BNL' in chatroom['NickName']:
    print(chatroom['NickName'] + ', Total %s members' % len(chatroom['MemberList']))
    print('adding %d new users' % add_users(chatroom))

    #for chatroom in itchat.get_chatrooms(): #All chatrooms, be careful when using this
    #    print(chatroom['NickName'] + ', Total %s members' % len(chatroom['MemberList']))
    #    print('adding %d new users' % add_users(chatroom))

if __name__ == "__main__":
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    main()
