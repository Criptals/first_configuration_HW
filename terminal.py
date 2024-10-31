import os
import zipfile
from zipfile import ZipFile
from os import remove, rename
from win_mode import Window


class MyTerminal:
    def __init__(self, file_system: ZipFile):
        self.fs = file_system
        self.cur_d = ''
        self.polling = False
        self.window = None
        self.file_perm = "-rw-r--r--"
        self.d_path ="C/Users/serge/OneDrive/Рабочий стол/МИРЭА/first_configuration_HW/my_test"

    def attach(self, window: Window):
        self.window = window
        self.window.write(f'user:~{self.cur_d}$ ')

    def output(self, message, end='\n'):
        if self.window is None:
            print(message)
        else:
            self.window.write(message + end)

    def start_polling(self):
        self.polling = True
        while self.polling:
            message = f'user:~{self.cur_d}$ '
            enter = input(message).strip()
            if len(enter) > 0:
                self.command_dispatcher(enter)
        self.output('stop polling...')

    def command_dispatcher(self, command):
        if self.window is not None:
            self.output(command)

        params = command.split()
        if params[0] == 'exit':
            if self.window is None:
                self.polling = False
            else:
                self.window.stop_polling()
                return
        elif params[0] == 'cd':
            temp_dir = self.cd(params[1:])
            if temp_dir is not None:
                self.cur_d = temp_dir
        elif params[0] == 'ls':
            self.output(self.ls(params[1:]))
        elif params[0] == 'mv':
            self.mv(params[1:])
        elif params[0] == 'chmod':
            self.chmod(params[1:])
        else:
            self.output("Команда не найдена")

        if self.window is not None:
            self.output(f'user:~{self.cur_d}$ ', end='')

    def cd(self, params):
        if len(params) == 0:
            return ''
        directory = params[-1]

        directory = directory.strip('/')
        directory = directory.split('/')

        new_directory = self.cur_d[:-1].split('/')
        if new_directory == ['']:
            new_directory = []
        for i in directory:
            if i == '..':
                if len(new_directory) > 0:
                    new_directory.pop()
                else:
                    self.output('Некорректный путь до директории')
                    return
            else:
                new_directory.append(i)

        new_path = '/'.join(new_directory) + '/'
        if new_path == '/':
            return ''

        for file in self.fs.namelist():
            if file.startswith(new_path):
                return new_path
        self.output('Директория с таким названием отсутствует')

    def ls(self, params):
        work_directory = self.cur_d
        if len(params) > 0:
            work_directory = self.cd((params[-1],))
            if work_directory is None:
                return ''

        files = set()
        for file in self.fs.namelist():
            if file.startswith(work_directory):
                ls_name = file[len(work_directory):]
                if '/' in ls_name:
                    ls_name = ls_name[:ls_name.index('/')]
                files.add(ls_name)
        return '\n'.join(sorted(filter(lambda x: len(x) > 0, files)))

    def mv(self, params):
        file1 = params[-2]
        file2 = params[-1]
        z = zipfile.ZipFile("C:/Users/serge/OneDrive/Рабочий стол/МИРЭА/first_configuration_HW/my_test_zip.zip")
        z.extractall("my_test")

        nl = self.fs.namelist()
        print(nl)
        a = b = ''
        for i in nl:
            if file1 == i.split("/")[0]:
                a = self.d_path + i
                b = self.d_path + file2
            print(i.split("/")[-1])
            if file1 == i.split("/")[-1]:
                print(1111, file1)
                a = self.d_path + "/".join(i.split("/")[1:-1]) + "/" + file1
                b = self.d_path + "/".join(i.split("/")[1:-1]) + "/" + file2
                print(a, b)
                break
        try:
            os.rename(a, b)
        except:
            return 'Неправильное название файла'

    def chmod(self, params):
        try:
            options, path_to_file = params.split()
        except IndexError:
            return "chmod: Provide additional arguments"
        output = ""
        try:
            if options.isdigit():
                a, b, c = [int(i) for i in options]
                """if a == 0:
                    
                elif a == 1:

                elif a == 2:

                elif a == 3:

                elif a == 4:

                elif a == 5:

                elif a == 6:

                elif a == 7:

                if b == 0:

                elif b == 1:

                elif b == 2:

                elif b == 3:

                elif b == 4:

                elif b == 5:

                elif b == 6:

                elif b == 7:

                if c == 0:

                elif c == 1:

                elif c == 2:

                elif c == 3:

                elif c == 4:

                elif c == 5:

                elif c == 6:

                elif c == 7:"""
        except KeyError:
            return -1

        return output
