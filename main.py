# TODO: Bogenbeschreibeung?
# brauche ich nil und ende?
# 0 als alternative
# warum condition so gekurzt

from enum import Enum
import lexer_
from lexer_ import Morph


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
              Bogen("0", None, 7, 0),    #6        #ist das kein Prooblem? 0 steht fur ersten bogen UND fuer keinen bogen
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
              EndBogen("statement", None,0,0) #18
              ]

graphExpression = [Bogen("-", None, 1,5),#0
                   Bogen("term", None,2,0),#1
                   Bogen("0", None,3,0),#2
                   Bogen("+",None,4,5),#3
                   Bogen("term",None,2,0),#4
                   Bogen("-",None,6,8),#5
                   Bogen("term",None,2,0),#6
                   Bogen("term",None,2,0),#7
                   EndBogen("0", None, 0,0),#8
                   ]
graphTerm = [   Bogen("factor",None,1,0), #0
                Bogen("0", None, 2,0), #1
                Bogen("*",None,3,4), #2
                Bogen("factor",None,1,0), #3
                Bogen("/",None,5,6), #4
                Bogen("factor",None,1,0), #5
                EndBogen("0", None, 0,0), #6
             ]
graphStatement = [  Bogen("ident",None,1,3), #0
                    Bogen(":=",None,2,0), #1
                    Bogen("expression",None,0,0), #2 ENDBOGEN?
                    Bogen("IF",None,4,7), #3
                    Bogen("CONDITION",None,5,0), #4
                    Bogen("THEN",None,6,0), #5
                    Bogen("STATEMENT",None,0,0), #6 ENDBOGEN?
                    Bogen("WHILE",None,8,11), #7
                    Bogen("CONDITION",None,9,0), #8
                    Bogen("DO",None,10,0), #9
                    Bogen("STATEMENT", None, 0,0), #10 ENDBOGEN?
                    Bogen("BEGIN",None,12,15), #11
                    Bogen("STATEMENT",None, 13,0), #12
                    Bogen(";",None,12,14), #13
                    Bogen("END",None, 0 ,0), #14 ENDBOGEN?
                    Bogen("CALL",None,16,17), #15
                    Bogen("IDENT",None,0,0), #16 ENDBOGEN?
                    Bogen("?",None, 18,19), #17
                    Bogen("ident",None, 0,0), #18 ENDBOGEN?
                    Bogen("!", None, 20,21), #19
                    Bogen("EXPRESSION",None,0,0), #20 ENDBOGEN?
                    Bogen("0",None,0,0), #21 ENDBOGEN?
                  ]
graphCondition = [  Bogen("ODD",None,1,2), #0
                    Bogen("EXPRESSION",None,0,0), #1
                    Bogen("EXPRESSION",None,3,0), #2
                    Bogen("=",None,9,4), #3
                    Bogen("#",None,9,5), #4
                    Bogen("<",None,9,6), #5
                    Bogen(">",None,9,7), #6
                    Bogen("<=",None,9,8), #7
                    Bogen(">=",None,9,0), #8
                    Bogen("EXPRESSION",None,0,0), #9

]

def pars(bogen):
    pBog = bogen
    succ = 0
    morphem = Morph
    print(morphem)
    if morphem.MorphemCode == "":
        lexer_.lexer.lex()
    while True:


    return None

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
