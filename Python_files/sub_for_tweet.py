from inspect import getsource
from inspect import getfile
from inspect import getmodule
from encrypt import encrypt, decrypt, getKey
from getpass import getpass


print(getmodule(encrypt))
print(getfile(encrypt))


print(getsource(encrypt))
