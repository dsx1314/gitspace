import random


def get_pin(self):
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K',
              'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    total = number + letter

    Chinese_demo = ['粤', '京', '鲁', '贵', '云','津','沪','渝','冀','吉','辽','黑',
               '湘','鄂','甘','晋','陕','豫','川','桂','蒙','青','藏','新','宁','琼','闽','苏','浙','赣']



    # letter1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K',
    #            'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    f = open('dsx.txt','w')
    f.write('carnumber\n')
    for i in range(1000):
        u_len = random.randint(5,6)
        carnumber = ''.join([random.choice(total) for i in range(u_len)])
        # print(carnumber)

        p_len = random.randint(1,1)
        first_number = ''.join([random.choice(Chinese_demo) for i in range(p_len)])
        # print(first_number)


        t_len = random.randint(1,1)
        two_number = ''.join([random.choice(letter) for i in range(t_len)])
        # print(two_number)

        total_value = first_number + two_number + carnumber
        print(total_value)
        f.write(f'{total_value}\n')
    f.close()



if __name__ == '__main__':
    get_pin(self=None)
