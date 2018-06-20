#!/usr/bin/env python3
import sys
from module import *
result = None
''' Файл запуска '''
layout = Layout()
if __name__ == "__main__":
    if len(sys.argv) > 1 and len(sys.argv) < 5:

        if sys.argv[1] == '-eng' and sys.argv[2] == '-path' and len(sys.argv) == 4:
            pass
        elif sys.argv[1] == '-rus' and sys.argv[2] == '-path' and len(sys.argv) == 4:
            pass

        layout.get_text(sys.argv[-1])
        if sys.argv[1] == '-eng':
            result = layout.eng_to_rus()
        elif sys.argv[1] == '-rus':
            result = layout.rus_to_eng()
        else:
            result = layout.auto_translate()
        layout.view_result(result)
    else:
        print('отсутствуют параметры или их много')


