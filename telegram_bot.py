import telebot
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def send_signal(symbol, position, entry, target1, target2, stop_loss, leverage, pattern):
    message = f"{symbol}\nپوزیشن: {position}\nالگو: {pattern}\n\n" \
              f"نقطه ورود: {entry}\n" \
              f"تارگت 1: {target1}\n" \
              f"تارگت 2: {target2}\n" \
              f"حد ضرر: {stop_loss}\n" \
              f"لورج پیشنهادی: {leverage}"
    
    bot.send_message(TELEGRAM_CHAT_ID, message)
