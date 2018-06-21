from os.path import isfile, splitext, basename

class Layout:
    ''' Работа с текстом раскладки
    attributes:
        rus     русская раскладка
        eng     английская раскладка
        text    текст перевода
    methods:
        get_text        получить текст
        view_result     результта перевода
        eng_to_rus      с англ. на рус. раскладку текста
        rus_to_eng      c рус. на англ. раскладку текста
        auto_translate  автоматическое определение языка
        translate_txt   процесс перевода текста
        read_file       загрузка текста из файла.
    '''
    def __init__(self):
        self.rus = "ё1234567890-=йцукенгшщзхъфывапролджэ\\ячсмитьбю.Ё!\"№;%:?*()_+ХЪЖЭ/БЮ,"
        self.eng = "`1234567890-=qwertyuiop[]asdfghjkl;'\\zxcvbnm,./~!@#$%^&*()_+{}:\"|<>?"
        self.text = None


    def get_text(self,text):
        self.text = text


    def view_result(self,text):
        print('Результат: \"'+text+'\"')


    def eng_to_rus(self):
        abc_all = [
            list(self.eng),
            list(self.rus)]
        return self.translate_txt(abc_all)


    def rus_to_eng(self):
        abc_all = [
            list(self.rus),
            list(self.eng)]
        return self.translate_txt(abc_all)


    def auto_translate(self):
        for ch in self.text:
            if ch in list(self.rus[13:46]):
                return self.rus_to_eng()
            elif ch in list(self.eng[13:44]):
                return self.eng_to_rus()
        return "[ текста для перевода нет ]"


    def translate_txt(self, abc):
        text = ''
        for ch in self.text:
            for i in range(0,len(abc[0])):
                if ch == abc[0][i]:
                    text+=abc[1][i]
                    break
                elif ch == abc[0][i].upper():
                    text += abc[1][i].upper()
                    break
                elif ch == ' ':
                    text+=' '
                    break
                elif ch == "\n":
                    text+="\n"
                    break
        return text


    def read_file(self, data):
        if type(data) == list:
            self.text = "".join(data)
        else:
            return 1
        return 0



class File:
    ''' Работа с файлом
    attributes:
        path_file   путь к файлу
        path_save   путь сохранения результата
    methods:
        path_exists     проверяет путь к файлу
        type_file       проверка файла на его тип через расширение
        open_file       открытие и чтение файла в список
        save_file       сохранение файла с результатом перевода
    '''
    def __init__(self):
        self.path_file = None
        self.path_save = './'


    def path_exists(self, path):
        if isfile(path):
           self.path_file = path
        else:
            print('неверный путь к файлу')
            return 1
        return 0


    def type_file(self):
        path, vtype = splitext(self.path_file)
        if vtype == '.txt':
            return 0
        else:
            print('неверный тип файла')
            return 1


    def open_file(self):
        if not self.type_file():
            with open(self.path_file,'r') as r:
                return r.readlines()
        else:
            return 1


    def save_file(self,data):
        self.path_save += basename(splitext(self.path_file)[0]) + '_save.txt'
        if not isfile(self.path_save):
            with open(self.path_save,'w') as w:
                w.write(data)
            return self.path_save
        else:
            print('Файл уже существует')
            return False
