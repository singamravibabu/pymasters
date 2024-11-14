class FileManager:
    def __init__(self, filename):
        self.filename = filename
        
    def write_data(self, data):
        with open(self.filename, "w") as file:
            file.write(data)
            
    def read_data(self):
        with open(self.filename, "r") as file:
            return file.read()
        
# Using the FileManager class
file_manager = FileManager("sample.txt")
file_manager.write_data("Hello, World!")
print(file_manager.read_data())         # Output: Hello, World!