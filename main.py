from aiogram import Bot, Dispatcher, executor, types
from aiohttp.client_exceptions import ClientOSError, ClientConnectorError
from asyncio.exceptions import TimeoutError
from aiogram.utils.exceptions import MessageToDeleteNotFound, MessageCantBeDeleted, TelegramAPIError, NetworkError, RetryAfter
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import TOKEN, admin


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=["start", "update"])
async def start(message: types.Message):
    
    await message.answer(text= "Добро пожаловать в Бот-Блокнот!", reply_markup= )


@dp.message_handler()
async def del_text(message: types.Message):
    
    await message.delete()
    
@dp.errors_handler(exception=TimeoutError)
async def error_oserror(update: types.Update, exception: TimeoutError):
    
    if isinstance(exception, TimeoutError):
        IGNORE_ERRNO = {
            10038,
            121,
        }
    
    return True

@dp.errors_handler(exception=OSError)
async def error_oserror(update: types.Update, exception: OSError):
    
    if isinstance(exception, OSError):
        IGNORE_ERRNO = {
            10038,
            121,
        }
    
    return True

@dp.errors_handler(exception=NetworkError)
async def error_oserror(update: types.Update, exception: NetworkError):
        
    if isinstance(exception, NetworkError):
        IGNORE_ERRNO = {
            10038,
            121,
        }
        
    return True

@dp.errors_handler(exception=TelegramAPIError)
async def error_oserror(update: types.Update, exception: TelegramAPIError):
    
    if isinstance(exception, TelegramAPIError):
        IGNORE_ERRNO = {
            10038,
            121,
        }
        
    return True

@dp.errors_handler(exception=ClientOSError)
async def error_oserror(update: types.Update, exception: ClientOSError):
    
    if isinstance(exception, TelegramAPIError):
        IGNORE_ERRNO = {
            10038,
            121,
        }
        
    return True

@dp.errors_handler(exception=ClientConnectorError)
async def error_oserror(update: types.Update, exception: ClientConnectorError):  
    
    if isinstance(exception, TelegramAPIError):
        IGNORE_ERRNO = {
            10038,
            121,
        }
        
    return True

@dp.errors_handler(exception=RetryAfter)
async def exception_handler(message: types.Message, update: types.Update, exception: RetryAfter):
    
    await bot.send_message(message.chat.id, text="Не флудите!")
    
    return True

if __name__ == "__main__":
    
    executor.start_polling(dp, skip_updates=True)