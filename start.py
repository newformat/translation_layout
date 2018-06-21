#!/usr/bin/env python3
import sys
from module import *
result = None
''' Файл запуска '''
layout = Layout()
file = File()
if __name__ == "__main__":
    if len(sys.argv) > 1 and len(sys.argv) < 5:
        # комбинации ключей в работе с файлом
        if sys.argv[1] == '-eng' and ('-path' in sys.argv) and len(sys.argv) == 4:
            if file.path_exists(sys.argv[-1]): exit(1)
            if layout.read_file(file.open_file()): print('данные не верны'); exit(1)
            result = layout.eng_to_rus()
        elif sys.argv[1] == '-rus' and ('-path' in sys.argv) and len(sys.argv) == 4:
            if file.path_exists(sys.argv[-1]): exit(1)
            if layout.read_file(file.open_file()): print('данные не верны'); exit(1)
            result = layout.rus_to_eng()

        if result != None:
            status = file.save_file(result)
            layout.view_result("сохранено в текущей папке - " + status); exit(0) if type(status) == str else exit(1)

        # комбинации ключей без файла
        layout.get_text(sys.argv[-1])
        if sys.argv[1] == '-eng' and len(sys.argv) == 3:
            result = layout.eng_to_rus()
        elif sys.argv[1] == '-rus' and len(sys.argv) == 3:
            result = layout.rus_to_eng()
        elif len(sys.argv) == 2 and (not '-rus' in sys.argv ) and (not '-eng' in sys.argv) and (not '-path' in sys.argv):
            result = layout.auto_translate()
        else:
            print('неверный порядок параметров')
            exit(1)
        layout.view_result(result)
    else:
        print('отсутствуют параметры или их много')


