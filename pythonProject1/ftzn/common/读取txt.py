def read_txt():
    f = open('F:\\pythonProject1\\ftzn\data\\carnumber.txt' ,'r')

    a = list(f)
    return a

if __name__ == '__main__':
    print(read_txt())