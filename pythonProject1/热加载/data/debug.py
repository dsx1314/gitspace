import random

def rand_str():
    return str(random.randint(1000000,2000000))


if __name__ == '__main__':
    print(rand_str())