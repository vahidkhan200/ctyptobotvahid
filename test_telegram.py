from telegram_bot import send_telegram_message

if __name__ == "__main__":
    response = send_telegram_message("سلام! این یه پیام تستیه.")
    print(response)
