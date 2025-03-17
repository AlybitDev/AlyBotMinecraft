from javascript import require, On, Once, AsyncTask, once, off

mineflayer = require('mineflayer')

bot = mineflayer.createBot({ 'host': 'server-url/ip', 'port': server-port, 'username': 'bot-username'})

# The spawn event
once(bot, 'login')
bot.chat(pass)

@On(bot, 'chat')
def onChat(this, user, message, *rest):
  print(f'{user} said "{message}"')
  
  if message.startswith('AlyBot'):
    pass

  # If the message contains stop, remove the event listener and stop logging.
  if 'stop' in message:
    off(bot, 'chat', onChat)
