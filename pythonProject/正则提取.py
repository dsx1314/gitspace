import re

from cssutils.helper import string

f = open('dsx3.txt', 'r')

data = f.readlines()
print(data)



p = re.compile(r"'在停中(.*?)',")
f1 = open('dsx4.txt','w')
for line in p.findall(str(data)):
    print(line)
    f1.write(f'{line}\n')


f1.close()
print('-------success--------')