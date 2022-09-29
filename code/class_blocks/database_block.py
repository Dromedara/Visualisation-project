import os
import re
import pandas as pd
from datetime import datetime


class DataBase():

    def __init__(self):
        self.bases_dict = {}
        self.dates_list = []
        self.path = "C:\Ira\AtomPyProjects\Visualisation-project\data"
        self.link_list = os.listdir(self.path)
        self.def_date = datetime.now()
        self.start_date = self.def_date
        self.finish_date = self.def_date
        self.str_period = []
        self.date_period = []

    def change_def_date(self, start_date=datetime.now(), finish_date=datetime.now()):
        self.start_date = start_date
        self.finish_date = finish_date

    def get_dates(self):
        for i in range(len(self.link_list)):
            date = re.findall(
                r'\d{4}-\d{2}-\d{2}', self.link_list[i])
            self.dates_list.append(date[0])

    def get_bases(self):
        self.get_dates()
        for i in range(len(self.dates_list)):
            self.bases_dict[self.dates_list[i]] = pd.read_csv(
                f"{self.path}\{self.link_list[i]}")


BD = DataBase()
