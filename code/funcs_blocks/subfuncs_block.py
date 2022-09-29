import pandas
from datetime import datetime
import re

from class_blocks.database_block import BD


def get_num_of_rows():
    n = input("Сколько пользователей вывести? [<число>/all]: ")

    while not n.isdigit() or n != 'all':
        if n == 'all':
            return None
        if n.isdigit():
            return int(n)
        n = input("Невозможно выполнить. Попробуйте еще раз: ")

####################


def input_date(tag=''):

    date_in = input(f"{tag} (yyyy-mm-dd): ")
    date = re.findall(
        r'\d{4}-\d{2}-\d{2}', date_in)

    while len(date) == 0:
        date_in = input("Неправильный формат ввода даты. Попробуйте снова: ")
        date = re.findall(
            r'\d{4}-\d{2}-\d{2}', date_in)

    return date[0]


def translate_dates(str_date):
    date = datetime.strptime(str_date, "%Y-%m-%d").date()
    return date


def check_period(start_date="", finish_date=""):
    start_date = translate_dates(start_date)
    finish_date = translate_dates(finish_date)

    while finish_date < start_date:
        start_date = input_date("Период не существует. Попробуйте снова: показать данные с")
        finish_date = input_date("по")
        start_date = translate_dates(start_date)
        finish_date = translate_dates(finish_date)

    return start_date, finish_date


def get_dates():
    start_date = input_date("Показать данные с")
    finish_date = input_date("по")

    start_date, finish_date = check_period(start_date, finish_date)

    BD.change_def_date(start_date=start_date, finish_date=finish_date)


def select_dates(start_date, finish_date):

    str_dates = []
    dates = []
    for str_date in BD.dates_list:
        date = translate_dates(str_date)
        if start_date <= date <= finish_date:
            str_dates.append(str_date)
            dates.append(date)
    return str_dates, dates


def get_period():

    get_dates()
    BD.str_period, BD.date_period = select_dates(BD.start_date, BD.finish_date)


def period_operator():
    if len(BD.str_period) == 0:
        get_period()
    else:
        res = input(
            f"Использовать выбранный ранее период времени: {BD.start_date} - {BD.finish_date}? [y/n] : ")
        if res == 'n':
            get_period()


########################


def check_index(choice=''):
    df = BD.bases_dict[BD.dates_list[-1]]
    if choice in df["Username"].values:
        index = df.index[df["Username"] == choice].tolist()
        return index[0]
    if choice in df["Student ID"].values:
        index = df.index[df["Student ID"] == choice].tolist()
        return index[0]
    return None


def get_index():
    choice = input("Введите имя/ID: ")
    index = check_index(choice)

    while index is None:
        choice = input("Такого студента не существует. Введите другое имя/ID: ")
        index = check_index(choice)
    return index

########################


def regulise(ex):
    ex = ex.lower()

    res = re.findall(
        r'[0-9]+.[0-9]', ex)
    if len(res) > 0:
        return res[0]

    res = re.findall(
        r'контроль [0-9]', ex)
    if len(res) > 0:
        return res[0]

    res = re.findall(
        r'зачет [0-9]', ex)
    if len(res) > 0:
        return res[0]

    res = re.findall(
        r'зачет', ex)
    if len(res) > 0:
        return 'зачет (avg)'

    res = re.findall(
        r'контроль', ex)
    if len(res) > 0:
        return 'контроль (avg)'

    res = re.findall(
        r'[0-9]', ex)
    if len(res) > 0:
        return 'упражнение ' + res[0] + ' (avg)'


def find_column_name(choice=""):
    choice = regulise(ex=choice)
    columns = BD.bases_dict[BD.dates_list[-1]].columns
    for i in range(len(columns)):
        ex = columns[i]
        ex = ex.lower()
        if choice in ex:
            return columns[i]
    return None


def check_ex(choice):
    df = BD.bases_dict[BD.dates_list[-1]]
    column_name = find_column_name(choice)
    if column_name is not None:
        if column_name in df.columns:
            return column_name
    return None


def get_ex():
    choice = input("Введите название/номер задания: ")
    num = check_ex(choice)

    while num is None:
        choice = input("Такого задания не существует. Введите другой номер: ")
        num = check_ex(choice)
    return num

########################


def check_poss_index(index=0, date=""):
    l = len(BD.bases_dict[date].index)
    if l > index:
        return True
    return False


def check_poss_column(c_name="", date=""):
    df = BD.bases_dict[date]
    sum = df[c_name].sum()
    cls = "str"
    if type(sum) == type(cls):
        return False
    return True
