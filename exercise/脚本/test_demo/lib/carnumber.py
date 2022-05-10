import random

while True:
    hanzi = ['粤','京','桂','云','湘','贵','川','辽','晋']

    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K','L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


    value_hanzi = "".join(random.sample(hanzi,1))
    print(value_hanzi)

    total_number = number + letter
    value_number = "".join(random.sample(total_number,5))

    zimu = "".join(random.sample(letter,1))

    car_number = value_hanzi + zimu + value_number
    print(car_number)
    with open('data.txt','w',encoding='utf-8') as fp:
            fp.write(car_number)

