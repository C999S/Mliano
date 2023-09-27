#!/usr/bin/env python
# -*- coding:h o d e -*-
# ---------------------
# Telegram : @rffr3
# Coded by WESTON
# ---------------------
import telebot,requests
from telebot import types


bot = telebot.TeleBot("6515619759:AAFo1N6g0F-gqAcQ-3v2QENvUGflrScXIU4")

@bot.message_handler(commands=[ 'start' ])
def start(message):
	mark = types.InlineKeyboardMarkup(row_width=1)
	s1 =types.InlineKeyboardButton("• قناة لبوت •",url =f"https://t.me/hwxdw")
	mark.add(s1)			
	bot.send_message(message.chat.id,"""⟠  بوت تحويل نص الى GIF . 
⟠ يمكن تحويل نص بسهوله الى اكثر من شكل.
⟠ فقط قم بإرسال نص ! .
╌ ╌ ╌ ╌ ╌ ╌ ╌ ╌ ╌ ╌""",reply_markup=mark)
 
 
@bot.message_handler(func=lambda message: True)
def Re(message):
	res = requests.get("https://api.codebazan.ir/image/?type=gif&text="+message.text).json()
	for key in res:
		value = res[key]
		try:
			if "https:" in value:
				bot.send_audio(message.chat.id,value,"• Tele : @rffr3 ")
		except:
			pass


bot.infinity_polling()							