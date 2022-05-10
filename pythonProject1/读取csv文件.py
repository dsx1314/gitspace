import csv

def read_csv():
    file = 'F:\pythonProject1\dsx2.csv'

    with open(file) as f:
        read = csv.reader(f)
        header_row = next(read)

        for row in read:
            print(row)


if __name__ == '__main__':
    read_csv()
