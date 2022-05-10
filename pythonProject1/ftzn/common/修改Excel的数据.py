import xlrd
from xlutils.copy import copy

from ftzn.common.读取txt import read_txt
def remove_demo():
    rb = xlrd.open_workbook('F:\\pythonProject1\\ftzn\\data\\carnumber.xls')
    wb = copy(rb)
    ws = wb.get_sheet(0)
    for i in range(1,101):
        ws.write(i ,0,read_txt()[i-1])

    wb.save('F:\\pythonProject1\\ftzn\\data\\carnumber.xls')

if __name__ == '__main__':
    remove_demo()