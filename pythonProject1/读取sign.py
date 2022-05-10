import hashlib

def compute(message):
    m = hashlib.md5()
    m.update(message.encode(encoding='utf-8'))
    return m.hexdigest()


if __name__ == '__main__':
    str = '12345678909876543|{"parkingId":"qp31022900183","plateId":"皖AP1851","dataTime":1507863248063}'

    print(compute(str))