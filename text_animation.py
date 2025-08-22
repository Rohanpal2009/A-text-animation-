import string
import time
text = "hello world i am a coder!"
temp = ""
for ch in text:
    for i in string.printable:
        if i == ch or ch == i:
            time.sleep(0.2)
            print(temp+i)
            temp +=ch
            break
        else:
            time.sleep(0.02)
            print(temp+i)

