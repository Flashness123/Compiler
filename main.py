# TODO: Bogenbeschreibeung?
# brauche ich nil und ende?
# 0 als alternative
# warum condition so gekurzt
# kein alternativBogen 0 mit -1 ersetzen

from enum import Enum
import lexer_
from lexer_ import Morph
from lexer_ import MorphemTyp


class bogenTyp(Enum):  # Bei Beck tBg
    BgNil = 0
    BgSymbol = 1
    BgMorphem = 2
    BgGraph = 4
    BgEnde = 8


class SymbolBogen:  # bei Beck tBog
    Typ = bogenTyp.BgSymbol
    Bogenbeschreibung = None
    Folgefunktion = None
    Folgebogen = None
    Alternativbogen = None
    def __init__(self, bogenbeschreibung, folgefunktion, folgebogen, alternativbogen):
        Typ = bogenTyp.BgSymbol  # (Ascii oder Wortsymbolcode aus enum)
        Bogenbeschreibung = bogenbeschreibung
        Folgefunktion = folgefunktion
        Folgebogen = folgebogen
        Alternativbogen = alternativbogen


class MorphemBogen:
    Typ = bogenTyp.BgMorphem
    Bogenbeschreibung = None
    Folgefunktion = None
    Folgebogen = None
    Alternativbogen = None
    def __init__(self, bogenbeschreibung, folgefunktion, folgebogen, alternativbogen):
        Typ = bogenTyp.BgMorphem  # Morphem
        Bogenbeschreibung = bogenbeschreibung
        Folgefunktion = folgefunktion
        Folgebogen = folgebogen
        Alternativbogen = alternativbogen


class GraphBogen:
    Typ = bogenTyp.BgGraph
    Bogenbeschreibung = None
    Folgefunktion = None
    Folgebogen = None
    Alternativbogen = None
    def __init__(self, bogenbeschreibung, folgefunktion, folgebogen, alternativbogen):
        Typ = bogenTyp.BgGraph  # Graph
        Bogenbeschreibung = bogenbeschreibung
        Folgefunktion = folgefunktion
        Folgebogen = folgebogen
        Alternativbogen = alternativbogen


class EndBogen:
    Typ = bogenTyp.BgEnde
    def __init__(self):
        Typ = bogenTyp.BgEnde  # Morphem

class NilBogen:
    Typ = bogenTyp.BgNil
    Folgefunktion = None
    def __init__(self, folgebogen):
        Typ = bogenTyp.BgNil
        Folgefunktion = folgebogen
    def __init__(self, folgefunktion,folgebogen):
        Typ = bogenTyp.BgNil
        Folgefunktion = folgefunktion
        Folgefunktion = folgebogen



