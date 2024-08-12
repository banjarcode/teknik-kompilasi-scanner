# Impor library sly untuk lexer dan parser
from sly import Lexer, Parser

# Definisikan kelas Lexer
class CalculatorLexer(Lexer):
    tokens = {NUMBER, PLUS, MINUS, TIMES, DIVIDE, LPAREN, RPAREN}
    ignore = ' \t'

    # Definisikan token dengan regular expression
    NUMBER = r'\d+'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    LPAREN = r'\('
    RPAREN = r'\)'

# Definisikan kelas Parser
class CalculatorParser(Parser):
    tokens = CalculatorLexer.tokens

    # Aturan produksi untuk ekspresi matematika
    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
    )

    def __init__(self):
        self.env = {}

    @_('expr PLUS expr',
       'expr MINUS expr',
       'expr TIMES expr',
       'expr DIVIDE expr')
    def expr(self, p):
        if p[1] == '+':
            return p.expr0 + p.expr1
        elif p[1] == '-':
            return p.expr0 - p.expr1
        elif p[1] == '*':
            return p.expr0 * p.expr1
        elif p[1] == '/':
            return p.expr0 / p.expr1

    @_('NUMBER')
    def expr(self, p):
        return int(p.NUMBER)

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

if __name__ == '__main__':
    lexer = CalculatorLexer()
    parser = CalculatorParser()

    while True:
        try:
            text = input('Masukkan ekspresi matematika: ')
            result = parser.parse(lexer.tokenize(text))
            print(f'Hasil: {result}')
        except EOFError:
            break
