from openpyxl import load_workbook

def read_excel(file):
    wb = load_workbook(file)

    ws = wb['dsx']

    test_case = []
    addr = []

    for row in ws:
        addr.append(row[0].value)

    addr.pop(0)

    test_case.append(addr)
    return test_case[0]
    # print(test_case)


if __name__ == '__main__':
    test_carnumber = read_excel('1.xlsx')
    print(test_carnumber)

