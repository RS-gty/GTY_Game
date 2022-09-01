import sys


filename = sys.argv[1]
f = open(filename)
f.close()


def encode(string: str, password: str):
    password1 = 1
    if len(password) > 1:
        for i in password:
            password1 *= ord(i)
    else:
        password1 = ord(password)
    output = ''
    out = ''
    for i in string:
        if len(str(ord(i) + password1)) > 2:
            output += str(ord(i) + password1)[::-1]
            out += str(ord(i) + password1)[::-1] + '|'
        else:
            output += ('0' + str(ord(i) + password1))[::-1]
            out += ('0' + str(ord(i) + password1))[::-1] + '|'
    return int(output + str(len(out.split('|')[0])))


def decode(integer: int, password: str):
    password1 = 1
    if len(password) > 1:
        for i in password:
            password1 *= ord(i)
    else:
        password1 = ord(password)
    r = str(integer)[0:-1]
    n = 1
    m = ''
    l1 = []
    l2 = []
    output = ''
    for i in str(integer):
        if n % int(str(integer)[-1]) == 0:
            m += i
            l1.append(m)
            m = ''
        else:
            m += i
        n += 1
    for i in l1:
        l2.append(int(i[::-1])-password1)
    for i in l2:
        output += chr(i)
    return output


string_coding = 'Custom Theme'
password_ = '$%%#%'


