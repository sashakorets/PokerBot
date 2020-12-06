from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from treys import Card

from tgApi.db import table1

def setInLineKey(tgID):
    inline_keyboard = [
        [
            InlineKeyboardButton(text="9", callback_data="test:cards9:9"),
            InlineKeyboardButton(text="ImgTable", callback_data="lev3"),
            InlineKeyboardButton(text="1", callback_data="test:cards1:1")
        ],
        [
            InlineKeyboardButton(text="8", callback_data="test:cards8:8"),
            InlineKeyboardButton(text="Board", callback_data="lev2"),
            InlineKeyboardButton(text="2", callback_data="test:cards2:2")
        ],
        [
            InlineKeyboardButton(text="7", callback_data="test:cards7:7"),
            InlineKeyboardButton(text="Potsameinfo", callback_data="lev1"),
            InlineKeyboardButton(text="3", callback_data="test:cards3:3")
        ],
        [
            InlineKeyboardButton(text="6", callback_data="test:cards6:6"),
            InlineKeyboardButton(text="5", callback_data="test:cards4:5"),
            InlineKeyboardButton(text="4", callback_data="test:cards4:4")
        ],
    ]
    count = 1
    for i in table1.getPl('id'):
        if count == 1:
            if i == tgID:
                inline_keyboard[0][2] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count-1]}', callback_data="test:cards1:1")
                count += 1
            else:
                inline_keyboard[0][2] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count-1]}', callback_data="test:cards1:1")
                count += 1
        elif count == 2:
            if i == tgID:
                inline_keyboard[1][2] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count - 1]}', callback_data="test:cards2:2")
                count += 1
            else:
                inline_keyboard[1][2] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count - 1]}',callback_data="test:cards2:2")
                count += 1
        elif count == 3:
            if i == tgID:
                inline_keyboard[2][2] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count - 1]}',callback_data="test:cards3:3")
                count += 1
            else:
                inline_keyboard[2][2] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count - 1]}',callback_data="test:cards3:3")
                count += 1
        elif count == 4:
            if i == tgID:
                inline_keyboard[3][2] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count - 1]}',callback_data="test:cards4:4")
                count += 1
            else:
                inline_keyboard[3][2] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count - 1]}',callback_data="test:cards4:4")
                count += 1
        elif count == 5:
            if i == tgID:
                inline_keyboard[3][1] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count - 1]}',callback_data="test:cards5:5")
                count += 1
            else:
                inline_keyboard[3][1] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count - 1]}', callback_data="test:cards5:5")
                count += 1
        elif count == 6:
            if i == tgID:
                inline_keyboard[3][0] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count - 1]}',callback_data="test:cards6:6")
                count += 1
            else:
                inline_keyboard[3][0] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count - 1]}',callback_data="test:cards6:6")
                count += 1
        elif count == 7:
            if i == tgID:
                inline_keyboard[2][0] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count - 1]}',callback_data="test:cards7:7")
                count += 1
            else:
                inline_keyboard[2][0] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count - 1]}',callback_data="test:cards7:7")
                count += 1
        elif count == 8:
            if i == tgID:
                inline_keyboard[1][0] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count - 1]}',callback_data="test:cards8:8")
                count += 1
            else:
                inline_keyboard[1][0] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count - 1]}',callback_data="test:cards8:8")
                count += 1
        elif count == 9:
            if i == tgID:
                inline_keyboard[0][0] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count-1]}', callback_data="test:cards9:9")
                count += 1
            else:
                inline_keyboard[0][0] = InlineKeyboardButton(text=f'{table1.getPl("full")[count-1].getHand("lca")} {table1.getPl("fname")[count-1]}', callback_data="test:cards9:9")
                count += 1
        else:
            print("error in inline_key")

        inline_keyboard[1][1] = InlineKeyboardButton(text=f'{table1.getBoard("river","lca")}', callback_data="test:board:1")
        inline_keyboard[2][1] = InlineKeyboardButton(text=f'{table1.getPot()}', callback_data="test:pot:1")

    player = InlineKeyboardMarkup(inline_keyboard = inline_keyboard)
    return player
