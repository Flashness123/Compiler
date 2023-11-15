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
        self.Typ = bogenTyp.BgSymbol  # (Ascii oder Wortsymbolcode aus enum)
        self.Bogenbeschreibung = bogenbeschreibung
        self.Folgefunktion = folgefunktion
        self.Folgebogen = folgebogen
        self.Alternativbogen = alternativbogen


class MorphemBogen:
    Typ = bogenTyp.BgMorphem
    Bogenbeschreibung = None
    Folgefunktion = None
    Folgebogen = None
    Alternativbogen = None
    def __init__(self, bogenbeschreibung, folgefunktion, folgebogen, alternativbogen):
        self.Typ = bogenTyp.BgMorphem  # Morphem
        self.Bogenbeschreibung = bogenbeschreibung
        self.Folgefunktion = folgefunktion
        self.Folgebogen = folgebogen
        self.Alternativbogen = alternativbogen


class GraphBogen:
    Typ = bogenTyp.BgGraph
    Bogenbeschreibung = None
    Folgefunktion = None
    Folgebogen = None
    Alternativbogen = None
    def __init__(self, bogenbeschreibung, folgefunktion, folgebogen, alternativbogen):
        self.Typ = bogenTyp.BgGraph  # Graph
        self.Bogenbeschreibung = bogenbeschreibung
        self.Folgefunktion = folgefunktion
        self.Folgebogen = folgebogen
        self.Alternativbogen = alternativbogen


class EndBogen:
    Typ = bogenTyp.BgEnde
    def __init__(self):
        self.Typ = bogenTyp.BgEnde  # Morphem

class NilBogen:
    Typ = bogenTyp.BgNil
    Folgefunktion = None
    def __init__(self, folgebogen):
        self.Typ = bogenTyp.BgNil
        self.Folgefunktion = folgebogen
    # def __init__(self, folgefunktion,folgebogen):
    #     Typ = bogenTyp.BgNil
    #     Folgefunktion = folgefunktion
    #     Folgefunktion = folgebogen



