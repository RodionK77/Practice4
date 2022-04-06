class Tag:
    def __init__(self, html, name):
        self.html = html
        self.name = name

    def __enter__(self):
        self.html.add("<{name}>\n".format(name=self.name))

    def __exit__(self, a, b, c):
        self.html.add("</{name}>\n".format(name=self.name))

class HTML():
    def __init__(self):
        self.code = list()

    def body(self):
        return Tag(self,'body')

    def div(self):
        return Tag(self, 'div')

    def p(self, str):
        self.code.append('<p>{s}</p>\n'.format(s=str))

    def add(self, code):
        self.code.append(code)

    def get_code(self):
        return "".join(self.code)


html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')
print(html.get_code())