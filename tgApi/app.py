from aiogram.utils import executor
import logging
from mechanic.table import Table
from tgApi.hendlers import WokrWithHandler

dp = WokrWithHandler(Table()).getDP()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
