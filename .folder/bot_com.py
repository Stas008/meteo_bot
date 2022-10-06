
from pygismeteo import Gismeteo
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


gismeteo = Gismeteo()
def get_weather(input_city):
    search_results = gismeteo.search.by_query(input_city)
    city_id = search_results[0].id
    current = gismeteo.current.by_id(city_id)
    temper=str(current.temperature.air.c)
    descrip=str(current.description)
    res=f'Температура в городе {input_city} = {temper}, {descrip[6:-1]}'
    return(res)
    

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Для того чтобы узнать погоду введите /weather Город')

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    print(msg[9:])
    await update.message.reply_text(get_weather(msg[9:]))
