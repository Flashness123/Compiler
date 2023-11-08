# TODO: implement functions _fslb etc
#leerzeichen other?
# enum und automatentabelel ist durcheinanader - behoben aber was ist mit space
# ich mache noch nichts mit token[0] - behoben
# warum fb so behindert was ist mit zusatnd 2?

#habe endState auf 8 gesetzt
from enum import Enum

class KeyWord(Enum):
        ZNIL = 0

        ZErg = 128
        Zle = 129
        Zge = 130
        ZBGN = 131
        ZCLL = 132
        ZCST = 133
        ZDO = 134
        ZEND = 135
        ZELS = 136
        ZIF = 137
        ZPUT = 138
        ZPRC = 139
        ZTHEN = 140
        ZVAR = 141
        ZWHL = 142

token_to_enum = {
    ":=":KeyWord.ZErg,
    "<":KeyWord.Zle,
    ">":KeyWord.Zge,
    "BEGIN":KeyWord.ZBGN,
    "CALL":KeyWord.ZCLL,
    "CONST":KeyWord.ZCST,
    "DO":KeyWord.ZDO,
    "END":KeyWord.ZEND,
    "ELSE": KeyWord.ZELS,
    "IF": KeyWord.ZIF,
    "PUT": KeyWord.ZPUT,
    "PROCEDURE": KeyWord.ZPRC,
    "THEN": KeyWord.ZTHEN,
    "VAR": KeyWord.ZVAR,
    "WHILE": KeyWord.ZWHL
}
class Morph:
    def __init__(self, MorphemCode, PosLine, PosCol, Value, mpLen):
        self.MorphemCode = MorphemCode
        self.PosLine = PosLine
        self.PosCol = PosCol
        self.Value = Value
        self.mpLen = mpLen


class typeMC(Enum):
    mcSpecial = 0
    mcNumber = 1
    mcSymbol = 2
    mcColon = 3
    mcEqual = 4
    mcSmaller = 5
    mcGreater = 6
    mcOther = 7

