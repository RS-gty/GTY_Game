import os


def encode(string: str, password: str) -> None:
    cmd = 'encode.exe' + ' ' + string + ' ' + password
    c = os.system(cmd)


def decode(password: str) -> None:
    cmd = 'decode.exe' + ' ' + password
    c = os.system(cmd)
