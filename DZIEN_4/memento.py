class Memento:
    def __init__(self,file,content):
        self.file = file
        self.content = content


class FileWriterUtility:
    def __init__(self,file):
        self.file = file
        self.content = ""

    def write(self,string):
        self.content += string

    def save(self):
        return Memento(self.file,self.content)

    def undo(self,memento):
        self.content = memento.content


class FileWriteCretaker:
    def save(self,writer):
        self.obj = writer.save()

    def undo(self,writer):
        writer.undo(self.obj)

if __name__ == '__main__':
    caretaaker = FileWriteCretaker()
    writer = FileWriterUtility("info.txt")
    writer.write("Pierwsza odsłona pliku info...\n")
    print(writer.content +"\n")
    caretaaker.save(writer)

    print("_"*50)
    writer.write("druga wersja zawartości...")
    print(writer.content + "\n")

    print("_"*50)
    caretaaker.undo(writer)
    print(writer.content + "\n")
