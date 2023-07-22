from lex import Lexer, TokenType
from parse import Parser
import sys

def main():
    print("Teeny Tiny Compiler\n")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()

    # Initialize the lexer and parser.
    lexer = Lexer(source)
    parser = Parser(lexer)

    parser.program() # Start the parser.
    print("\nParsing completed.")
main()
