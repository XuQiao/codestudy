#coding=utf-8
import itchat, time, random
def add_friend_new(userid):
    VerifyContent = ''
    add_msg = itchat.add_friend(userid, status=2, verifyContent=VerifyContent, autoUpdate=True)
    return add_msg

def main():
    msg = add_friend_new('oTqS4jnO2c7CSNnX10P-f_jashvs')
    print msg


if __name__ == "__main__":
    itchat.auto_login(enableCmdQR=2, hotReload=True)
    main()
