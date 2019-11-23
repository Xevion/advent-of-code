import os
import sys

import hashlib

PATH = os.path.join(sys.path[0], '..', 'input')
SALT = open(PATH).read()
md5_original = hashlib.md5(SALT.encode())


def find_key(START_WITH):
    i = 0
    while True:
        md5 = md5_original.copy()
        md5.update(str(i).encode())
        md5hash = md5.hexdigest()
        if md5hash.startswith(START_WITH):
            print(i)
            break
        i += 1

find_key('00000')
find_key('000000')