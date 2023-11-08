# TODO: implement functions _fslb etc
#leerzeichen other?
# enum und automatentabelel ist durcheinanader - behoben aber was ist mit space
# ich mache noch nichts mit token[0] - behoben
# warum fb so behindert was ist mit zusatnd 2?
#habe endState auf 8 gesetzt


from enum import Enum
import lexer_

class bogenTyp(Enum):
    BgNil = 0
    BgSymbol = 1
    BgMorphem = 2
    BgGraph = 4
    BgEnde = 8


class Bogen:
    Typ: bogenTyp

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
