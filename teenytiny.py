from lex import Lexer, TokenType

def main():
    # source_code = "+ - * /"
    # source_code = "+ - * / > >= = != !"
    # source_code = "#This will be ignored\n"
    # source_code = "\"String = 13\" != +"
    # source_code = "2+3=5"
    # source_code = "2.45 + 3.55 = 6.00"
    # source_code = "IF foo THEN bar"
    source_code = "PRINT\"Hello, World\" > 4.5"

    lexer = Lexer(source_code)
    
    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()
main()
