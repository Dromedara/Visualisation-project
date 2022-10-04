import pandas as pd
from datetime import datetime

from class_blocks.database_block import BD
import funcs_blocks.visualisation_block as visualisation_block
import funcs_blocks.subfuncs_block as subfuncs_block

########################
# 1


def count_arithmetic_mean(date=""):
    sum = BD.bases_dict[date]['Grade percent'].sum()
    count = len(BD.bases_dict[date].index)
    return (sum / count)


def all_progress():
    subfuncs_block.period_operator()

    values = []
    for date in BD.str_period:
        values.append(count_arithmetic_mean(date))

    visualisation_block.built_plot(y_values=values, x_values=BD.date_period,
                                   title=f"Общий прогресс пользователей за {BD.start_date} - {BD.finish_date}", xlbl="Дата", ylbl="Прогресс (%)")


########################
# 2

def get_value_by_choice(index=0, date=""):
    val = BD.bases_dict[date].at[index, 'Grade percent']
    return val


def individual_progress():

    index = subfuncs_block.get_index()

    subfuncs_block.period_operator()

    values = []
    period = []
    for i in range(len(BD.str_period)):
        if subfuncs_block.check_poss_index(index=index, date=BD.str_period[i]):
            values.append(get_value_by_choice(index, BD.str_period[i]))
            period.append(BD.date_period[i])

    visualisation_block.built_plot(y_values=values, x_values=period,
                                   title=f"Прогресс {BD.bases_dict[BD.str_period[-1]].at[index, 'Username']} за {BD.start_date} - {BD.finish_date}", xlbl="Дата", ylbl="Прогресс (%)")


########################
# 3


def get_value_by_ex(ex="", date=""):
    sum = BD.bases_dict[date][ex].sum()
    count = len(BD.bases_dict[date].index)
    return (sum / count)


def all_progress_ex():

    str_period = []
    period = []

    while len(str_period) == 0:
        str_period = []
        period = []
        ex = subfuncs_block.get_ex()
        subfuncs_block.period_operator()

        for i in range(len(BD.str_period)):
            if subfuncs_block.check_poss_column(c_name=ex, date=BD.str_period[i]):
                str_period.append(BD.str_period[i])
                period.append(BD.date_period[i])

        if len(str_period) == 0:
            print("Отсутствуют данные. Выберете другое задание или другой промежуток времени")

    values = []
    for date in str_period:
        values.append(get_value_by_ex(ex=ex, date=date))

    visualisation_block.built_plot(y_values=values, x_values=period,
                                   title=f"Общий прогресс пользователей по {ex} за {BD.start_date} - {BD.finish_date}", xlbl="Дата", ylbl="Прогресс (%)")


#######################
# 4


def get_value_by_coordinates(index="", ex="", date=""):
    val = BD.bases_dict[date].at[index, ex]
    return val


def individual_progress_ex():

    str_period = []
    period = []
    index = subfuncs_block.get_index()

    while len(str_period) == 0:
        str_period = []
        ex = subfuncs_block.get_ex()
        subfuncs_block.period_operator()

        for i in range(len(BD.str_period)):
            if subfuncs_block.check_poss_column(c_name=ex, date=BD.str_period[i]):
                str_period.append(BD.str_period[i])

        if len(str_period) == 0:
            print("Отсутствуют данные. Выберете другое задание или другой промежуток времени")

    values = []
    for i in range(len(str_period)):
        date = str_period[i]
        if subfuncs_block.check_poss_index(index=index, date=date):
            values.append(get_value_by_coordinates(index=index, ex=ex, date=date))
            period.append(BD.date_period[i])
    print(values)
    print(period)

    if len(values) == 0:
        print("Отсутствуют данные по этому пользователю за выбранные промежуток времени")
    else:
        visualisation_block.built_plot(y_values=values, x_values=period,
                                       title=f"Прогресс {BD.bases_dict[BD.str_period[-1]].at[index, 'Username']} по {ex} за {BD.start_date} - {BD.finish_date}", xlbl="Дата", ylbl="Прогресс (%)")

#######################
# 5


def get_column_of_values_by_ex(ex=""):
    vals = BD.bases_dict[BD.dates_list[-1]][ex].values
    return vals


def ex_done_mark():
    ex = subfuncs_block.get_ex()

    while not subfuncs_block.check_poss_column(c_name=ex, date=BD.dates_list[-1]):
        print("На данный момент недоступно. Выберете другое задание: ")
        ex = subfuncs_block.get_ex()

    values = get_column_of_values_by_ex(ex=ex)

    for i in range(len(values)):
        values[i] = values[i] * 100

    visualisation_block.built_hist(
        values=values, title=f" Оценка успешности выполнения {ex} на {BD.dates_list[-1]}", xlbl="Процент выполнения (%)", ylbl="Кол-во студентов")

#######################
# 6


def values_arithmetic_mean(ex=""):
    df = BD.bases_dict[BD.dates_list[-1]]
    sum = df[ex].sum()
    count = len(BD.bases_dict[BD.dates_list[-1]].index)
    cls = "str"
    if type(sum) == type(cls):
        return None
    else:
        return sum / count


def get_columns():
    columns = []
    words = ["Упражнение", "Зачет", "контроль"]
    all_columns = BD.bases_dict[BD.dates_list[-1]].columns
    for name in all_columns:
        for word in words:
            if word in name and any(chr.isdigit() for chr in name):
                columns.append(name)
    return columns


def top_exs_done():

    columns = get_columns()

    values = []
    x_names = []

    for ex in columns:
        val = values_arithmetic_mean(ex)
        if val is not None:
            values.append(val * 100)
            x_names.append(subfuncs_block.regulise(ex))

    visualisation_block.built_top(y_values=values, x_values=x_names,
                                  title=f" Оценка успешности выполнения всех заданий на {BD.dates_list[-1]}", xlbl="Номер задания", ylbl="Процент выполнения(%)")