class Lexer:
    endState: int = 8
    Line: int = 0
    Col: int = 0
    token: Morph
    currentState: int = 0
    Zeichenklassenvektor = [
        # Other 33mal
        typeMC.mcOther, typeMC.mcOther, typeMC.mcOther, typeMC.mcOther, typeMC.mcOther,
        typeMC.mcOther, typeMC.mcOther, typeMC.mcOther, typeMC.mcOther, typeMC.mcOther,
        typeMC.mcOther, typeMC.mcOther, typeMC.mcOther, typeMC.mcOther, typeMC.mcOther,
        typeMC.mcOther, typeMC.mcOther, typeMC.mcOther, typeMC.mcOther, typeMC.mcOther,
        typeMC.mcOther, typeMC.mcOther, typeMC.mcOther, typeMC.mcOther, typeMC.mcOther,
        typeMC.mcOther, typeMC.mcOther, typeMC.mcOther, typeMC.mcOther, typeMC.mcOther,
        typeMC.mcOther, typeMC.mcOther, typeMC.mcOther,
        # Special 15mal
        typeMC.mcSpecial, typeMC.mcSpecial, typeMC.mcSpecial, typeMC.mcSpecial, typeMC.mcSpecial,
        typeMC.mcSpecial, typeMC.mcSpecial, typeMC.mcSpecial, typeMC.mcSpecial, typeMC.mcSpecial,
        typeMC.mcSpecial, typeMC.mcSpecial, typeMC.mcSpecial, typeMC.mcSpecial, typeMC.mcSpecial,
        # Number 10 mal
        typeMC.mcNumber, typeMC.mcNumber, typeMC.mcNumber, typeMC.mcNumber, typeMC.mcNumber,
        typeMC.mcNumber, typeMC.mcNumber, typeMC.mcNumber, typeMC.mcNumber, typeMC.mcNumber,
        # Colon 1 mal
        typeMC.mcColon,
        # Special 1 mal
        typeMC.mcSpecial,
        # Smaller 1 mal
        typeMC.mcSmaller,
        # Equal 1 mal
        typeMC.mcEqual,
        # Greater 1 mal
        typeMC.mcGreater,
        # 2 mal Special
        typeMC.mcSpecial, typeMC.mcSpecial,
        # 26 mal Symbol
        typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol,
        typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol,
        typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol,
        typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol,
        typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol,
        typeMC.mcSymbol,
        # 6 mal Special
        typeMC.mcSpecial, typeMC.mcSpecial, typeMC.mcSpecial, typeMC.mcSpecial, typeMC.mcSpecial,
        typeMC.mcSpecial,
        # 26 mal Symbol
        typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol,
        typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol,
        typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol,
        typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol,
        typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol, typeMC.mcSymbol,
        typeMC.mcSymbol,
        # 5 mal Special
        typeMC.mcSpecial, typeMC.mcSpecial, typeMC.mcSpecial, typeMC.mcSpecial, typeMC.mcSpecial
    ]
    hashTable = []


    def __init__(self, input):
        self.Expression = input
        self.token = Morph(None, 0, 0, [], 0)  # this has to be done smarter, die nullen mussen geupdatet werden
        keyWords = ["BEGIN", "CALL", "CONST", "DO", "END", "IF", "ODD", "PROCEDURE", "THEN", "VAR", "WHILE"]
        for i in range(len(keyWords)):
            self.hashTable.append(hash(keyWords[i]))


    def Test(self):
        res = []
        for i in range(len(self.Expression)):
            res.append(
                self.Zeichenklassenvektor[ord(self.Expression[i])].value)  # here I either take the mcType or its value
        #print(res)
        return res

    def lex(self) -> Morph:  # gib mir den nachs

        self.currentState = 0
        self.token.Value = []
        self.endState = 8 # wichtig, auch endState wieder auf 9 setzen
        while(self.currentState != self.endState):
            print("the expression is: " + self.Expression)
            if not self.Expression:
                break
            tupel = self.Automatentabelle[self.currentState][self.Zeichenklassenvektor[ord(self.Expression[0])].value]  # currenstate fibt Zeile an,  # Vektor gibt Spalte an  # gibt tupel nachster zustand
            #^ 0 oder 1? 0 funktioniert besser
            exec = tupel[1](self)
            print("Tupel 0: " + str(tupel[0]))
            self.currentState = tupel[0]
            print(exec)

        return self.token #if self.token.Value else None


    def _fslb(self):  #  schreiben,lesen,beenden
        self._fsl()
        self._fb()

    def _fsl(self):# schreiben, lesen
        normal = self.Expression[0]
        print("geschrieben und gelesen: " + normal)
        self.token.Value.append(normal)
        self._fl()

    def _fgl(self): #schreiben als Grossbuchstabe, lesen
        upper = self.Expression[0].upper()
        self.token.Value.append(upper) #hier sollte der char zum token appended werden
        self._fl()

    def _fb(self): #funktion beenden
        print("Jetzt muss ich das token zuruckgeben")
        print(self.token.Value)
        #in python kein switchcase, spater als dictionary map:
        if(self.currentState == 3 or self.currentState == 4 or self.currentState == 5 or self.currentState == 0):
            self.token.MorphemCode = "mcSymb"
            self.token.Value = ord(''.join(self.token.Value))
            #self.token.Value =  unverstandlich, steht doch schon drinnen

        elif self.currentState == 1:
            self.token.MorphemCode = "mcNum"

        elif self.currentState == 2: # ist nur der case fur namen und schlusselwort
            case = self.HashKey(self.token.Value)
            if case != "":
                self.token.MorphemCode = "mcSymb"
                self.token.Value = token_to_enum[case].value
            else :
                self.token.MorphemCode = "mcIdent"
                self.token.Value = str(case)


        elif self.currentState == 6:
            self.token.MorphemCode = "mcSymb"
            self.token.Value = KeyWord.ZErg.value

        elif self.currentState == 7:
            self.token.MorphemCode = "mcSymb"
            self.token.Value = KeyWord.Zle.value

        elif self.currentState == 8:
            self.token.MorphemCode = "mcSymb"
            self.token.Value = KeyWord.Zle.value
        self.endState = 8 #soll das 1 oder 0 sein?



    def _fl(self): #lesen
        print("FL ausgefuhrt")
        char = self.Expression[0]
        if char == '\n':
            self.Line += 1
            self.Col = 0
        else:
            self.Col += 1
        print("Expression wurde ein zeichen abgezogen")
        self.Expression = self.Expression[1:] # spater testen

    Automatentabelle = [
        # Folgezustand
        #SoZei              Ziffer      Buchstabe               :                   =                  <                    >                   Sonst
        [(endState, _fslb), (1, _fsl),  (2,_fgl),           (3, _fsl),          (endState,_fslb),   (4,_fsl),           (5,_fsl),           (1, _fl)],
        [(endState, _fb),   (1, _fsl),  (endState, _fb),    (endState, _fb),    (endState, _fb),    (endState, _fb),    (endState, _fb),    (endState, _fb)],
        [(endState, _fb),   (2, _fsl),  (2, _fgl),          (endState, _fb),    (endState, _fb),    (endState, _fb),    (endState, _fb),    (endState, _fb)],
        [(endState, _fb),   (endState, _fb),(endState, _fb),(endState, _fb),    (6, _fsl),          (endState, _fb),    (endState, _fb),    (endState, _fb)],
        [(endState, _fb),   (endState, _fb),(endState, _fb),(endState, _fb),    (7, _fsl),          (endState, _fb),    (endState, _fb),    (endState, _fb)],
        [(endState, _fb),   (endState, _fb),(endState, _fb),(endState, _fb),    (8, _fsl),          (endState, _fb),    (endState, _fb),    (endState, _fb)],
        [(endState, _fb),   (endState, _fb),(endState, _fb),(endState, _fb),    (endState, _fb),    (endState, _fb),    (endState, _fb),    (endState, _fb)],
        [(endState, _fb),   (endState, _fb),(endState, _fb),(endState, _fb),    (endState, _fb),    (endState, _fb),    (endState, _fb),    (endState, _fb)],
        [(endState, _fb),   (endState, _fb),(endState, _fb),(endState, _fb),    (endState, _fb),    (endState, _fb),    (endState, _fb),    (endState, _fb)]]

    def HashKey(self, array: list):
        arrayToString = "".join(array)
        print("arrayToString: " + arrayToString)
        return arrayToString if hash(arrayToString) in self.hashTable else ""