#print("hello")

# while True:
#     text = input('basic>')
#     print(text)


class Token: 
    def __init__(self, type_ , value):  
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}: {self.value}'
        return f'{self.type}'

class Lexer: 
    def __init__(self, text):
        self.text = text 
        self.pos = -1 
        self.current_char = None
        self.advance()
    
    def advance(self): 
        self.pos += 1 
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

token = Token('TT_INT', 2)
print(token)

lexer = Lexer('1 + 2')
lexer.advance()
