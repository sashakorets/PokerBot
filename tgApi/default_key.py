from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Сісти за стіл"),
        KeyboardButton(text="Правила"),
    ],
    [
        KeyboardButton(text="Комбінації"),
        KeyboardButton(text="Баланс"),

    ],
], resize_keyboard=True)

game = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Call"),
        KeyboardButton(text="Fold"),
        KeyboardButton(text="Bet"),
    ],
    [
        KeyboardButton(text="Chek"),
        KeyboardButton(text="All-in"),
        KeyboardButton(text="Raise"),

    ],
    [
        KeyboardButton(text="Вийти"),

    ],
], resize_keyboard=True)

startrule = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Читати далі(1/6)")
    ],
    [
        KeyboardButton(text="Повернутись в меню"),
    ],

], resize_keyboard=True)
rule2 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Читати далі(2/6)")
    ],
    [
        KeyboardButton(text="Повернутись в меню"),
    ],

], resize_keyboard=True)
rule3 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Читати далі(3/6)")
    ],
    [
        KeyboardButton(text="Повернутись в меню"),
    ],

], resize_keyboard=True)
rule4 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Читати далі(4/6)")
    ],
    [
        KeyboardButton(text="Повернутись в меню"),
    ],

], resize_keyboard=True)
rule5 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Читати далі(5/6)")
    ],
    [
        KeyboardButton(text="Повернутись в меню"),
    ],

], resize_keyboard=True)
rule6 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Повернутись в меню"),
    ],

], resize_keyboard=True)

playKeyPos = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Грати"),
    ],
    [
        KeyboardButton(text="Вийти"),

    ],
], resize_keyboard=True)
playKeyNeg = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Зупинити"),
    ],
    [
        KeyboardButton(text="Вийти"),

    ],
], resize_keyboard=True)
