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
urls = ['https://yandex.com/images/','https://osxdaily.com/2018/10/20/how-list-all-homebrew-packages-installed-mac/','https://osxdaily.com/2018/07/29/uninstall-packages-homebrew-mac/','https://osxdaily.com/2018/03/26/best-homebrew-packages-mac/','https://github.com/austin-taylor/code-vault/blob/master/python_expert_notebook.ipynb','https://simpleisbetterthancomplex.com/series/2017/10/16/a-complete-beginners-guide-to-django-part-7.html']
k = PyKeyboard()

while count < 1:
    for url in urls:
        webbrowser.open(url, new=0)
        time.sleep(5)
        k.press_keys(['Command','W'])
        count = count + 1

else:
    pass
