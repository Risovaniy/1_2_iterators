import hashlib


class Countries:
    def __init__(self, path):
        self.path = path
        self.file = open(self.path)
        self.md5 = hashlib.md5(self.file.readline().encode()).hexdigest()

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            raise StopIteration
        self.md5 = hashlib.md5(line.encode()).hexdigest()
        return self.md5

#
# for file in Countries('links.json'):
#     print(file)