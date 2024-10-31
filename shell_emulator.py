import tkinter as tk
from tkinter import scrolledtext
from commands import FileSystemEmulator


class ShellEmulator:
    def __init__(self, master, username):
        self.master = master
        self.username = username
        self.current_directory = "my_test_zip.zip"
        self.file_system_path = "C:/Users/serge/OneDrive/Рабочий стол/МИРЭА/first_configuration_HW/my_test_zip.zip"
        self.file_system = FileSystemEmulator("C:/Users/serge/OneDrive/Рабочий стол/МИРЭА/first_configuration_HW/my_test_zip.zip")
        self.output_area = scrolledtext.ScrolledText(master, wrap=tk.WORD)
        self.output_area.pack(expand=True, fill='both')
        self.input_field = tk.Entry(master)
        self.input_field.pack(fill='x')
        self.input_field.bind("<Return>", self.execute_command)

    def execute_command(self, event):
        command = self.input_field.get().strip()  # Получаем и обрезаем введённую команду
        self.output_area.insert(tk.END,
                                f"{self.username}@shell: {self.current_directory} $ {command}\n")  # Отображаем команду

        # Обработка команд
        parts = command.split()  # Разделяем команду на части

        if not parts:
            return  # Если команда пустая, ничего не делаем

        cmd = parts[0]

        try:
            if cmd == "ls":
                output = self.file_system.ls(self.current_directory)  # Вызываем метод ls
                self.output_area.insert(tk.END, ", ".join(output)+"\n")

            elif cmd == "cd":

                if len(parts) > 1:
                    if parts[1] == "..":
                        self.current_directory = "/".join(self.current_directory.split("/")[0:-2])
                    else:
                        a = self.file_system.cd(parts[1])  # Вызываем метод cd
                        if a == "Нельзя перейти в файл":
                            self.output_area.insert(tk.END, "Error: You can't cd to file\n")
                        else:
                            self.current_directory += a  # Обновляем текущий каталог
                else:
                    self.output_area.insert(tk.END, "Error: Directory name required\n")

            elif cmd == "mv":
                if len(parts) > 2:
                    print(parts[1], parts[2])
                    self.file_system.mv(parts[1], parts[2])  # Перемещаем или переименовываем файл/каталог
                    self.output_area.insert(tk.END, f"Moved '{parts[1]}' to '{parts[2]}'\n")
                else:
                    self.output_area.insert(tk.END, "Error: Source and destination required\n")

            elif cmd == "exit":
                self.master.quit()  # Выход из приложения

            else:
                self.output_area.insert(tk.END, "Error: Command not found\n")

        except Exception as e:
            self.output_area.insert(tk.END, f"Error: {str(e)}\n")

        finally:
            self.input_field.delete(0, tk.END)  # Очищаем текстовое поле ввода


if __name__ == "__main__":
    root = tk.Tk()
    app = ShellEmulator(root, "user")
    root.mainloop()
