#learn class, consider cookie cutter as a class

class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

monaco_cookie = Cookie('Yellow')
parle_cookie = Cookie('Red')

print('monaco cookie color is', monaco_cookie.get_color())
print('parle cookie color is', parle_cookie.get_color())

parle_cookie.set_color('brown')

print('monaco cookie color is', monaco_cookie.get_color())
print('parle cookie color is', parle_cookie.get_color())