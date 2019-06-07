#coding=utf-8
import itchat, requests
from constants import *
from func import *
from pullfuturekline import *
from pullspotkline import *
from merge_future import *
from merge_spot import *
from classification import *
from model import *
from plot import *

@itchat.msg_register(itchat.content.TEXT)
def get_prob(msg):
    reply = ''
    friend = itchat.search_friends(userName = msg['FromUserName'])
    ownAccount = itchat.get_friends(update=True)[0]
    if friend['UserName'] == ownAccount['UserName']:
        now = datetime.utcnow()
        now = time.mktime(now.timetuple())
        df_future = pd.read_csv('data/btc_usd_full_next_quarter_future.csv','r',delimiter='\t', index_col=None)
        df_spot = pd.read_csv('data/btc_usd_full_spot.csv','r',delimiter='\t', index_col=None)
        price_f = get_price(now, df_future)
        price_s = get_price(now, df_spot)
        if msg['Text'] == u'diff':
            return str(price_f - price_s)
        if msg['Text'] == u'future':
            return str(price_f)
        if msg['Text'] == u'spot':
            return str(price_s)

itchat.auto_login(hotReload=True, enableCmdQR=1)
#itchat.run()
rounds = 4
while True:
    if rounds == 4:
        print '********refit the model*************'
        pullfuturekline()
        pullspotkline()
        merge_spot()
        merge_future()
        classification() 
        rounds = 0
        print '*********long term***********'
        print '********apply the model *************'
        test = model(15)
        print '********plot*************'
        plot(15, True)
        print '************send to itchat*********'
        itchat.send_image('data/figure.png', toUserName='filehelper')
    
    print '*********short term***********'
    print '********apply the model *************'
    test = model(2)
    print '********plot*************'
    plot(2)
    print '************send to itchat*********'
    itchat.send_image('data/figure.png', toUserName='filehelper')
    itchat.send(
            'long '+str(test.iloc[-1]['longposition'])+'\t'+str(test.iloc[-1]['longamount'])+'\n'+
            'short '+str(test.iloc[-1]['shortposition'])+'\t'+str(test.iloc[-1]['shortamount'])+'\n'+
            'liq '+str(test.iloc[-1]['liqbtc'])+'\n'
            'hold '+str(test.iloc[-1]['holdbtc'])+'\n'+
            'btc '+str(test.iloc[-1]['btc_future_back'])+'\n'+
            'money '+str(test.iloc[-1]['fiat_future_back']), toUserName='filehelper')
    rounds += 1
    time.sleep(15*60)

