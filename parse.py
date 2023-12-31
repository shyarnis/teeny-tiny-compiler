import sys
from lex import TokenType 

# Parser object keeps track of current token and checks if the code matches the grammar.
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer

        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()    # Call this twice to initialize current and peek.

    # Return true if the current token matches.
    def checkToken(self, kind):
        return kind == self.curToken.kind

    # Return true if the next token matches.
    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    # Try to match current token. If not, error. Advances the current token.
    def match(self, kind):
        if not self.checkToken(kind):
            self.abort("Expected " + kind.name + ", got " + self.curToken.kind.name)
        self.nextToken()

    # Advances the current token.
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
        # No need to worry about passing the EOF, lexer handles that.
    
    def abort(self, message):
        sys.exit("Error. " + message)
    
    # Production rules.

    # program ::= {statement}
    def program(self):
        print("PROGRAM")

        # Parse all the statements in the program.
        while not self.checkToken(TokenType.EOF):
            self.statement()

    # statement ::= "PRINT" (expression | string) nl
    def statement(self):
        # Check the first token to see what kind of statement this is.

        # "PRINT" (expression | string)
        if self.checkToken(TokenType.PRINT):
            print("STATEMENT-PRINT")
            self.nextToken()

            if self.checkToken(TokenType.STRING):
                # Simple string.
                self.nextToken()
            else:
                # Expect an expression.
                self.expression()

        # "IF" comparison "THEN" nl {statement} "ENDIF" nl
        elif self.checkToken(TokenType.IF):
            print("STATEMENT-IF")
            self.nextToken()
            self.comparsion()
            self.match(TokenType.THEN)
            self.nl()
            
            # Zero or more statements in the body.
            while not self.checkToken(TokenType.ENDIF):
                self.statement()
            self.match(TokenType.ENDIF)

        # "WHILE" comparison "REPEAT" nl {statement nl} "ENDWHILE" nl
        elif self.checkToken(TokenType.WHILE):
            print("STATEMENT-WHILE")
            self.nextToken()
            self.comparison()
            self.match(TokenType.REPEAT)
            self.nl()

            # Zero or more statements in the body.
            while not self.checkToken(TokenType.ENDIF):
                self.statement()
            self.match(TokenType.ENDWHILE)

        # "LABEL" ident nl
        elif self.checkToken(TokenType.LABEL):
            print("STATEMENT-LABEL")
            self.nextToken()
            self.match(TokenType.IDENT)
        
        # "GOTO" ident nl
        elif self.checkToken(TokenType.GOTO):
            print("STATEMENT-GOTO")
            self.nextToken()
            self.match(TokenType.IDENT)
        
        # "LET" ident "=" expression nl
        elif self.checkToken(TokenType.LET):
            self.nextToken()
            self.match(TokenType.IDENT)
            self.match(TokenType.EQ)
            self.expression()
        
        # "INPUT" ident nl
        elif self.checkToken(TokenType.GOTO):
            print("STATEMENT-INPUT")
            self.nextToken()
            self.match(TokenType.IDENT)
        
        # This is not a valid statement. ERROR!!!
        else:
            # self.abort(f"Invalid statement at {self.curToken.text} + ( {self.curToken.kind.name} )")
            self.abort("Invalid statement at " + self.curToken.text + " (" + self.curToken.kind.name + ")")

        # Newline.
        self.nl()    
    
    # nl ::= '\n'+
    def nl(self):
        print("NEWLINE")
		
        # Require at least one newline.
        self.match(TokenType.NEWLINE)
        # But we will allow extra newlines too, of course.
        while self.checkToken(TokenType.NEWLINE):
            self.nextToken()