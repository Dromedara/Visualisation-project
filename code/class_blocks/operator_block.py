import funcs_blocks.counter_block as counter_block
import cover_blocks.end_block as end_block


class Operator():

    def __init__(self):
        self.operation_names_list = ["" for i in range(10)]
        self.operation_names_list[0] = "Общий прогресс пользователей за выбранный промежуток времени"
        self.operation_names_list[1] = "Индивидуальный прогресс пользователя за выбранный промежуток времени"
        self.operation_names_list[2] = "Прогресс пользователей по конкретному заданию за выбранный промежуток времени"
        self.operation_names_list[3] = "Прогресс индивидуального пользователя по конкретному заданию за выбранный промежуток времени"
        self.operation_names_list[4] = "Оценка успешности выполнения конкретного задания"
        self.operation_names_list[5] = "Оценка успешности выполнения всех заданий"
        self.operation_names_list[6] = "Рейтинг пользователей по прогрессу за определенный промежуток времени"
        self.operation_names_list[7] = "Поиск подозрительного прогресса"
        self.operation_names_list[8] = "Поиск выполнивших минимум"
        self.operation_names_list[9] = "Поиск имеющих <= 10% прогресса"

        self.operation_list_dict = {
            "Общий прогресс пользователей за выбранный промежуток времени": counter_block.all_progress,
            "Индивидуальный прогресс пользователя за выбранный промежуток времени": counter_block.individual_progress,
            "Прогресс пользователей по конкретному заданию за выбранный промежуток времени": counter_block.all_progress_ex,
            "Прогресс индивидуального пользователя по конкретному заданию за выбранный промежуток времени": counter_block.individual_progress_ex,
            "Оценка успешности выполнения конкретного задания": counter_block.ex_done_mark,
            "Оценка успешности выполнения всех заданий": counter_block.top_exs_done,
            "Рейтинг пользователей по прогрессу за определенный промежуток времени": counter_block.users_top,
            "Закончить работу": end_block.run_it,
            "Поиск подозрительного прогресса": counter_block.cheater_block,
            "Поиск выполнивших минимум": counter_block.have_mark,
            "Поиск имеющих <= 10% прогресса": counter_block.have_no_mark
        }

        self.subfuncks_dict = {
            "exit": end_block.run_it
        }

        self.commands_messages = [
            "Закончить работу (команда 'exit')"]

    def show_menu(self):

        print(*self.commands_messages, sep='\n')
        print("-" * 40)

        for i in range(len(self.operation_names_list)):
            print(f"{i+1}: {self.operation_names_list[i]}")
        print("=" * 40)

    def run_operation(self, choice=""):
        self.operation_list_dict[self.operation_names_list[choice]]()

    def run_commands(self):
        self.subfuncks_dict['exit']()

    def check_input(self, choice):

        if choice.isdigit():
            for i in range(len(self.operation_names_list)):
                if choice == str(i + 1):
                    return True

        if choice == 'exit':
            self.run_commands()

    def get_input(self):
        choice = input("Пожалуйста, выберете номер операции или введите команду: ")
        while not self.check_input(choice):
            choice = input("Невозможно исполнить. Попробуйте снова: ")
            print(choice)

        choice = int(choice)
        self.run_operation(choice - 1)

    def run_it(self):
        self.show_menu()
        self.get_input()


connection_operator = Operator()
