from zipfile import ZipFile
from sys import argv
from os.path import exists
from win_mode import Window
from terminal import MyTerminal


def main():
    if len(argv) > 1:
        config_file = argv[1]
    else:
        print("Отсутствует необходимый аргумент: путь к конфигурационному файлу")
        return

    if exists(config_file):
        with open(config_file) as config:
            fs_path = config.readline().strip()
    else:
        print("Конфигурационный файл с таким названием отсутствует")
        return

if __name__ == '__main__':
    main()