from cssutils.helper import string


def read_txt():
    f = open('dsx4.txt','r')
    a = list(f)
    print(a)

    if '\n' or '\\n\n' in a:
        a.pop()

if __name__ == '__main__':
    read_txt()