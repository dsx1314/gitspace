import time
from os import system
import pytest

if __name__ == '__main__':
    pytest.main()
    time.sleep(2)
    ret = system('allure generate ./temps -o ./reports --clean')

    # ret_01 = system('allure open ./reports')


    # ret_server = system('allure serve out/result')

    # pytest.main(['-vs'])