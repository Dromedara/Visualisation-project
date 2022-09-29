from class_blocks.database_block import BD


def greeting():
    print("Данная программа была написна для визуализации данных об обучении студентов на курсе. Ниже приведен список доступных операций:")


def prepare_data():
    BD.get_bases()


def run_it():
    prepare_data()
    greeting()
