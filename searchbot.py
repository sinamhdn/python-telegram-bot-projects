import os
import re
import logging
from dotenv import load_dotenv
from urllib.request import urlopen
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Search anything...')


async def result_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    page = urlopen("http://olympus.realpython.org/profiles/aphrodite")
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    title_index = html.find("<title>")
    start_index = title_index + len("<title>")
    end_index = html.find("</title>")
    title = html[start_index:end_index]
    await context.bot.send_message(chat_id=update.effective_chat.id, text='ٍExtract Data With String Handling\n<title>StringStartIndex --> {}\nTitleStartIndex --> {}\n</title>StraingStartIndex --> {}\nSiteTitle --> {}'.format(title_index, start_index, end_index, title))
    url = "http://olympus.realpython.org/profiles/poseidon"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    start_index = html.find("<title>") + len("<title>")
    end_index = html.find("</title>")
    title = html[start_index:end_index]
    await context.bot.send_message(chat_id=update.effective_chat.id, text='ٍExtract Data With String Handling Not Always Accurate\n<title>StringStartIndex --> {}\nTitleStartIndex --> {}\n</title>StraingStartIndex --> {}\nSiteTitle --> {}'.format(title_index, start_index, end_index, title))
    url = "http://olympus.realpython.org/profiles/dionysus"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    pattern = "<title.*?>.*?</title.*?>"
    match_results = re.search(pattern, html, re.IGNORECASE)
    title = match_results.group()
    title = re.sub("<.*?>", "", title)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='ٍExtract Page Title with Regular Expression: '.format(title))
    url = "http://olympus.realpython.org/profiles/dionysus"
    html_page = urlopen(url)
    html_text = html_page.read().decode("utf-8")
    for string in ["Name: ", "Favorite Color:"]:
        string_start_idx = html_text.find(string)
        text_start_idx = string_start_idx + len(string)
        next_html_tag_offset = html_text[text_start_idx:].find("<")
        text_end_idx = text_start_idx + next_html_tag_offset
        raw_text = html_text[text_start_idx: text_end_idx]
        clean_text = raw_text.strip(" \r\n\t")
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Scrape Data From A Website <--> clean data <--> {}'.format(clean_text))

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('TOKEN')).build()
    application.add_handler(CommandHandler('start', start_command_handler))
    application.add_handler(MessageHandler(
        filters.TEXT & ~(filters.COMMAND), result_message_handler))
    application.run_polling()
