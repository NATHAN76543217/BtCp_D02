from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader('students.csv', header=False) as file:
        data = file.getdata()
        print("data = ", data)
        header = file.getheader()
        print("header = ", header)
    # with CsvReader('bad.csv') as file:
    #     if file == None:
    #         print("File is corrupted")
