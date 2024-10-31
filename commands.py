import os
import json
import zipfile


class FileSystemEmulator:
    def __init__(self, zip_path):
        self.zip_path = zip_path

    def ls(self, dir):
        with zipfile.ZipFile(self.zip_path, 'r') as arch:
            a = arch.infolist()
            n = dir.split("/")
            b = ""
            if n[-1] == '':
                b = n[-2]
            else:
                b = n[-1]
            lst1 = []
            lst2 = []
            for i in a:
                if b in str(i.filename):
                    c = "/".join(str(i.filename).split("/")[1:])
                    if c != "":
                        lst1.append(c)
                else:
                    lst2.append(str(i.filename))
            if len(lst2) == len(a):
                return lst2
            else:
                return lst1

    def cd(self, path):
        with zipfile.ZipFile(self.zip_path, 'r') as arch:
            a = arch.infolist()
            lst = []
            for i in a:
                lst.append(str(i.filename))
            if path in lst:
                if '.' not in path:
                    return "/" + path
                else:
                    return "Нельзя перейти в файл"

    def mv(self, source, destination):
        with zipfile.ZipFile(self.zip_path, 'x') as arch:
            a = arch.infolist()
            lst = ""
            for i in a:
                if source in i.filename:
                    lst = i.filename
                    break
            s = self.zip_path + "/" + lst
            a = zipfile.Path(s)
            b = a.read_text()
            print(b)
            c = destination

    def chmod(self, mode, path):
        os.chmod(path, mode)


# Логирование действий
class Logger:
    def __init__(self, log_path):
        self.log_path = log_path

    def log_action(self, action):
        with open(self.log_path, 'a') as log_file:
            json.dump(action, log_file)
            log_file.write('n')
