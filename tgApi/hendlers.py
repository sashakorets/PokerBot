from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery
from tgApi.config import dp, bot
from tgApi.default_key import *
from tgApi.inline_key import *
from mechanic.player import Player
from DB.singletonDB import Database

class WokrWithHandler:
    __table = None

    def __init__(self, tbl):
        WokrWithHandler.__table = tbl

    @staticmethod
    async def OutPutInfo(mes):
        rpmrkp = None
        table = WokrWithHandler.getTable()
        for el in table.getPl('full'):
            if isinstance(el, Player):
                id = el.getID()
                plHand = el.getHand('lca')
                plStack = el.getStack()
                plBet = el.getBet()
                if not el.getFold():
                    rpmrkp = loseKey
                else:
                    if table.getcall() == 0: # choose between default_key.checkbet and default_key.callraise
                        rpmrkp = checkbet
                    else:
                        rpmrkp = callraise
                await bot.send_message(id, f'{mes}', reply_markup=setInLineKey(id, table))
                await bot.send_message(id, f'Ur cards: {plHand}\nUr stack: {plStack}\nUr Bet: {plBet}', reply_markup=rpmrkp)

    @staticmethod
    def getTable():
        return WokrWithHandler.__table

    @staticmethod
    def getDP():
        return dp

    @dp.message_handler(commands=['menu'])
    async def show_menu(message: types.Message):
        await bot.send_message(message.from_user.id, 'hola, Відкрито меню ✔', reply_markup=menu)
    
    @dp.message_handler(Text(equals=["Правила","Читати далі(1/6)","Читати далі(2/6)",
                                     "Читати далі(3/6)","Читати далі(4/6)","Читати далі(5/6)",
                                     "Повернутись в меню"]))
    async def rules(message: Message):
        if message.text == "Правила":
            await bot.send_message(message.from_user.id, 'В техасский холдем играют стандартной колодой — 52 карты. В холдеме существуют две обязательные ставки, называемые блайндами (ставки вслепую). Игра начинается с того, что два игрока, ставят заранее определенную сумму, ещё до сдачи карт. Первый игрок ставит малый блайнд и следующий игрок ставит большой блайнд. Большой блайнд, как правило, в два раза больше малого блайнда.', reply_markup=startrule)
        if message.text == "Читати далі(1/6)":
            await bot.send_message(message.from_user.id, 'Префлоп\nКаждый игрок получает по две карты. Первый круг ставок начинается сразу после сдачи карт. Первый игрок, который может делать ставки, это игрок, сидящий сразу по левую руку от игрока, поставившего большой блайнд. Первый игрок обязан принять ставку (✅ Call), поднять ставку (⏫ Raise) или же сбросить карты (❌ Fold). Принять ставку (✅ Call) – сделать ставку, которая будет равна большому блайнду. Поднять ставку (⏫ Raise) – игрок ставит большую сумму денег, чем ставка предыдущего игрока.', reply_markup=rule2)
        if message.text == "Читати далі(2/6)":
            await bot.send_message(message.from_user.id, 'Сбросить карты (❌ Fold) – игрок кладёт карты лицом вниз и передвигает их к середине стола. После этого игрок не принимает участия в игре до следующей сдачи карт, и теряет все сделанные им ставки. Следующие игроки имеют право выбора между теми же тремя действиями: принять ставку (✅ Call), поднять ставку (⏫ Raise) или сбросить карты (❌ Fold). Игроки могут повторно повысить ставку (Re-Raise), сумма которой должна составлять как минимум размер последнего повышения ставки.', reply_markup=rule3)
        if message.text == "Читати далі(3/6)":
            await bot.send_message(message.from_user.id, 'Флоп\nНа стол сдаются три общие карты. Второй круг ставок и все последующие круги начинаются с первого, ещё не сбросившего карты игрока, сидящего слева от дилера. Вдобавок к принятию ставки (✅ Call), поднятию ставки (⏫ Raise) или повторному повышению ставки (Re-Raise) игрок теперь может пропустить (✊ Check), при этом, не скидывая карты и не делая ставки, пока опять не подойдёт его очередь. В том случае если ставка была сделана, то игрок может принять её (✅ Call), поднять ставку (Raise) или повторно повысить ставку (Re-Raise). В противном случае игрок должен сбросить карты (❌ Fold). Таким образом, в конце круга все игроки сделают одинаковое количество ставок, кроме игроков, которым не хватило фишек. В таком случае он может поставить все фишки (💰 All-In), и тогда появляется один или несколько дополнительных банков (Side Pots), что ограничивает сумму, которую он может выиграть.', reply_markup=rule4)
        if message.text == "Читати далі(4/6)":
            await bot.send_message(message.from_user.id, 'Терн\nСдается четвёртая общая карта. Проходит третий круг ставок.', reply_markup=rule5)
        if message.text == "Читати далі(5/6)":
            await bot.send_message(message.from_user.id, 'Ривер\nСдается на стол последняя, пятая общая карта. Это последний круг ставок, после которого игроки вскрывают свои карты и определяется победитель. Если два или более игроков имеют одинаковую комбинацию, то выигрывает игрок, комбинация которого содержит вторую по старшинству карту (Kicker). Если ни у кого нет такой карты (Kicker), то банк делится между этими игроками.', reply_markup=rule6)
        if message.text == "Повернутись в меню":
            await bot.send_message(message.from_user.id, 'Відкриваю меню ✔', reply_markup=menu)
    
    
    @dp.message_handler(Text(equals=["Комбінації"]))
    async def get_button(message:Message):
        await bot.send_message(message.from_user.id, '''Комбинации карт в порядке убывания их достоинства:\n
                    9. ♥️A ♥️K ♥️Q ♥️J ♥️10 — Роял-флэш: стрит от 10 до туза из карт одинаковой масти.\n
                    8. ♣️9 ♣️8 ♣️7 ♣️6 ♣️5 — Стрит-флэш: стрит от любой карты, состоящий из карт одинаковой масти.\n
                    7. ♥️A ♠️A ♦️A ♣️A — Каре: любые четыре карты одинакового ранга.\n
                    6. ♥️A ♠️A ♦️A ♠️K ♥️K — Фул-хаус: любые три карты одинакового ранга и пара из двух других карт.\n
                    5. ♠️A ♠️9 ♠️7 ♠️6 ♠️2 — Флэш: любые пять карт одной масти в любой последовательности.\n
                    4. ♥️6 ♣️5 ♦️4 ♠️3 ♥️2 — Стрит: любые пять последовательных по рангу карт разных мастей.\n
                    3. ♥️A ♠️A ♦️A — Тройка: любые три карты одинакового ранга.\n
                    2. ♥️A ♠️A ♣️K ♦️K — Две пары: любые две карты одного ранга вместе с любыми двумя картами одинакового достоинства.\n
                    1. ♥️A ♠️A — Пара: любые две карты одного ранга.\n
                    0. ♥️A — Старшая карта: любая рука, из которой невозможно сложить указанные выше комбинации в покере.''')
    
    @dp.message_handler(Text(equals=["Рекорди"]))
    async def balance_func(message: Message):
        var = Database.getRows()
        await bot.send_message(message.from_user.id, f'{var[0]}\n{var[1]}\n{var[2]}\n{var[3]}\n{var[4]}\n')
    
    
    @dp.message_handler(Text(equals=["Сісти за стіл"]))
    async def main_func(message: Message):
        table = WokrWithHandler.getTable()
        if len(table.getPl('id')) < 9:
            if not (message.from_user.id in table.getPl('id')) and not table.getStart():
                table.addPl(message.from_user.id, message.from_user.first_name)
                for i in table.getPl('id'):
                    await bot.send_message(i, "new player in table)!", reply_markup=setInLineKey(i,table))
                    await bot.send_message(i, "щасливої гри", reply_markup=playKeyPos)

            elif not (message.from_user.id in table.getPl('id')) and table.getStart():
                table.addPl(message.from_user.id, message.from_user.first_name)
                await WokrWithHandler.OutPutInfo("new player in table)!")
            else:
                if table.getcall() == 0:
                    await bot.send_message(message.from_user.id, "new player in table)!", reply_markup=setInLineKey(message.from_user.id, table))
                    await bot.send_message(message.from_user.id, "щасливої гри", reply_markup=checkbet)
                else:
                    await bot.send_message(message.from_user.id, "new player in table)!", reply_markup=setInLineKey(message.from_user.id, table))
                    await bot.send_message(message.from_user.id, "щасливої гри", reply_markup=callraise)

            print(table.getPl('test'))
        else:
            await bot.send_message(message.from_user.id, "Вибачте, сталася помилка", reply_markup=menu)

    @dp.message_handler(Text(equals=["Грати","Зупинити"]))
    async def main_func(message: Message):
        table = WokrWithHandler.getTable()
        print(table.getStart())
        for el in table.getPl('full'):
            if isinstance(el, Player):
                if el.getID() == message.from_user.id:
                    if message.text == "Грати":
                        el.setFold(True)
                        await bot.send_message(message.from_user.id, "i ready!", reply_markup=setInLineKey(message.from_user.id, table))
                        await bot.send_message(message.from_user.id, 'Щасливої гри', reply_markup=playKeyNeg)
                    elif message.text == "Зупинити":
                        el.setFold(False)
                        await bot.send_message(message.from_user.id, "i not ready!", reply_markup=setInLineKey(message.from_user.id, table))
                        await bot.send_message(message.from_user.id, 'Щасливої гри', reply_markup=playKeyPos)
        print(table.getPl('test'))
    
        if table.goplay():
            await WokrWithHandler.OutPutInfo("new player in table)!")

    @dp.message_handler(Text(equals=["Call", "Fold", "Bet", "Check", "All-in", "Raise"]))
    async def main_func(message: Message):
        table = WokrWithHandler.getTable()
        if len(list(filter(lambda x: isinstance(x, Player), table.getPl('full')))) == 0:
            await bot.send_message(message.from_user.id, 'Відкрито меню ✔', reply_markup=menu)
            return
        else:
            if not message.from_user.id in table.getPl('id'):
                await bot.send_message(message.from_user.id, 'Відкрито меню ✔', reply_markup=menu)
                return

        if message.text == 'Call':
            if table.move(message.from_user.id, 'call'):
                await WokrWithHandler.OutPutInfo(f'call from {message.from_user.first_name}')
        elif message.text == 'Fold':
            if table.move(message.from_user.id, 'fold'):
                await WokrWithHandler.OutPutInfo(f'fold from {message.from_user.first_name}')
        elif message.text == 'Bet':
            if table.move(message.from_user.id, 'bet'):
                await WokrWithHandler.OutPutInfo(f'bet from {message.from_user.first_name}')
        elif message.text == 'Check':
            if table.move(message.from_user.id, 'check'):
                await WokrWithHandler.OutPutInfo(f'check from {message.from_user.first_name}')
        elif message.text == 'All-in':
            if table.move(message.from_user.id, 'all-in'):
                await WokrWithHandler.OutPutInfo(f'all-in from {message.from_user.first_name}')
        elif message.text == 'Raise':
            if table.move(message.from_user.id, 'raise'):
                await WokrWithHandler.OutPutInfo(f'raise from {message.from_user.first_name}')
        else:
            print("error in handler")
    
        if table.win(message.from_user.id):
            print('line 184')
            table.nextcircle()
            await WokrWithHandler.OutPutInfo(f'{table.getBoSt()}')
        else:
            print('line 190')
            if message.from_user.id == table.getCurrentlyPos().getID():
                print('line 192')
                if table.endcircle(message.from_user.id):
                    table.nextcircle()
                    await WokrWithHandler.OutPutInfo(f'{table.getBoSt()}')
                else:
                    print('line 155')
                    table.setCurrentlyPos('next')

        print(table.getPl('test'))
    
    
    @dp.message_handler(Text(equals=["Вийти"]))
    async def main_func(message: Message):
        table = WokrWithHandler.getTable()
        if message.from_user.id in table.getPl('id'):
            for el in table.getPl('full'):
                if isinstance(el, Player):
                    if el.getID() == message.from_user.id:
                        Database.setRows(message.from_user.id, el.getStack())
            table.delPl(message.from_user.id)
        await bot.send_message(message.from_user.id, 'Повертайтесь ще, ми вас чекаємо.', reply_markup=menu)

        if table.checkempty():
            for el in table.getPl('full'):
                if isinstance(el, Player):
                    await bot.send_message(el.getID(), 'Повертайтесь ще, ми вас чекаємо.', reply_markup=menu)
                    for el in table.getPl('full'):
                        if isinstance(el, Player):
                            if el.getID() == message.from_user.id:
                                Database.setRows(message.from_user.id, el.getStack())
                    table.delPl(el.getID())

    @dp.message_handler(commands=['start'])
    async def show_menu(message: types.Message):
        Database.add_posts((message.from_user.id, message.from_user.first_name, 0))
        await message.answer(f'hello, use command /menu')

    @dp.message_handler(commands=['help'])
    async def show_menu(message: types.Message):
        await message.answer(f'hi, use command /menu')