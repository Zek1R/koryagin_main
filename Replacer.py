# Переставить два слова в конец

class Replacer():

    def __init__(self):
        self.text = []
        self.first_index = ""
        self.second_index = ""
        self.err = ""
        
    def reset(self):
        self.text = []
        self.first_index = ""
        self.second_index = ""
        self.err = ""

    def text_to_str(self):
        text = " ".join(self.text)
        return(text)
        # for i in self.text:
        #     text = text+i

    def validation(self, indx):
        if len(self.text) > 1:
            try:
                indx = int(indx)
                if not indx in range(len(self.text)+1):
                    self.err = f"Индекс может состоять только из чисел от 0 до {len(self.text)}"
                    return ""
                return indx
            except ValueError:
                self.err = "Индекс может состоять только из чисел"
                return ""
        else:
            self.err = "Количество слов должно быть больше одного" 
            return ""

    def set_index(self, indx, position):
        indx = self.validation(indx)
        print(f"index: {indx}")
        if indx != "":
            if position == 1:
                self.first_index = self.validation(indx)
                return self.first_index
            if position == 2:
                self.second_index = self.validation(indx)
                return self.second_index
        else:
            if position == 1: self.first_index = 0
            if position == 2: self.second_index = 0
            return ""

    
    def replace_word(self):
        self.err = ""

        print(f"Input text: {self.text_to_str()}")
        print(f"Input indexes: [{self.first_index}, {self.second_index}]")

        if self.first_index == "" or self.second_index == "": 
            return "Введите индексы"
        
        if self.first_index >= 0 and self.second_index >= 0:
            if (self.first_index == self.second_index) and self.first_index > 0:
                self.text.append(self.text.pop(self.first_index-1))
                return self.text_to_str()
            
            text = self.text

            if self.first_index > 0:
                first_word = text[self.first_index - 1]
                self.text[self.first_index - 1] = ""
                self.text.append(first_word)
            
            if self.second_index > 0:
                second_word = text[self.second_index - 1]
                self.text[self.second_index - 1] = ""
                self.text.append(second_word)

            print(f"После перестановки {self.text}")
            self.text = [i.strip() for i in self.text if i.strip()]

        return self.text_to_str()


# text = "Вася сегодня в ларек завезли пиво"