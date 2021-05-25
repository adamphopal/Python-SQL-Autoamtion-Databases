'''
Video Tutorial:
https://youtu.be/Dq7yHiCjKrA

Description:
Automatically visit certain websites, wait so long, then close the tabs.
'''

import sys
import webbrowser
import time
#from pykeyboard import InlineKeyboard
from pykeyboard import PyKeyboard
#from pymouse import PyMouse


count = 0
urls = ['https://www.youtube.com/watch?v=HGOBQPFzWKo&t=10049s&ab_channel=freeCodeCamp.org','https://www.youtube.com/watch?v=kQDxmjfkIKY&list=PL_557Q1uZ7gLM0QMIWJLaNX5b1QVqb2EO&index=3&ab_channel=CodDevX','https://www.youtube.com/watch?v=Sa_kQheCnds&list=PL_557Q1uZ7gLM0QMIWJLaNX5b1QVqb2EO&index=118&ab_channel=CoreySchafer','https://pythonspot.com/beginner/','https://www.interviewcake.com/data-structures-reference','https://github.com/okeeffed/cheat-sheets/blob/master/Python-Data-Structures.md','https://www.youtube.com/watch?v=p65AHm9MX80&ab_channel=freeCodeCamp.org','https://www.youtube.com/watch?v=7lmCu8wz8ro&list=PL_557Q1uZ7gLM0QMIWJLaNX5b1QVqb2EO&index=82&ab_channel=CodingTech','Django rest api: https://www.youtube.com/watch?v=A4zqqjLhDgU&list=PL8GFhcuc_fW4cxdkRtWIlln1DQ3CZwQen&index=12']
k = PyKeyboard()

while count < 1:
    for url in urls:
        webbrowser.open(url, new=0)
        time.sleep(5)
        k.press_keys(['Command','W'])
        count = count + 1

else:
    pass
