class Filereader:
    def __init__(self, filename):
        self.filename = filename
        self.data = ""  # initialize

    def read_and_write(self):
        f = open(self.filename, "r", encoding="utf-8")
        self.data = f.read()  # store in self.data
        print(self.data)
        f.close()

    def count(self):
        if self.data:
            star_count = self.data.count('*')  # count '*' characters
            print(f"\nNumber of '*' characters: {star_count}")
        else:
            print("No data to count. Please read the file first.")


# Usage
reader = Filereader("demo_file.txt")
reader.read_and_write()  # Read and print file
reader.count()           # Count '*' characters
