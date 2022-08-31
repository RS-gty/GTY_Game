s = input()
t = ''
for c in s:
    if 'a' <= c <= 'z':
        t += chr(ord('a') + ((ord(c) - ord('a')) + 3) % 26)
    elif 'A' <= c <= 'Z':
        t += chr(ord('A') + ((ord(c) - ord('A')) + 3) % 26)
    else:
        t += c  # t+=是实现了两个字符相加，eg：输入abc第一次循环t = d，第二次循环t = de，第三次循环t = def
print(t)
