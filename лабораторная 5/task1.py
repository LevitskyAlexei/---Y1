# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
dictionaries = [{"bin": bin(x), "dec": x, "oct": oct(x), "hex": hex(x)} for x in range(16)]
pprint(dictionaries)


