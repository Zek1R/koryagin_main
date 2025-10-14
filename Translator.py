# Французский язык

# Алфавит ['A', ... , 'Z', '-', ' ']


class Translator:
    def __init__(self):
        self.alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', ' ']
        
        self.hundreds = {"cent" : 100,
                         "deux-cent" : 200,
                         "trois-cent" : 300,
                         "quatre-cent" : 400,
                         "cinq-cent" : 500,
                         "six-cent" : 600,
                         "sept-cent" : 700,
                         "huit-cent" : 800,
                         "neuf-cent" : 900}
        
        self.tens = {"dix" : 10,
                     "vingt" : 20,
                     "trente" : 30,
                     "quarante" : 40,
                     "cinquante" : 50,
                     "soixante" : 60,
                     "soixante-dix" : 70,
                     "quatre-vingts" : 80,
                     "quatre-vingts-dix" : 90}
        
        self.units = {"zero" : 0,
                      "un" : 1,
                      "etun" : 1,
                      "deux" : 2,
                      "trois" : 3,
                      "quatre" : 4,
                      "cinq" : 5,
                      "six" : 6,
                      "sept" : 7,
                      "huit" : 8,
                      "neuf" : 9,
                      "onze" : 11,
                      "etonze" : 11,
                      "douze" : 12,
                      "treize" : 13,
                      "quatorze" : 14,
                      "quinze" : 15,
                      "seize" : 16,
                      "dix-sept" : 17,
                      "dix-huit" : 18,
                      "dix-neuf" : 19}
                
        self.number = {"hundred" : 0, "ten" : 0, "unit" : 0}

        self.err = ""
        
        
    
    def validation(self, slovo):
        print(slovo)
        slovo = slovo.lower()
        for i in slovo:
            if i not in self.alphabet:
                self.err = f"Неверный символ {i}"
                return 0
        return self.check_numbers(slovo)
    

    def in_hundreds(self, slovo):
        if slovo in self.hundreds: return True  
        return False
        
    def in_tens(self, slovo):
        if slovo in self.tens: return True  
        return False
    
    def in_units(self, slovo):
        if slovo in self.units: return True  
        return False


    def raise_error(self, err):
        if self.in_hundreds(err):
            if self.number["hundred"] != 0: self.err = f"Ошибка. Сотни уже введены"
            if self.number["ten"] != 0 or self.number["unit"] != 0: self.err = f"Ошибка. Неверный порядок ввода"
        elif self.in_tens(err):
            if self.number["ten"] != 0: self.err = f"Ошибка. Десятки уже введены"
            if self.number["unit"] != 0: self.err = f"Ошибка. Неверный порядок ввода"
        elif self.in_units(err):
            if self.number["unit"] != 0: self.err = f"Ошибка. Единицы уже введены"
            if self.number["ten"] != 0: self.err = f"Ошибка. Единицы должны быть \nв диапазоне от 0 до 9"
        else: self.err = ""

    def check_numbers(self, slovo):
        self.err = ""
        words = slovo.replace("et un", "etun").replace("et onze", "etonze").split(" ")
        words = [i.strip() for i in words if i.strip()]
        print(words)

        self.number = {"hundred" : 0, "ten" : 0, "unit" : 0}
        for i in range(len(words)):
            # self.raise_error(words[i])

            if self.in_hundreds(words[i]):
                if self.number["hundred"] == 0 and self.number["ten"] == 0 and self.number["unit"] == 0:
                    if i != 0:
                        self.err = f"Перед сотнями ничего не должно быть написано"
                        return self.number_sum()
                    self.number["hundred"] = self.hundreds[words[i]]
                
            elif self.in_tens(words[i]):
                if self.number["ten"] == 0 and self.number["unit"] == 0:
                    if (self.number["hundred"] != 0 and i != 1) or (self.number["hundred"] == 0 and i != 0):
                        self.err = "Перед десятками ничего ничего не должно быть написано"
                        return self.number_sum()
                    self.number["ten"] = self.tens[words[i]]  

            elif self.in_units(words[i]):
                if self.number["unit"] == 0:
                    if (self.number["hundred"] == 0 and self.number["ten"] == 0 and i != 0) or (((self.number["hundred"] != 0 and self.number["ten"] == 0) or (self.number["hundred"] == 0 and self.number["ten"] != 0)) and i != 1) or ((self.number["hundred"] != 0 and self.number["ten"] != 0) and i != 2):
                        self.err = "Перед единицами ничего не должно быть написано"
                        return self.number_sum()
                    
                    if self.number["ten"] != 0:
                        if self.number["ten"] == 70 or self.number["ten"] == 90:
                            if not self.units[words[i]] in range (11, 20): 
                                self.err = "После 70 и 90 допускаются только числа от 11 до 19"
                            else: self.number["unit"] = self.units[words[i]] - 10
                        elif self.units[words[i]] in range (0, 10):
                            self.number["unit"] = self.units[words[i]]
                        else: self.err =  f"Ошибка. Единицы должны быть в диапазоне от 0 до 9"
                    else:
                        self.number["unit"] = self.units[words[i]]
                else: self.raise_error(words[i])        
                            
            else: self.raise_error(words[i])

        return self.number_sum()
    
    
    def number_sum(self):
        print(self.number["hundred"], self.number["ten"], self.number["unit"])
        print(self.err)
        return (self.number["hundred"] + self.number["ten"] + self.number["unit"])

