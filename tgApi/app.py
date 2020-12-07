from aiogram.utils import executor
import logging
from tgApi.db import table123

from tgApi.hendlers import WokrWithHandler
a = WokrWithHandler(table123)
dp = a.getDP()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
