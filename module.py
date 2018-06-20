from os.path import isfile, splitext, basename

class Layout:
    def __init__(self):
        self.rus = "ё1234567890-=йцукенгшщзхъфывапролджэ\\ячсмитьбю.Ё!\"№;%:?*()_+ХЪЖЭ/БЮ,"
        self.eng = "`1234567890-=qwertyuiop[]asdfghjkl;'\\zxcvbnm,./~!@#$%^&*()_+{}:\"|<>?"
        self.text = None


    def get_text(self,text):
        self.text = text


    def view_result(self,text):
        print('Результат:',text)


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
        if data == list:
            self.text = "".join(data)
        else:
            return 1
        return 0



class File:
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
        with open(self.path_save,'w') as w:
            w.write(data)
        return self.path_save