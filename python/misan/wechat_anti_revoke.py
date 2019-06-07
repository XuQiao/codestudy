from xml.etree import ElementTree as ETree
from wxpy import *

bot = Bot()

@bot.register(msg_types=NOTE)
def get_revoked(msg):
    revoked = ETree.fromstring(msg.raw['Content']).find('revokemsg')
    if revoked:
        revoked_msg = bot.messages.search(id=int(revoked.find('msgid').text))[0]
        bot.file_helper.send(revoked_msg)

bot.start()