# TODO: implement functions _fslb etc
#leerzeichen other?
# enum und automatentabelel ist durcheinanader - behoben aber was ist mit space
# ich mache noch nichts mit token[0] - behoben
# warum fb so behindert was ist mit zusatnd 2?

#habe endState auf 8 gesetzt
import lexer_

def main():
    input_string = "while VAR := TSymbol; begin while true do begin"

    lexer = lexer_.Lexer(input_string)
    print(lexer.Test())
    tokens = []
    types = []
    lex = lexer.lex()
    tokens.append(lex.Value)
    print("Tokens: ")
    print(tokens)
    """lex = lexer.lex()
    tokens.append(lex.Value)
    print("Tokens: ")
    print(tokens)
    lex = lexer.lex()
    tokens.append(lex.Value)
    print("Tokens: ")
    print(tokens)"""

    return -1

# Testen des Interpreters
if __name__ == '__main__':
    main()
