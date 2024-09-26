import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import subprocess

class TerminalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Embedded Terminal")

        self.terminal_output = ScrolledText(self, wrap=tk.WORD)
        self.terminal_output.pack(fill=tk.BOTH, expand=True)

        self.terminal_process = subprocess.Popen(["bash"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

        self.after(100, self.update_terminal())

    def update_terminal(self):
        data = self.terminal_process.stdout.read(1024)
        if data:
            self.terminal_output.insert(tk.END, data.decode())
        self.after(100, self.update_terminal())

if __name__ == "__main__":
    app = TerminalApp()
    app.mainloop()