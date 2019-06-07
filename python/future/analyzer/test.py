#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import time
from analyzer import constants, pullfuturekline, pullspotkline, merge_future, merge_spot, classification, model, plot, runxgboost


def test(bot, job):
    pullfuturekline()
    pullspotkline()
    merge_spot()
    merge_future()

    if time.time() % 4 > 3:
        bot.send_message(job.context, '********refit the model*************')
        cv_score, f1_score, precision_score = classification()
        cv_score_xgb, f1_score_xgb, precision_score_xgb = runxgboost.run()
        bot.send_message(job.context, text = 'log_loss, f1_score, precision\nRF :' + str([cv_score, f1_score, precision_score]) + '\nXGB :' + str([cv_score_xgb, f1_score_xgb, precision_score_xgb]))
    print '*********long term***********'
    print '********apply the model *************'
    test = model(15)
    print '********plot*************'
    plot(15, True)
    print '************send to telgram*********'
    bot.send_photo(job.context, photo=open('data/figure.png', 'rb'))

    print '*********short term***********'
    print '********apply the model *************'
    #test = model(2)
    print '********plot*************'
    plot(2)
    print '************send to telgram*********'
    bot.send_photo(job.context, photo=open('data/figure.png', 'rb'))
    bot.send_message(job.context, text=
            'long '+str(test.iloc[-1]['longposition'])+'\t'+str(test.iloc[-1]['longamount'])+'\n'+
            'short '+str(test.iloc[-1]['shortposition'])+'\t'+str(test.iloc[-1]['shortamount'])+'\n'+
            'total '+str(test.iloc[-1]['positions'])+'\n'+
            'liq '+str(test.iloc[-1]['liqbtc'])+'\n'
            'hold '+str(test.iloc[-1]['holdbtc'])+'\n'+
            'btc_RF '+str(test.iloc[-1]['btc_future_back_RF'])+'\n'+
            'btc_XGB '+str(test.iloc[-1]['btc_future_back_XGB'])+'\n'+
            'money '+str(test.iloc[-1]['fiat_future_back']))

def backtest(bot, chat_id, startday = -1, endday = 0):
    pullfuturekline()
    pullspotkline()
    merge_spot()
    merge_future()
    cv_score = classification(startday, endday)
    cv_score_xgb = runxgboost.run(startday, endday)
    bot.send_message(chat_id, '********fit the model from '+str(startday)+' to  '+str(endday)+' *************')
    bot.send_message('RF :' + str(cv_score) + ' XGB :' + str(cv_score_xgb))
    test=model(8)
    print '*******************************'
    plot(8)
    bot.send_photo(chat_id, photo=open('data/figure.png', 'rb'))
    bot.send_message(chat_id, text=
            'long '+str(test.iloc[-1]['longposition'])+'\t'+str(test.iloc[-1]['longamount'])+'\n'+
            'short '+str(test.iloc[-1]['shortposition'])+'\t'+str(test.iloc[-1]['shortamount'])+'\n'+
            'total '+str(test.iloc[-1]['positions'])+'\n'+
            'liq '+str(test.iloc[-1]['liqbtc'])+'\n'
            'hold '+str(test.iloc[-1]['holdbtc'])+'\n'+
            'btc_RF '+str(test.iloc[-1]['btc_future_back_RF'])+'\n'+
            'btc_XGB '+str(test.iloc[-1]['btc_future_back_XGB'])+'\n'+
            'money '+str(test.iloc[-1]['fiat_future_back']))
