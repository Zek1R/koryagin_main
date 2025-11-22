from tkinter import *  
from tkinter import ttk
import Translator
import Replacer


class App(Tk):
    def __init__(self):
        super().__init__()
        # Конфигурация окна
        self.title("Multiapp")
        self.geometry("450x500")

        self.translator = Translator.Translator()
        self.replacer = Replacer.Replacer()

        self.container = ttk.Frame()
        self.container.pack(fill='both', expand=True)
        
        self.pages = {}
        for PageClass in (Translator_page, Replacer_page):
            page = PageClass(self.container, self)
            self.pages[PageClass] = page
            page.grid(row=0, column=0, sticky='nsew')

        self.show_page(Translator_page)
        

    def show_page(self, PageClass):
        page = self.pages[PageClass]
        page.tkraise()



class Translator_page(ttk.Frame):        
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.input_text = StringVar()
        self.err_text = StringVar()
        
        self.num = StringVar(value='Вводите текст')

        self.entry = ttk.Entry(self, width=30, font=("Calibri Bold", 20), textvariable=self.input_text)
        self.entry.grid(row=0, column=0, padx=10, rowspan=1, pady=50, sticky="n")
        
        self.reset_button = Button(self, text="×", command=lambda: self.input_text.set(""), font=("Calibri Bold", 15), width=3)
        self.reset_button.grid(row=0, column=0, padx=0, sticky="e")
        
        self.num_lable = ttk.Label(self, textvariable=self.num, font=("Arial", 32))
        self.num_lable.grid(row=2, column=0, pady=50)
        
        self.err_label = ttk.Label(self, textvariable=self.err_text, font=("Arial", 20), wraplength="400", justify="center")
        self.err_label.grid()

        self.goto_next_page = Button(self, text="2-е задание", command=lambda: controller.show_page(Replacer_page), font=("Arial", 16))
        self.goto_next_page.grid(row=6, column=0, padx=10)

        self.input_text.trace_add("write", self.translator_callback)
        

    def translator_callback(self, *args):
        self.num.set(self.controller.translator.check_numbers(self.input_text.get()))
        self.err_text.set(self.controller.translator.err)
        self.input_text.set(self.input_text.get().upper())



class Replacer_page(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.input_text = StringVar()
        self.first_index = StringVar()
        self.second_index = StringVar()
        self.text = StringVar(value="Введите текст")
        self.err_text = StringVar()

        self.text_entry = ttk.Entry(self, width=30, font=("Calibri Bold", 20), textvariable=self.input_text)
        self.text_entry.grid(row=0, column=0, padx=10, rowspan=1, pady=50, sticky="n")

        self.reset_button = Button(self, text="×", command=self.reset, font=("Calibri Bold", 15), width=3)
        self.reset_button.grid(row=0, column=0, padx=10, sticky="e")

        self.first_index_entry = ttk.Entry(self, width=3, font=("Arial", 18), textvariable=self.first_index)
        self.first_index_entry.grid(row=1, column=0, padx=10, sticky="w")
        
        self.second_index_entry = ttk.Entry(self, width=3, font=("Arial", 18), textvariable=self.second_index)
        self.second_index_entry.grid(row=1, column=0, padx=60, sticky="w")

        # self.reset_button = Button(self, text="Стереть", command=lambda: self.input_text.set(""), font=("Arial", 14), width=10).place(y=95, x=380)
        
        self.text_label = ttk.Label(self, textvariable=self.text, font=("Arial Bold", 20), wraplength="400", justify="center")
        self.text_label.grid(row=2, pady=30)

        self.err_label = ttk.Label(self, textvariable=self.err_text, font=("Arial", 20), wraplength="400", justify="center")
        self.err_label.grid(row=3)

        self.goto_previous_page = Button(self, text="1-е задание", command=lambda: controller.show_page(Translator_page), font=("Arial", 16))
        self.goto_previous_page.grid(row=6, column=0, padx=10)

        self.input_text.trace_add("write", self.replacer_callback)
        self.first_index.trace_add("write", self.first_index_callback)
        self.second_index.trace_add("write", self.second_index_callback)


    def reset(self):
        self.first_index.set("")
        self.second_index.set("")
        self.input_text.set("")
        self.controller.replacer.reset()
        self.text.set("Введите текст")


    def replacer_callback(self, *args):
        text = self.input_text.get().split(" ")
        self.controller.replacer.text = [i.strip() for i in text if i.strip()]  


    def first_index_callback(self, *args):
        self.replacer_callback()
        self.first_index.set(self.controller.replacer.set_index(self.first_index.get(), 1))
        print(f"Первый индекс: {self.first_index.get()}")
        self.text.set(self.controller.replacer.replace_word())
        self.err_text.set(self.controller.replacer.err)
        

    def second_index_callback(self, *args):
        self.replacer_callback()
        self.second_index.set(self.controller.replacer.set_index(self.second_index.get(), 2))
        print(f"Второй индекс: {self.second_index.get()}")
        self.text.set(self.controller.replacer.replace_word())
        self.err_text.set(self.controller.replacer.err)
        

app = App()
app.mainloop()
