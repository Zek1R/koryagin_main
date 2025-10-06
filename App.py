from tkinter import *
from tkinter import ttk
import Translator


class App:
    def __init__(self):
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.translator = Translator.Translator()
        self.text_var = StringVar()
        self.err_text = StringVar()
        self.num = StringVar(value='Вводите текст')


    def config_window(self):
        # Конфигурация окна
        self.root.title("Translator")
        self.root.geometry("500x600")

        self.entry = ttk.Entry(self.root, width=40, font=("Arial", 18), textvariable=self.text_var).pack(pady=50)
        self.label = ttk.Label(self.root, textvariable=self.num, font=("Arial", 20)).pack(pady=70)
        self.err_label = ttk.Label(self.root, textvariable=self.err_text, font=("Arial", 20)).pack(pady=100)
        self.text_var.trace_add("write", self.callback)
        self.root.mainloop()
        
    def callback(self, *args):
        self.num.set(self.translator.validation(self.text_var.get()))
        self.err_text.set(self.translator.err)
    

    def run_app(self):
        self.config_window()

app = App()
app.run_app()