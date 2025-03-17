from javascript import require, On, Once, AsyncTask, once, off

mineflayer = require('mineflayer')

bot = mineflayer.createBot({ 'host': 'server-url/ip', 'port': server-port, 'username': 'bot-username'})

# The spawn event
once(bot, 'login')
bot.chat(pass)
