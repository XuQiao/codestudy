import itchat
itchat.auto_login(enableCmdQR=2, hotReload=True)

itchat.send('Hello, filehelper', toUserName='filehelper')
itchat.send('Hello, Self')
itchat.sleep()