class Parse():
    graphBlock = [-1]
    graphExpression = [-1]
    graphTerm = [-1]
    graphFactor = []
    graphStatement = [-1]
    graphCondition = [-1]
    graphProgramm = [-1]
    def __init__(self):


        self.graphFactor = [MorphemBogen(MorphemTyp.Ident, None, 5, 1), #0
                       MorphemBogen(MorphemTyp.Number, None, 5, 2),  #1
                       SymbolBogen("(", None, 3, -1),        #2
                       GraphBogen(self.graphExpression[0], None, 4, -1),     #3
                       SymbolBogen(")", None, 5, -1),        #4
                       EndBogen() #5
                       ]

                    #Typ    String  None Folge Alternative
        self.graphBlock = [SymbolBogen("CONST",None, 1, 6), #0
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
                      GraphBogen(self.graphBlock[0], None, 16,-1),#15
                      SymbolBogen(";", None, 12,-1),   #16
                      #NilBogen(None,18), #17
                      NilBogen(18),
                      GraphBogen(self.graphStatement[0], None,19,-1), #18
                      EndBogen() #19
                      ]


        self.graphExpression = [SymbolBogen("-", None, 1,7),#0
                           GraphBogen(self.graphTerm[0], None,2,-1),#1
                           NilBogen(3),#2
                           SymbolBogen("+",None,4,5),#3
                           GraphBogen(self.graphTerm[0],None,2,-1),#4
                           SymbolBogen("-",None,6,8),#5 #ist das so richtig Endbogen nur als alternative
                           GraphBogen(self.graphTerm[0],None,2,-1),#6
                           GraphBogen(self.graphTerm[0],None,2,-1),#7
                           EndBogen(),#8
                           ]
        self.graphTerm = [   GraphBogen(self.graphFactor[0],None,1,-1), #0
                        NilBogen(2), #1
                        SymbolBogen("*",None,3,4), #2
                        GraphBogen(self.graphFactor[0],None,1,-1), #3
                        SymbolBogen("/",None,5,6), #4
                        GraphBogen(self.graphFactor[0],None,1,-1), #5
                        EndBogen(), #6
                     ]
        self.graphStatement = [  MorphemBogen("ident",None,1,3), #0
                            SymbolBogen(":=",None,2,-1), #1
                            GraphBogen(self.graphExpression[0],None,22,-1), #2 ENDBOGEN?
                            SymbolBogen("IF",None,4,7), #3
                            GraphBogen(self.graphCondition[0],None,5,-1), #4
                            SymbolBogen("THEN",None,6,-1), #5
                            GraphBogen(self.graphStatement[0],None,22,-1), #6 ENDBOGEN?
                            SymbolBogen("WHILE",None,8,11), #7
                            GraphBogen(self.graphCondition[0],None,9,-1), #8
                            SymbolBogen("DO",None,10,-1), #9
                            GraphBogen(self.graphStatement[0], None, 22,-1), #10 ENDBOGEN?
                            SymbolBogen("BEGIN",None,12,15), #11
                            GraphBogen(self.graphStatement[0],None, 13,-1), #12
                            SymbolBogen(";",None,12,14), #13
                            SymbolBogen("END",None, 22,-1), #14 ENDBOGEN?
                            SymbolBogen("CALL",None,16,17), #15
                            MorphemBogen("ident",None,22,-1), #16 ENDBOGEN?
                            SymbolBogen("?",None, 18,19), #17
                            MorphemBogen("ident",None, 22,-1), #18 ENDBOGEN?
                            SymbolBogen("!", None, 20,21), #19
                            GraphBogen(self.graphExpression[0],None,22,-1), #20 ENDBOGEN?
                            NilBogen(22), #21 ENDBOGEN?
                            EndBogen() #22
                          ]
        self.graphCondition = [  SymbolBogen("ODD",None,1,2), #0
                            GraphBogen(self.graphExpression[0],None,0,-1), #1
                            GraphBogen(self.graphExpression[0],None,3,-1), #2
                            SymbolBogen("=",None,9,4), #3
                            SymbolBogen("#",None,9,5), #4
                            SymbolBogen("<",None,9,6), #5
                            SymbolBogen(">",None,9,7), #6
                            SymbolBogen("<=",None,9,8), #7
                            SymbolBogen(">=",None,9,-1), #8
                            GraphBogen(self.graphExpression[0],None,10,-1), #9
                            EndBogen() #10
        ]
        self.graphProgramm = [GraphBogen(self.graphBlock[0],None,1,-1), #0
                         SymbolBogen(".",None,2,-1), #1
                         EndBogen() #2
                         ]
        self.reInit()

    def reInit(self):
        print("-----------reInit Called------------------")
        self.graphFactor = [MorphemBogen(MorphemTyp.Ident, None, self.graphFactor[5], self.graphFactor[1]), #0
                       MorphemBogen(MorphemTyp.Number, None, self.graphFactor[5], self.graphFactor[2]),  #1
                       SymbolBogen("(", None, self.graphFactor[3], -1),        #2
                       GraphBogen(self.graphExpression[0], None, self.graphFactor[4], -1),     #3
                       SymbolBogen(")", None, self.graphFactor[5], -1),        #4
                       EndBogen() #5
                       ]

                    #Typ    String  None Folge Alternative
        self.graphBlock = [SymbolBogen("CONST",None, self.graphBlock[1], self.graphBlock[6]), #0
                      MorphemBogen(MorphemTyp.Ident, None, self.graphBlock[2], -1),#1
                      SymbolBogen("=", None, self.graphBlock[3], -1),    #2
                      MorphemBogen(MorphemTyp.Number, None, self.graphBlock[4], -1),#3
                      SymbolBogen(",", None, self.graphBlock[1], self.graphBlock[5]),    #4
                      SymbolBogen(";", None, self.graphBlock[7], -1),    #5
                      NilBogen(self.graphBlock[7]),    #6        #ist das kein Prooblem? 0 steht fur ersten bogen UND fuer keinen bogen
                      SymbolBogen("VAR", None, self.graphBlock[8],self.graphBlock[11]), #7
                      MorphemBogen("ident",None,self.graphBlock[9],-1),  #8
                      SymbolBogen(",",None,self.graphBlock[8],self.graphBlock[10]),     #9
                      SymbolBogen(";", None, self.graphBlock[12], -1),  #10
                      NilBogen(self.graphBlock[12]),  #11
                      SymbolBogen("PROCEDURE", None, self.graphBlock[13], self.graphBlock[17]),#12
                      MorphemBogen("ident", None, self.graphBlock[14],-1),#13
                      SymbolBogen(";", None,self.graphBlock[15],-1),    #14
                      GraphBogen(self.graphBlock[0], None, self.graphBlock[16],-1),#15
                      SymbolBogen(";", None, self.graphBlock[12],-1),   #16
                      #NilBogen(None,18), #17
                      NilBogen(self.graphBlock[18]),#17
                      GraphBogen(self.graphStatement[0], None,self.graphBlock[19],-1), #18
                      EndBogen() #19
                      ]

        self.graphExpression = [SymbolBogen("-", None, self.graphExpression[1],self.graphExpression[7]),#0
                           GraphBogen(self.graphTerm[0], None,self.graphExpression[2],-1),#1
                           NilBogen(self.graphExpression[3]),#2
                           SymbolBogen("+",None,self.graphExpression[4],self.graphExpression[5]),#3
                           GraphBogen(self.graphTerm[0],None,self.graphExpression[2],-1),#4
                           SymbolBogen("-",None,self.graphExpression[6],self.graphExpression[8]),#5 #ist das so richtig Endbogen nur als alternative
                           GraphBogen(self.graphTerm[0],None,self.graphExpression[2],-1),#6
                           GraphBogen(self.graphTerm[0],None,self.graphExpression[2],-1),#7
                           EndBogen(),#8
                           ]
        self.graphTerm = [   GraphBogen(self.graphFactor[0],None,self.graphTerm[1],-1), #0
                        NilBogen(self.graphTerm[2]), #1
                        SymbolBogen("*",None,self.graphTerm[3],self.graphTerm[4]), #2
                        GraphBogen(self.graphFactor[0],None,self.graphTerm[1],-1), #3
                        SymbolBogen("/",None,self.graphTerm[5],self.graphTerm[6]), #4
                        GraphBogen(self.graphFactor[0],None,self.graphTerm[1],-1), #5
                        EndBogen(), #6
                     ]
        self.graphStatement = [  MorphemBogen("ident",None,self.graphStatement[1],self.graphStatement[3]), #0
                            SymbolBogen(":=",None,self.graphStatement[2],-1), #1
                            GraphBogen(self.graphExpression[0],None,self.graphStatement[22],-1), #2 ENDBOGEN?
                            SymbolBogen("IF",None,self.graphStatement[4],self.graphStatement[7]), #3
                            GraphBogen(self.graphCondition[0],None,self.graphStatement[5],-1), #4
                            SymbolBogen("THEN",None,self.graphStatement[6],-1), #5
                            GraphBogen(self.graphStatement[0],None,self.graphStatement[22],-1), #6 ENDBOGEN?
                            SymbolBogen("WHILE",None,self.graphStatement[8],self.graphStatement[11]), #7
                            GraphBogen(self.graphCondition[0],None,self.graphStatement[9],-1), #8
                            SymbolBogen("DO",None,self.graphStatement[10],-1), #9
                            GraphBogen(self.graphStatement[0], None, self.graphStatement[22],-1), #10 ENDBOGEN?
                            SymbolBogen("BEGIN",None,self.graphStatement[12],self.graphStatement[15]), #11
                            GraphBogen(self.graphStatement[0],None, self.graphStatement[13], -1), #12
                            SymbolBogen(";",None,self.graphStatement[12],self.graphStatement[14]), #13
                            SymbolBogen("END",None, self.graphStatement[22],-1), #14 ENDBOGEN?
                            SymbolBogen("CALL",None,self.graphStatement[16],self.graphStatement[17]), #15
                            MorphemBogen("ident",None,self.graphStatement[22],-1), #16 ENDBOGEN?
                            SymbolBogen("?",None, self.graphStatement[18],self.graphStatement[19]), #17
                            MorphemBogen("ident",None, self.graphStatement[22],-1), #18 ENDBOGEN?
                            SymbolBogen("!", None, self.graphStatement[20],self.graphStatement[21]), #19
                            GraphBogen(self.graphExpression[0],None,self.graphStatement[22],-1), #20 ENDBOGEN?
                            NilBogen(self.graphStatement[22]), #21 ENDBOGEN?
                            EndBogen() #22
                          ]
        self.graphCondition = [  SymbolBogen("ODD",None,self.graphCondition[1],self.graphCondition[2]), #0
                            GraphBogen(self.graphExpression[0],None,self.graphCondition[0],-1), #1
                            GraphBogen(self.graphExpression[0],None,self.graphCondition[3],-1), #2
                            SymbolBogen("=",None,self.graphCondition[9],self.graphCondition[4]), #3
                            SymbolBogen("#",None,self.graphCondition[9],self.graphCondition[5]), #4
                            SymbolBogen("<",None,self.graphCondition[9],self.graphCondition[6]), #5
                            SymbolBogen(">",None,self.graphCondition[9],self.graphCondition[7]), #6
                            SymbolBogen("<=",None,self.graphCondition[9],self.graphCondition[8]), #7
                            SymbolBogen(">=",None,self.graphCondition[9],-1), #8
                            GraphBogen(self.graphExpression[0],None,self.graphCondition[10],-1), #9
                            EndBogen() #10
        ]
        self.graphProgramm = [GraphBogen(self.graphBlock[0],None,self.graphProgramm[1],-1), #0
                         SymbolBogen(".",None,self.graphProgramm[2],-1), #1
                         EndBogen() #2
                         ]
    def lexNext(self):
        print("Nachstes token gelext: ")
        while True:
            morph = lexer.lex()
            print(morph.Value)
            if morph.Value != []:
                print("Final gelext: ")
                print(morph.Value)
                return morph


    def pars(self, bogen) -> bool: #ich uebergebe einen Bogen
        #Namensliste: BgD - BogenTyp
                      #MC - MorphemTyp
                      #fx - Funktionspointer
                      #iAlt - Alternativbogen
                      #iNext - Folebogen
                      #BgX - Bogenbeschreibung
        print(type(bogen))
        BogenTypXY = type(bogen)
        print(self.graphBlock[0].Folgebogen)
        pBog = bogen
        succ = False
        morphem = Morph
        print(morphem.Value)
        if morphem.MorphemTyp == None:
            morphem=self.lexNext()

        while True:
            print ("Schleife geentert")
            if pBog.Typ == bogenTyp.BgNil: # done
                print("Nilbogen")
                succ = True
                #return False
            if pBog.Typ == bogenTyp.BgSymbol: # done
                print("Symbolbogen")
                temp = lexer_.token_to_enum[pBog.Bogenbeschreibung].value
                succ = (morphem.Value == temp)
            if pBog.Typ == bogenTyp.BgMorphem: #1/2 done
                print("Morphembogen")
                succ = (morphem.MorphemTyp==pBog.Bogenbeschreibung)
            if pBog.Typ == bogenTyp.BgGraph: # done
                print("Graphbogen")
                #print("Bogenbeschreibung: ")
                #print(type(pBog.Bogenbeschreibung))
                succ = (self.pars(pBog.Bogenbeschreibung))
            if pBog.Typ == bogenTyp.BgEnde:
                print("Endbogen")
                return True

            if (succ and (pBog.Folgefunktion)):
                temp = pBog.Folgefunktion
                print(temp)
                test = type(bogen)
                succ = pBog.Folgefunktion#aufrufen()
            if(not succ):
                if pBog.Alternativbogen != -1:
                    pBog = pBog.Alternativbogen
                else:
                    return False
            else:
                if pBog.Typ == bogenTyp.BgSymbol or pBog.Typ == bogenTyp.BgMorphem:
                    morphem = self.lexNext()
                    pBog = pBog.Folgebogen

input_string = "VAR x, y; BEGIN x := 2; y := x + 3; END."

lexer = lexer_.Lexer(input_string)
def main():
    print(lexer.Test())
    parser = Parse()
    parser.reInit()
    #print(parser.graphProgramm[0])
    Parse.pars(parser, parser.graphProgramm[0])
    #Parse.pars(GraphBogen)
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
