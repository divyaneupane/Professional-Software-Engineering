class Filereader:
    def __init__(self, filename):
        self.filename = filename
        self.data = ""

    def read_and_write(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            self.data = f.read()
        print("File content:\n")
        print(self.data)

    def count(self):
        if self.data:
            star_count = self.data.count('*')
            print(f"\nNumber of '*' characters: {star_count}")
        else:
            print("No data to count. Please read the file first.")

    def append(self):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write("\n--- End of File ---\n")
        print("Text added successfully!")

def main():
        # Usage
    reader = Filereader("demo_file.txt")
    reader.read_and_write()  # Read and print file
    reader.count()           # Count '*' characters
    reader.append()
    
    
if __name__ == "__main__":
    main()