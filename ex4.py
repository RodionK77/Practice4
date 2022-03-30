class Num:
    def __init__(self, num):
        self.num = num

    def calc(self):
        return self.num

    def stack(self):
        s = 'PUSH {n}'.format(n=self.num)
        return s

    def toString(self):
        return str(self.num)


class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def calc(self):
        return self.right.calc() + self.left.calc()

    def stack(self):
        s = '{one}\n{two}\nADD'.format(one=self.left.stack(), two=self.right.stack())
        return s

    def toString(self):
        s = '({one} + {two})'.format(one=self.left.toString(), two=self.right.toString())
        return s


class Sub:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def calc(self):
        return self.left.calc() - self.right.calc()

    def stack(self):
        s = '{one}\n{two}\nSUB'.format(one=self.left.stack(), two=self.right.stack())
        return s

    def toString(self):
        s = '({one} - {two})'.format(one=self.left.toString(), two=self.right.toString())
        return s


class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def calc(self):
        return self.right.calc() * self.left.calc()

    def stack(self):
        s = '{one}\n{two}\nMUL'.format(one=self.left.stack(), two=self.right.stack())
        return s

    def toString(self):
        s = '({one} * {two})'.format(one=self.left.toString(), two=self.right.toString())
        return s


class PrintVisitor:
    def visit(self, o):
        return o.toString()


class CalcVisitor:
    def visit(self, o):
        return o.calc()

class StackVisitor:
    def visit(self, o):
        return o.stack()

ast = Sub(Num(30), Add(Num(7), Mul(Num(3), Num(2))))
pv = PrintVisitor()
cv = CalcVisitor()
sv = StackVisitor()
print(pv.visit(ast))
print(cv.visit(ast))
print(sv.visit(ast))