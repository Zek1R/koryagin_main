# Французский язык

# Алфавит ['A', ... , 'Z', '-', ' ']


class Translator:
    def __init__(self):
        self.alphabet= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', ' ']
        
        self.hundreds = {"cent" : 100,
                         "deux-cent" : 200,
                         "deuxcent" : 200,
                         "trois-cent" : 300,
                         "troiscent" : 300,
                         "quatre-cent" : 400,
                         "quatrecent" : 400,
                         "cinq-cent" : 500,
                         "cinqcent" : 500,
                         "six-cent" : 600,
                         "sixcent" : 600,
                         "sept-cent" : 700,
                         "septcent" : 700,
                         "huit-cent" : 800,
                         "huitcent" : 800,
                         "neuf-cent" : 900,
                         "neufcent" : 900}
        
        self.tens = {"vingt" : 20,
                     "trente" : 30,
                     "quarante" : 40,
                     "cinquante" : 50,
                     "soixante" : 60,
                     "soixante-dix" : 70,
                     "soixantedix" : 70,
                     "quatre-vingts" : 80,
                     "quatrevingts" : 80,
                     "quatre-vingts-dix" : 90,
                     "quatrevingtsdix" : 90}
        
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
                      "dix" : 10,
                      "onze" : 11,
                      "etonze" : 11,
                      "douze" : 12,
                      "treize" : 13,
                      "quatorze" : 14,
                      "quinze" : 15,
                      "seize" : 16,
                      "dix-sept" : 17,
                      "dixsept" : 17,
                      "dix-huit" : 18,
                      "dixhuit" : 18,
                      "dix-neuf" : 19,
                      "dixneuf" : 19}
                
        self.number = {"hundred" : 0, "ten" : 0, "unit" : 0}

        self.err = ""
        
    
    def validation(self, slovo):
        # print(f"Валидация слова: {slovo}")
        slovo = slovo.lower()
        for i in slovo:
            if i not in self.alphabet:
                self.err = f"Неверный символ {i}"
                # return self.number_sum()
                # print(f"split > {slovo[slovo.index(i)]}")
                slovo = slovo.split(i)[0]
                # print(f"Ошибка в слове: {slovo}")
                
        return slovo
    

    def in_hundreds(self, slovo):
        if slovo in self.hundreds: return True  
        return False
        
    def in_tens(self, slovo):
        if slovo in self.tens: return True  
        return False
    
    def in_units(self, slovo):
        if slovo in self.units: return True  
        return False

    
    def number_concatenation(self, words):
        
        for i in range(len(words)):
            n = False
            
            try:
                s = words[i] + words[i+1]

            except IndexError:
                if n == False:
                    # print(f"{words} обработано - ничего не найдено")
                    return words
                else:
                    self.number_concatenation(words)
            
            print(f"Слово = {s}")
            if self.in_hundreds(s):
                words[i] = s
                words.pop(i+1)
                n = True
                print(f"<<<{words[i]} in hundreds>>>")
            if self.in_tens(s):
                words[i] = s
                words.pop(i+1)
                n = True
                print(f"<<<{words[i]} in tens>>>")
            if self.in_units(s):
                words[i] = s
                words.pop(i+1)
                n = True
                print(f"<<<{words[i]} in units>>>")


    def check_numbers(self, slovo):
        self.err = ""
        slovo = self.validation(slovo)
        if slovo == "": return "Введите текст"
        words = slovo.split(" ")
        words = [i.strip() for i in words if i.strip()]
        
        words = self.number_concatenation(words)
            
        print(f"words: {words}")

        self.number = {"hundred" : 0, "ten" : 0, "unit" : 0}
        for i in range(len(words)):
            
            if self.in_hundreds(words[i]):
                if self.number["hundred"] == 0 and self.number["ten"] == 0 and self.number["unit"] == 0:
                    if i != 0:
                        self.err = f"Перед сотнями ничего не должно быть написано.\nСлово \"{words[i-1].upper()}\""
                        return self.number_sum()
                    self.number["hundred"] = self.hundreds[words[i]]
                else:
                    if self.number["hundred"] != 0: 
                        self.err = f"Сотни уже введены.\nСлово \"{words[i].upper()}\""
                        return self.number_sum()
                    else:
                        self.err = f"Перед сотнями ничего не должно стоять.\nСлово \"{words[i-1].upper()}\""
                        return self.number_sum()

            elif self.in_tens(words[i]):
                print(f"Проверка: {self.number["ten"] == 0 } {self.number["unit"] == 0}")
                if self.number["ten"] == 0 and self.number["unit"] == 0:
                    if (self.number["hundred"] != 0 and i != 1) or (self.number["hundred"] == 0 and i != 0):
                        self.err = f"Перед десятками ничего ничего не должно быть написано.\nСлово \"{words[i-1].upper()}\""
                        return self.number_sum()
                    self.number["ten"] = self.tens[words[i]]  
                else:
                    if self.number["ten"] != 0:
                        self.err = f"Десятки уже введены.\nСлово \"{words[i].upper()}\""
                        return self.number_sum()
                    else:
                        self.err = f"Перед десятками ничего не должно стоять.\nСлово \"{words[i-1].upper()}\""
                        return self.number_sum()

            elif self.in_units(words[i]):
                if self.number["unit"] == 0:
                    if (self.number["hundred"] == 0 and self.number["ten"] == 0 and i != 0) or \
                        (((self.number["hundred"] != 0 and self.number["ten"] == 0) or \
                        (self.number["hundred"] == 0 and self.number["ten"] != 0)) and i != 1) or \
                        ((self.number["hundred"] != 0 and self.number["ten"] != 0) and i != 2):
                        
                        self.err = f"Перед единицами ничего не должно быть написано.\nСлово \"{words[i-1].upper()}\""
                        return self.number_sum()
                    
                    if self.number["ten"] != 0:
                        if self.number["ten"] == 70 or self.number["ten"] == 90:
                            if not self.units[words[i]] in range (11, 20): 
                                self.err = f"После 70 и 90 допускаются только числа от 11 до 19.\nСлово \"{words[i].upper()}\""
                                return self.number_sum()
                            else: 
                                self.number["unit"] = self.units[words[i]] - 10
                                # print(self.units[words[i]] - 10)
                        else:
                            if self.units[words[i]] in range (0, 10):
                                self.number["unit"] = self.units[words[i]]
                            else:
                                self.err = f"Единицы должны быть в диапазоне от 0 до 9.\nСлово \"{words[i].upper()}\""
                                return self.number_sum()
                    else:
                        self.number["unit"] = self.units[words[i]]
                    
                    if (self.number["hundred"] != 0 or self.number["ten"]) != 0 and self.units[words[i]] == 0:
                        self.err = "Ноль нельзя использовать в составе числа"
                        return self.number_sum()
                else: 
                    if self.number["unit"] != 0: 
                        self.err = f"Единицы уже введены.\nСлово \"{words[i].upper()}\""
                        return self.number_sum()
                    else:
                        self.err = f"Перед единицами ничего не должно стоять.\nСлово \"{words[i-1].upper()}\""
                        return self.number_sum()
            else: self.err = ""

        return self.number_sum()
    
    
    def number_sum(self):
        res = ""
        # print(self.number["hundred"], self.number["ten"], self.number["unit"])
        # print(self.err)
        number = [self.number[i] for i in ("hundred", "ten", "unit") if self.number[i] != 0]
        print(f"NUMBER = {number}")
        if len(number) != 0:
            res = 0
            for i in number:
                res += i
        return res

