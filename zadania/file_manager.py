class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        with open('./zadania/'+self.file_name, 'r') as file:
            data = file.read().replace('\n', '')
        return data

    def update_file(self, text_data):
        file_object = open('./zadania/'+self.file_name, 'a')
        file_object.write(text_data)
        file_object.close()