class Parse():
    graphBlock = None
    graphExpression = None
    graphTerm = None
    graphFactor = None
    graphStatement = None
    graphCondition = None
    graphProgramm = None
    def __init__(self):


        graphFactor = [MorphemBogen(MorphemTyp.Ident, None, 5, 1), #0
                       MorphemBogen(MorphemTyp.Number, None, 5, 2),  #1
                       SymbolBogen("(", None, 3, -1),        #2
                       GraphBogen(self.graphExpression, None, 4, -1),     #3
                       SymbolBogen(")", None, 5, -1),        #4
                       EndBogen() #5
                       ]

        graphProgramm = [GraphBogen(self.graphBlock,None,1,-1), #0
                         SymbolBogen(".",None,2,-1), #1
                         EndBogen() #2
                         ]

                    #Typ    String  None Folge Alternative
        graphBlock = [SymbolBogen("CONST",None, 1, 6), #0
                      MorphemBogen(MorphemTyp.Ident, None, 2, -1),#1
                      SymbolBogen("=", None, 3, -1),    #2
                      MorphemBogen(MorphemTyp.Number, None, 4, -1),#3
                      SymbolBogen(",", None, 1, 5),    #4
                      SymbolBogen(";", None, 7, -1),    #5
                      NilBogen(7),    #6        #ist das kein Prooblem? 0 steht fur ersten bogen UND fuer keinen bogen
                      SymbolBogen("VAR", None, 8,11), #7
                      MorphemBogen("ident",None,9,-1),  #8
                      SymbolBogen(",",None,8,10),     #9
                      SymbolBogen(";", None, 12, -1),  #10
                      NilBogen(12),  #11
                      SymbolBogen("PROCEDURE", None, 13, 17),#12
                      MorphemBogen("ident", None, 14,-1),#13
                      SymbolBogen(";", None,15,-1),    #14
                      GraphBogen(self.graphBlock, None, 16,-1),#15
                      SymbolBogen(";", None, 12,-1),   #16
                      NilBogen(None,18), #17
                      GraphBogen("statement", None,19,-1), #18
                      EndBogen() #19
                      ]

        graphExpression = [SymbolBogen("-", None, 1,7),#0
                           GraphBogen(self.graphTerm, None,2,-1),#1
                           NilBogen(3),#2
                           SymbolBogen("+",None,4,5),#3
                           GraphBogen(self.graphTerm,None,2,-1),#4
                           SymbolBogen("-",None,6,8),#5 #ist das so richtig Endbogen nur als alternative
                           GraphBogen(self.graphTerm,None,2,-1),#6
                           GraphBogen(self.graphTerm,None,2,-1),#7
                           EndBogen(),#8
                           ]
        graphTerm = [   GraphBogen(self.graphFactor,None,1,-1), #0
                        NilBogen(2), #1
                        SymbolBogen("*",None,3,4), #2
                        GraphBogen(self.graphFactor,None,1,-1), #3
                        SymbolBogen("/",None,5,6), #4
                        GraphBogen(self.graphFactor,None,1,-1), #5
                        EndBogen(), #6
                     ]
        graphStatement = [  MorphemBogen("ident",None,1,3), #0
                            SymbolBogen(":=",None,2,-1), #1
                            GraphBogen(self.graphExpression,None,22,-1), #2 ENDBOGEN?
                            SymbolBogen("IF",None,4,7), #3
                            GraphBogen(self.graphCondition,None,5,-1), #4
                            SymbolBogen("THEN",None,6,-1), #5
                            GraphBogen(self.graphStatement,None,22,-1), #6 ENDBOGEN?
                            SymbolBogen("WHILE",None,8,11), #7
                            GraphBogen(self.graphCondition,None,9,-1), #8
                            SymbolBogen("DO",None,10,-1), #9
                            GraphBogen(self.graphStatement, None, 22,-1), #10 ENDBOGEN?
                            SymbolBogen("BEGIN",None,12,15), #11
                            GraphBogen(self.graphStatement,None, 13,-1), #12
                            SymbolBogen(";",None,12,14), #13
                            SymbolBogen("END",None, 22,-1), #14 ENDBOGEN?
                            SymbolBogen("CALL",None,16,17), #15
                            MorphemBogen("ident",None,22,-1), #16 ENDBOGEN?
                            SymbolBogen("?",None, 18,19), #17
                            MorphemBogen("ident",None, 22,-1), #18 ENDBOGEN?
                            SymbolBogen("!", None, 20,21), #19
                            GraphBogen(self.graphExpression,None,22,-1), #20 ENDBOGEN?
                            NilBogen(22), #21 ENDBOGEN?
                            EndBogen() #22
                          ]
        graphCondition = [  SymbolBogen("ODD",None,1,2), #0
                            GraphBogen(self.graphExpression,None,0,-1), #1
                            GraphBogen(self.graphExpression,None,3,-1), #2
                            SymbolBogen("=",None,9,4), #3
                            SymbolBogen("#",None,9,5), #4
                            SymbolBogen("<",None,9,6), #5
                            SymbolBogen(">",None,9,7), #6
                            SymbolBogen("<=",None,9,8), #7
                            SymbolBogen(">=",None,9,-1), #8
                            GraphBogen(self.graphExpression,None,10,-1), #9
                            EndBogen() #10

        ]

    def pars(bogen): #ich uebergebe einen Bogen
        pBog = bogen
        succ = 0
        morphem = Morph
        print(morphem)
        if morphem.MorphemTyp == None:
            lexer.lex()
            print("Nachstes token gelext")
        while True:
            print ("Schleife geentert")
            if pBog.Typ == bogenTyp.BgNil:
                print("Nilbogen")
                succ = 1
            if pBog.Typ == bogenTyp.BgSymbol:
                print("Symbolbogen")
            if pBog.Typ == bogenTyp.BgMorphem:
                print("Morphembogen")
            if pBog.Typ == bogenTyp.BgGraph:
                print("Graphbogen")
            if pBog.Typ == bogenTyp.BgEnde:
                print("Endbogen")
            return None
        return None

input_string = "while VAR := TSymbol; begin while true do begin"

lexer = lexer_.Lexer(input_string)
def main():
    print(lexer.Test())
    lex = lexer.lex()
    Parse.pars(GraphBogen)
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
