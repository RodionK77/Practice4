
class SomeClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def mul(self):
        return self.a * self.b * self.c


test = SomeClass(10, 20, 30)
for key, value in test.__dict__.items():
    print(key, ':', value)

print(getattr(test, 'mul')())
