import os

sentence = 'This/is/a/sentence/for/testing'
password = 't'

cmd1 = 'encode.exe' + ' ' + sentence + ' ' + password
aa = os.system(cmd1)
cmd2 = 'decode.exe' + ' ' + password
a = os.system(cmd2)
