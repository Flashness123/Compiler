# TODO: Bogenbeschreibeung?
# brauche ich nil und ende?
# 0 als alternative


from enum import Enum

import lexer_


class bogenTyp(Enum):  # Bei Beck tBg
    BgNil = 0
    BgSymbol = 1
    BgMorphem = 2
    BgGraph = 4
    BgEnde = 8


class SymbolBogen:  # bei Beck tBog
    def __init__(self, bogenbeschreibung, folgefunktion, folgebogen, alternativbogen):
        Typ = bogenTyp.BgSymbol  # (Ascii oder Wortsymbolcode aus enum)
        Bogenbeschreibung = bogenbeschreibung
        Folgefunktion = folgefunktion
        Folgebogen = folgebogen
        Alternativbogen = alternativbogen


class MorphemBogen:
    def __init__(self, bogenbeschreibung, folgefunktion, folgebogen, alternativbogen):
        Typ = bogenTyp.BgMorphem  # Morphem
        Bogenbeschreibung = bogenbeschreibung
        Folgefunktion = folgefunktion
        Folgebogen = folgebogen
        Alternativbogen = alternativbogen


class GraphBogen:
    def __init__(self, bogenbeschreibung, folgefunktion, folgebogen, alternativbogen):
        Typ = bogenTyp.BgGraph  # Graph
        Bogenbeschreibung = bogenbeschreibung
        Folgefunktion = folgefunktion
        Folgebogen = folgebogen
        Alternativbogen = alternativbogen


class EndBogen:
    def __init__(self, bogenbeschreibung, folgefunktion, folgebogen, alternativbogen):
        Typ = bogenTyp.BgEnde  # Morphem
        Bogenbeschreibung = bogenbeschreibung
        Folgefunktion = folgefunktion
        Folgebogen = folgebogen
        Alternativbogen = alternativbogen


graphFactor = [MorphemBogen("mcIdent", None, 5, 1), #0
               MorphemBogen("mcNumb", None, 5, 2),  #1
               SymbolBogen("(", None, 3, 0),        #2
               GraphBogen("gExpr", None, 4, 0),     #3
               SymbolBogen(")", None, 5, 0),        #4
               EndBogen("0", None, 0, 0)]           #5

graphProgramm = [Bogen("Block",None,1,0),
                 EndBogen(".",None,0,0)
                 ]

            #Typ    String  None Folge Alternative
graphBlock = [Bogen("CONST",None, 1, 6), #0
              Bogen("ident", None, 2, 0),#1
              Bogen("=", None, 3, 0),    #2
              Bogen("numeral", None, 4, 0),#3
              Bogen(",", None, 1, 5),    #4
              Bogen(";", None, 7, 0),    #5
              Bogen("0", None, 7, 0),    #6        #ist das keine Prooblem? 0 steht fur ersten bogen UND fuer keinen bogen
              Bogen("VAR", None, 8,11), #7
              Bogen("ident",None,9,0),  #8
              Bogen(",",None,8,10),     #9
              Bogen(";", None, 12, 0),  #10
              Bogen("0", None, 12, 0),  #11
              Bogen("PROCEDURE", None, 13, 17),#12
              Bogen("ident", None, 14,0),#13
              Bogen(";", None,15,0),    #14
              Bogen("block", None, 16,0),#15
              Bogen(";", None, 12,0),   #16
              Bogen("0", None, 18, 0 ), #17
              EndBogen("statement", None,0,0)
              ]

graphExpression = []
graphTerm = []
graphStatement = []
graphCondition = []


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
