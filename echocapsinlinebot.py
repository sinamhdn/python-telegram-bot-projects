import os
import logging
from uuid import uuid4
from dotenv import load_dotenv
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, InlineQueryHandler, filters

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='I\'m a bot, please talk to me!')


async def caps_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def echo_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def unknown_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


async def inline_caps_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=str(uuid4()),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)


if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('TOKEN')).build()
    application.add_handler(CommandHandler('start', start_command_handler))
    application.add_handler(CommandHandler('caps', caps_command_handler))
    application.add_handler(MessageHandler(
        filters.TEXT & ~(filters.COMMAND), echo_message_handler))
    application.add_handler(InlineQueryHandler(inline_caps_message_handler))
    application.add_handler(MessageHandler(
        filters.COMMAND, unknown_message_handler))
    application.run_polling()
