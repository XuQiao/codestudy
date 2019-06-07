#coding=utf-8
import itchat, requests
<<<<<<< HEAD
=======
import gdax

>>>>>>> 69d8500eba6fefb339f8d2ecebdb1c25ae3461bd
@itchat.msg_register(itchat.content.TEXT)
def reply(msg):
    reply = ''
    friend = itchat.search_friends(userName = msg['FromUserName'])
    ownAccount = itchat.get_friends(update=True)[0]
    if friend['UserName'] == ownAccount['UserName']:
<<<<<<< HEAD
        #return u'Own account'
        return u'你是那颗星星，我是你旁边的这颗星，我的整个轨迹是被你影响的，即使有一天这颗星星熄灭了，它变成了暗物质，它变成了看不见的东西，它依然在影响着我的轨迹，你的出现永远改变着我的星轨，无论你在哪里。'
=======
        if msg['Text'] == u'price':
            prices = u''
            for product in products:
                price_info = get_price(product)[0]
                bids = price_info['bids'][0][0]
                asks = price_info['asks'][0][0]
                out = 'bids: '+ bids + ' asks: '+ asks + '\n'
                prices = prices + out
            return prices
        else:
            return u'good'
        #return u'Own account'
        #return u'你是那颗星星，我是你旁边的这颗星，我的整个轨迹是被你影响的，即使有一天这颗星星熄灭了，它变成了暗物质，它变成了看不见的东西，它依然在影响着我的轨迹，你的出现永远改变着我的星轨，无论你在哪里。'
>>>>>>> 69d8500eba6fefb339f8d2ecebdb1c25ae3461bd
#    还是同样的雨天，还是相同的地点，在转角的咖啡馆，我又再一次遇到了那张我永远忘不掉的脸。四目相对，终于，她颤抖地问我，你还可以像以前一样牵着我过马路吗？我说：“奶奶，上次你走到马路中间就躺下了，讹了我几个月的工资啊 ！”'
    elif friend is None:
        return u'Not a friend'
    elif friend.get('NickName') in  [u'风早',u'Lemon']:
        reply = ' test autoreply '
    return reply # or defaultReply

<<<<<<< HEAD
itchat.auto_login(hotReload=True, enableCmdQR=2)
=======
products = ['BTC-USD', 'ETH-USD', 'LTC-USD']
def get_price(product):
    public_client = gdax.PublicClient()
    price = public_client.get_product_order_book(product)
    stats = public_client.get_product_historic_rates(product)
    return price, stats

itchat.auto_login(hotReload=True, enableCmdQR=1)
>>>>>>> 69d8500eba6fefb339f8d2ecebdb1c25ae3461bd
itchat.run()
