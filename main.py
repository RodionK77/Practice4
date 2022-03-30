class HashTable:
    def __init__(self, size):
        self.list = [[] for _ in range(size)]

    # setitem и getitem для реализации, подобной встроенному dict, для поддержки синтаксиса ссылки на объект
    def __setitem__(self, key, value):
        f = False
        index = hash(key) % len(self.list)
        for i in range(len(self.list[index])):
            if self.list[index][i][0] == key:
                self.list[index][i] = (key, value)
                f = True
        if not f:
            self.list[index].append((key, value))

    def __getitem__(self, key):
        index = hash(key) % len(self.list)
        for i in range(len(self.list[index])):
            if self.list[index][i][0] == key:
                return self.list[index][i][1]
        return None

    def __len__(self):
        return sum(len(i) for i in self.list)

    def __iter__(self):
        for i in self.list:
            for key, value in i:
                yield key  # генератор, который на каждой итерации возвращает ключ


table = HashTable(100)
table[35] = 'Первый'
print(table[35])
print(len(table))
table[35] = 'НовыйПервый'
table['Индекс'] = [2, 4, 6, 8]
table[2] = 99
print(table[35])
print(table['35'])
print(table['Индекс'])
print(len(table), end='\n\n')
for key in table:
    print(key, table[key])
