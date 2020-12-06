from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery
from tgApi.config import dp, bot
from tgApi.default_key import *
from tgApi.db import table1
from tgApi.inline_key import *

@dp.message_handler(commands=['menu'])
async def show_menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'Відкриваю меню ✔', reply_markup=menu)

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

@dp.message_handler(Text(equals=["Баланс"]))
async def main_func(message: Message):
    await bot.send_message(message.from_user.id, "Бот знаходиться в тестовому режимі, тому кожному гравцеві будуть видаватись 1000 фішок, коли він сідає за стіл, попередні будуть анульовані.\nДякуємо за розуміння!!!")


@dp.message_handler(Text(equals=["Сісти за стіл"]))
async def main_func(message: Message):
    if len(table1.getPl('id')) != 9 and not (message.from_user.id in table1.getPl('id')):
        table1.addPl(message.from_user.id, message.from_user.first_name)
        for i in table1.getPl('id'):
            await bot.send_message(i, "new player in table)!", reply_markup=setInLineKey(i))
            await bot.send_message(i, 'Щасливої гри', reply_markup=playKeyPos)
        print(table1.getPl('test'))
    else:
        await bot.send_message(message.from_user.id, "Вибач     те, сталася помилка", reply_markup=menu)

from mechanic.player import Player
@dp.message_handler(Text(equals=["Грати","Зупинити"]))
async def main_func(message: Message):
    for el in table1.getPl('full'):
        if isinstance(el, Player):
            if el.getID() == message.from_user.id:
                if message.text == "Грати":
                    el.setFold(True)
                    await bot.send_message(message.from_user.id, "i ready!", reply_markup=setInLineKey(message.from_user.id))
                    await bot.send_message(message.from_user.id, 'Щасливої гри', reply_markup=playKeyNeg)
                elif message.text == "Зупинити":
                    el.setFold(False)
                    await bot.send_message(message.from_user.id, "i not ready!", reply_markup=setInLineKey(message.from_user.id))
                    await bot.send_message(message.from_user.id, 'Щасливої гри', reply_markup=playKeyPos)
    print(table1.getPl('test'))

    if table1.goplay():
        for i in table1.getPl('id'):
            await bot.send_message(i, "welcome!", reply_markup=setInLineKey(i))
            await bot.send_message(i, 'Щасливої гри', reply_markup=game)

@dp.message_handler(Text(equals=["Call","Fold","Bet","Check","All-in","Raise"]))
async def main_func(message: Message):
    if message.text == 'Call':
        if table1.move(message.from_user.id, 'call'):
            for i in table1.getPl('id'):
                await bot.send_message(i, "call", reply_markup=setInLineKey(i))
                await bot.send_message(i, 'Щасливої гри', reply_markup=game)
    elif message.text == 'Fold':
        if table1.move(message.from_user.id, 'fold'):
            for i in table1.getPl('id'):
                await bot.send_message(i, "fold", reply_markup=setInLineKey(i))
                await bot.send_message(i, 'Щасливої гри', reply_markup=game)
    elif message.text == 'Bet':
        if table1.move(message.from_user.id, 'bet'):
            for i in table1.getPl('id'):
                await bot.send_message(i, "bet", reply_markup=setInLineKey(i))
                await bot.send_message(i, 'Щасливої гри', reply_markup=game)
    elif message.text == 'Check':
        if table1.move(message.from_user.id, 'check'):
            for i in table1.getPl('id'):
                await bot.send_message(i, "check", reply_markup=setInLineKey(i))
                await bot.send_message(i, 'Щасливої гри', reply_markup=game)
    elif message.text == 'All-in':
        if table1.move(message.from_user.id, 'all-in'):
            for i in table1.getPl('id'):
                await bot.send_message(i, "all-in", reply_markup=setInLineKey(i))
                await bot.send_message(i, 'Щасливої гри', reply_markup=game)
    elif message.text == 'Raise':
        if table1.move(message.from_user.id, 'raise'):
            for i in table1.getPl('id'):
                await bot.send_message(i, "raise", reply_markup=setInLineKey(i))
                await bot.send_message(i, 'Щасливої гри', reply_markup=game)
    else:
        print("error in handler")
    if not table1.endStep():
        table1.refresh()
        for i in table1.getPl('id'):
            await bot.send_message(i, "raise", reply_markup=setInLineKey(i))
            await bot.send_message(i, 'Щасливої гри', reply_markup=game)

    print(table1.getPl('test'))


@dp.message_handler(Text(equals=["Вийти"]))
async def main_func(message: Message):
    if message.from_user.id in table1.getPl('id'):
        table1.delPl(message.from_user.id)
    await bot.send_message(message.from_user.id, 'Повертайтесь ще, ми вас чекаємо.', reply_markup=menu)







