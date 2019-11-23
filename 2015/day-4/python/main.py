import os
import sys

import hashlib

PATH = os.path.join(sys.path[0], '..', 'input')
SALT = 'bgvyzdsv'
md5 = hashlib.md5()

i = 0
while True:
    md5.update((SALT + str(i)).encode())
    if md5.hexdigest().startswith('00000'):
        print(i)
        break
    i += 1