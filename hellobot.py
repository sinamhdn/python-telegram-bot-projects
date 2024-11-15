from telegram.ext import Application, MessageHandler, CommandHandler, filters


async def reply(update, context):
    await update.message.reply_text("Hello there!")


def main():
    """
    Handles the initial launch of the program (entry point).
    """
    token = "7899293642:AAFjwQF98uKuUkTqxyH_jOILYbqqNwu1RI0"
    application = Application.builder().token(token).concurrent_updates(
        True).read_timeout(30).write_timeout(30).build()
    application.add_handler(MessageHandler(filters.TEXT, reply))
    application.add_handler(CommandHandler("hello", reply))
    application.add_handler(MessageHandler(
        filters.PHOTO, reply))  # new photo handler here
    print("Telegram Bot started!", flush=True)
    application.run_polling()


if __name__ == '__main__':
    main()
