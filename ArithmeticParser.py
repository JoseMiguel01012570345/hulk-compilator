from ParserInterface import IExpressionParser
from GrammarDefinition import ArithMeticGrammar,ArithmeticTranslator,ArithmeticNonTerminals,ArithmeticTerminals,ArithmeticProductions
from RegExInterface import IRegEx,State
from GrammarParser import GrammarParser
from GrammarInterface import Grammar

AG = ArithMeticGrammar
parser = GrammarParser(AG,ArithmeticTranslator)

# print(AG.First('P'))

chain = 'a*(n-a^np/(n-a/n)'
index = 0

# while parser.Forward(chain[index]):
#     index += 1
#     pass

parser.Parse(chain)