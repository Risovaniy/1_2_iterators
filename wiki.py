import json
# from pprint import pprint


class Countries:
    def __init__(self, path):
        self.path = path
        self.file = json.load(open(self.path, encoding='utf-8'))
        self.start = 0
        self.end = len(self.file)
        self.name = self.file[self.start]["name"]["common"]

    def __iter__(self):
        return self

    def __next__(self):
        # print('.')
        self.start +=1
        if self.start == self.end:
            raise StopIteration
        self.name = self.file[self.start]["name"]["common"]
        return self


def fix_name(name):
    name = name.split()
    connector = '_'
    return connector.join(name)



with open('links.json', 'w') as f:
    for country in Countries('countries.json'):
        wiki = dict()
        wiki[country.name] = "https://ru.wikipedia.org/wiki/" + fix_name(country.name)
        json.dump(wiki, f, indent=2)