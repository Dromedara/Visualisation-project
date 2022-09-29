import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os


def built_plot(y_values=[], x_values=[], title="", xlbl="", ylbl=""):

    plt.figure(figsize=(12, 6))
    plt.title(title)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    if len(x_values) > 20:
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=int(len(x_values) / 10)))
    plt.gcf().autofmt_xdate()

    plt.grid(linestyle='--')
    plt.plot(x_values, y_values, marker='o')
    plt.show()


def built_hist(values=[], title="", xlbl="", ylbl=""):

    plt.figure(figsize=(12, 6))
    plt.title(title)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.grid(which='major', linestyle='--')
    plt.hist(values)
    plt.show()


def built_top(y_values=[], x_values=[], title="", xlbl="", ylbl=""):

    plt.figure(figsize=(12, 6))
    plt.title(title)
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.grid(which='major', linestyle='--')
    plt.bar(x_values, y_values, width=0.1)
    plt.show()


def show_dict(df, title_yes="", title_no="", flag=False):

    f = open("result.txt", "w")

    if flag:
        f.write(f"{title_yes}\n")
        f.write(f"{str(len(df.index))} \n\n")
        f.write(df.to_string(index=False))
    else:
        f.write(f"{title_no}")
    f.close()
    os.system("result.txt")
