#!/usr/bin/env python3
# coding: utf-8

import logging

from wxpy import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

bot = Bot('bot.pkl', console_qr=-2)
if bot.self.nick_name == '游否':
    raise ValueError('Wrong User!')

group = ensure_one(bot.groups().search('wxpy 交流群'))
tuling = Tuling()


def valid(msg):
    return 'wxpy' in msg.text.lower()


def invite(user):
    if user in group:
        logger.info('{} is already in {}'.format(user, group))
        user.send('你已经加入 {} 啦'.format(group.nick_name))
    else:
        logger.info('inviting {} to {}'.format(user, group))
        group.add_members(user, use_invitation=True)


@bot.register(msg_types=FRIENDS)
def new_friends(msg):
    user = msg.card.accept()
    if valid(msg):
        invite(user)
    else:
        user.send('你忘了写加群口令啦，快回去看看口令是啥~')


@bot.register(Friend, msg_types=TEXT)
def exist_friends(msg):
    if valid(msg):
        invite(msg.sender)
    else:
        tuling.do_reply(msg)


bot.start(False)
embed()
