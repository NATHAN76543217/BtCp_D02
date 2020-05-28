class CsvReader():
    """
        My context Manager for Csv files
    """
    def __init__(
                self, filename=None, sep=',', header=False,
                skip_top=0, skip_bottom=0):
        self.file = None
        self.filename = filename
        self.sep = sep
        self.data = None
        self.header = None
        self.need_header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        print("-->Enter in the with statemment")
        try:
            self.file = open(self.filename, "r")
            mon_contenue = self.file.read()
            print(mon_contenue)
            self.data = []
            mon_contenue = mon_contenue.split()
            print(mon_contenue)
            if self.need_header:
                self.need_header = False
                self.header = mon_contenue[0]
                mon_contenue.remove(self.header)
            for line in mon_contenue:
                line = line
                self.data.append(line)

        except FileNotFoundError:
            print("File \"{}\" not found!!".format(self.filename))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        print("<--Exiting with statement")

    def getdata(self):
        return self.data

    def getheader(self):
        return self.header
