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
        
        self.tens = {"dix" : 10,
                     "vingt" : 20,
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
                      "et-un" : 1,
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
                self.err = f"Неверный символ {i}.\nВам нужно использовать английский алфавит."
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
            try:
                s = words[i] + '-' + words[i+1]

            except IndexError:
                return words
               
            print(f"Слово = {s}")

            if self.in_hundreds(s):
                words[i] = s          
                words.pop(i+1)
                print(f"<<<{words[i]} in hundreds>>>")

            if self.in_tens(s):
                words[i] = s
                words.pop(i+1)
                try:
                    s = words[i] + '-' + words[i+1]
                    if self.in_tens(s):
                        words[i] = s
                        words.pop(i+1)
                        print("Тройное слово ебать:", words[i])
                except IndexError:                  
                    return words                
                print(f"<<<{words[i]} in tens>>>")

            if self.in_units(s):
                words[i] = s
                words.pop(i+1)
                print(f"<<<{words[i]} in units>>>")


    def check_numbers(self, slovo):
        self.err = ""
        slovo = self.validation(slovo)
        if slovo == "": return "Введите текст"
        words = slovo.split(" ")
        words = [i.strip() for i in words if i.strip()]
        
        words = self.number_concatenation(words)
            
        print(f"words: {words}")

        self.number = {"hundred" : "", "ten" : "", "unit" : ""}

        for i in range(len(words)):
            if self.err != "": break

            if self.in_hundreds(words[i]):
                if self.number["hundred"] == "" and self.number["ten"] == "" and self.number["unit"] == "":
                    if i != 0:
                        self.err = f"Перед сотнями ничего не должно быть написано."
                        # return self.number_sum()
                    else: 
                        self.number["hundred"] = self.hundreds[words[i]]
                else:
                    if self.number["ten"] == "" and self.number["unit"] == "" and self.number["hundred"] != "": 
                        self.err = f"Сотни не могут идти подряд"
                        # return self.number_sum()
                    else:
                        if self.in_tens(words[i-1]):
                            self.err = f"Сотни не могут идти после чисел десятичного"
                        else:
                            if self.number["unit"] > 9:
                                self.err = f"Сотни не могут идти после чисел формата 11-19."
                            else:
                                self.err = f"Сотни не могут идти после чисел единичного формата."                        
                        # retur n self.number_sum()е

            elif self.in_tens(words[i]):
                if self.number["ten"] == "" and self.number["unit"] == "":
                    if (self.number["hundred"] != "" and i != 1) or (self.number["hundred"] == "" and i != 0):
                        self.err = f"Перед десятками ничего не должно стоять."
                        # return self.number_sum()
                    else:
                        self.number["ten"] = self.tens[words[i]]  
                else:
                    if self.number["unit"] == "" and self.number["ten"] != "":
                        self.err = f"Числа десятичного формата не могут идти подряд"
                    else:
                        if self.number["unit"] > 9:
                            self.err = f"Числа десятичного формата не могут идти после:чисел формата 11-19"
                        else:
                            self.err = f"Числа десятичного формата не могут идти после: чисел единичного формата."

            elif self.in_units(words[i]):
                if self.number["unit"] == "":
                    if (self.number["hundred"] == "" and self.number["ten"] == "" and i != 0) or \
                        (((self.number["hundred"] != "" and self.number["ten"] == "") or \
                        (self.number["hundred"] == "" and self.number["ten"] != "")) and i != 1) or \
                        ((self.number["hundred"] != "" and self.number["ten"] != "") and i != 2):
                        
                        if self.units[words[i]] > 9:
                            self.err = f"Перед числами формата 11-19 ничего не должно быть написано."
                        else:
                            self.err = f"Перед единицами ничего не должно быть написано."
                        # return self.number_sum()
                    
                    if self.number["ten"] != "":
                        if self.number["ten"] == 70 or self.number["ten"] == 90 or self.number["ten"] == 10:
                            if self.number["ten"] == 10:
                                self.err = f"После 10 не допускается написание чисел.\nРекомендуется использовать числа формата 11-19"
                            else:    
                                if not self.units[words[i]] in range (11, 20): 
                                    self.err = f"После 70 и 90 допускаются только числа формата 11-19."
                                    # return self.number_sum()
                                else: 
                                    self.number["unit"] = self.units[words[i]] - 10
                                    # print(self.units[words[i]] - 10)
                        else:
                            if self.units[words[i]] in range (0, 9):
                                self.number["unit"] = self.units[words[i]]
                            else:
                                self.err = f"Допускаются только числа единичного формата"
                                # return self.number_sum()
                    else:
                        if self.err == "":
                            self.number["unit"] = self.units[words[i]]
                    
                    if (self.number["hundred"] != "" or self.number["ten"]) != "" and self.units[words[i]] == 0:
                        self.err = "Ноль нельзя использовать в составе числа"
                        # return self.number_sum()
                else: 
                    if self.number["unit"] != "": 
                        if self.units[words[i]] > 9:
                            if self.number["unit"] > 9:
                                self.err = f"Числа формата 11-19 не могут идти подряд."
                            else: self.err = f"Числа формата 11-19 не могут идти после чисел единичного формата."
                        else:
                            if self.number["unit"] > 9:
                                self.err = f"Числа единичного формата не могут идти после чисел формата 11-19."
                            else:
                                self.err = f"Числа единичного формата не могут идти подряд."
                        # return self.number_sum()
                    else:
                        self.err = f"Перед единицами ничего не должно стоять."
                        # return self.number_sum()
                    
            else: 
                self.err = f"Слово '{words[i]}' не распознано."
        print(f"Ошибки: {self.err}")
        if self.err != "":
            self.err = f"{self.err}\nПримерное положение слова: {i+1}"
            return ""
        return self.number_sum()
    
    
    def number_sum(self):
        res = ""
        # print(self.number["hundred"], self.number["ten"], self.number["unit"])
        # print(self.err)
        print(f"Сотни: {self.number["hundred"]}|Десятки: {self.number["ten"]}|Единицы: {self.number["unit"]}")
        number = [self.number[i] for i in ("hundred", "ten", "unit") if self.number[i] != ""]
        # print(f"NUMBER = {number}")
        if len(number) != 0:
            res = 0
            for i in number:
                res += i
        return res