#######################
# 7


def get_scores(n):
    scores = []
    for i in range(n):
        scores.append(BD.bases_dict[BD.dates_list[-1]].at[i, 'Grade percent'])
    return scores


def get_times(n):
    times = []
    for i in range(n):
        time_idx = -1
        date = BD.str_period[time_idx]
        score = BD.bases_dict[date].at[i, 'Grade percent']
        score_2 = score
        while score_2 == score and (-time_idx) < len(BD.str_period):
            time_idx = time_idx - 1
            date = BD.str_period[time_idx]
            if subfuncs_block.check_psblt_to_use(index=i, date=date):
                score_2 = BD.bases_dict[date].at[i, 'Grade percent']
        times.append(date)
    return times


def get_names():
    names = BD.bases_dict[BD.dates_list[-1]]["Username"].values
    return names


def get_ids():
    names = BD.bases_dict[BD.dates_list[-1]]["Student ID"].values
    return names


def users_top():

    subfuncs_block.period_operator()
    names = get_names()
    ids = get_ids()
    scores = get_scores(n=len(names))
    times_of_resault = get_times(n=len(names))

    top_df = pd.DataFrame({"ID": ids, "Username": names,
                          "Percent": scores, "Date": times_of_resault})

    top_df = top_df.sort_values(by=['Percent', 'Date'], ascending=[False, True])

    n = subfuncs_block.get_num_of_rows()
    txt = f"ТОП СТУДЕНТОВ ПО УСПЕВЕМОСТИ НА {BD.dates_list[-1]}\n\n"
    df = top_df if n is None or (n > len(BD.bases_dict[BD.dates_list[-1]].index)) else top_df[1:n]

    visualisation_block.show_dict(df=df, title_yes=txt, title_no="", flag=True)


#######################
# 8


class Carrier:
    def __init__(self, name="", id="", progress="", date=datetime.now().date()):
        self.name = name
        self.id = id
        self.progress = progress
        self.date = date


def check_cheater(prl, indx="", i_date=0):

    a = BD.bases_dict[BD.dates_list[i_date]].at[indx, 'Grade percent']
    b = BD.bases_dict[BD.dates_list[i_date + 1]].at[indx, 'Grade percent']

    if (b - a) > 50:
        prl.progress = f"+{b-a}%"
        prl.id = BD.bases_dict[BD.dates_list[i_date]].at[indx, "Student ID"]
        prl.name = BD.bases_dict[BD.dates_list[i_date]].at[indx, "Username"]
        prl.date = BD.dates_list[i_date + 1]
        return True, prl
    return False, prl


def cheater_block():

    ids = []
    names = []
    progress = []
    dates = []

    prl = Carrier()

    for i_date in range(0, len(BD.dates_list) - 1):
        for indx in BD.bases_dict[BD.dates_list[i_date]].index:
            res, prl = check_cheater(prl=prl, indx=indx, i_date=i_date)
            if res:
                ids.append(prl.id)
                names.append(prl.name)
                progress.append(prl.progress)
                dates.append(prl.date)

    prl_df = pd.DataFrame({"ID": ids, "Username": names,
                          "Progress": progress, "Date": dates})

    prl_df = prl_df.sort_values(by='Progress', ascending=False)

    txt1 = f"ПОДОЗРИЕТЛЬНЫЙ РОСТ ПРОГРЕССА\n\n"
    txt2 = "Подозрительных случаев не обнаружено!\n (Подозрительным считается прирост более 50% прогресса за сутки)\n\n"
    flag = True if len(prl_df.index) > 0 else False
    visualisation_block.show_dict(df=prl_df, title_yes=txt1, title_no=txt2, flag=flag)

#######################
# 9


def have_mark():
    ids = []
    names = []
    scores = []

    df = BD.bases_dict[BD.dates_list[-1]]
    for indx in BD.bases_dict[BD.dates_list[-1]].index:
        if df.at[indx, 'Grade percent'] > 60:
            ids.append(df.at[indx, "Student ID"])
            names.append(df.at[indx, "Username"])
            scores.append(df.at[indx, 'Grade percent'])

    ps_df = pd.DataFrame({"ID": ids, "Username": names, "Progress": scores})

    ps_df = ps_df.sort_values(by='Progress', ascending=False)

    txt1 = f"ВЫПОЛНИВШИЕ НЕОБХОДИМЫЙ МИНИМУМ\n\n"
    txt2 = "Выполнивших минимум не обнаружено!"
    flag = True if len(ps_df.index) > 0 else False

    visualisation_block.show_dict(df=ps_df, title_yes=txt1, title_no=txt2, flag=flag)

#######################
# 10


def have_no_mark():
    ids = []
    names = []
    scores = []

    df = BD.bases_dict[BD.dates_list[-1]]
    for indx in BD.bases_dict[BD.dates_list[-1]].index:
        if df.at[indx, 'Grade percent'] < 10:
            ids.append(df.at[indx, "Student ID"])
            names.append(df.at[indx, "Username"])
            scores.append(df.at[indx, 'Grade percent'])

    nps_df = pd.DataFrame({"ID": ids, "Username": names, "Progress": scores})

    nps_df = nps_df.sort_values(by='Progress', ascending=False)

    txt1 = f"ИМЕЮЩИЕ <= 10% ПРОГРЕССА\n(Не имеющие возможности закрытся в течениии дня без 'читерства')\n\n"
    txt2 = "Имеющих <= 10% прогресса не обнаружено!"
    flag = True if len(nps_df.index) > 0 else False

    visualisation_block.show_dict(df=nps_df, title_yes=txt1, title_no=txt2, flag=flag)
