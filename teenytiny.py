from lex import Lexer

def main():
    source_code = "Hello World 343"
    lexer = Lexer(source_code)

    # check upto last character
    while lexer.peek() != '\0':
        print(lexer.curChar)
        lexer.nextChar()        # Next Character
main()
