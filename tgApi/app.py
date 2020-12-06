from aiogram.utils import executor
import logging

from tgApi.hendlers import dp

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
