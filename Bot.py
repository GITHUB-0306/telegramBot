import telepot
token = '1175553984:AAGlWJ2U-uqa219Yhaovj2VID0Bsfs-VzbM'
bot = telepot.Bot(token)
print (bot.getMe())
def handle(msg):
    content_type, chat_type, chat_id= telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if (content_type =='text'):
        
        bot.sendMessage(chat_id, "you said'{}'".format(msg["text"]))
    
bot.message_loop(handle)
