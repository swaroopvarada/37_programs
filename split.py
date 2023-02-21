import re

string = "returns a match where the 10746 specified charaters  are 3456 numbers"


x = re.split(r"\Areturns",string)                # \A Returns a match if the specified characters are at the beginning of the string
print(x)
x = re.split(r"\Athe",string)                     
print(x)

x = re.split(r"\bmat",string)                     # \b Returns a match where the specified characters are at the beginning or at the end of a word
print(x)
y = re.split(r'\bere',string)
print(y)
x = re.split(r'ere\b',string)
print(x)
y = re.split(r"mat\b",string)
print(y)

x = re.split(r'wh\B',string)                  # \B Returns a match where the specified characters are present,but NOT at the beginning (or at the end) of a word                                  
print(x)
x = re.split(r'\Barat',string)
print(x)

x = re.split(r"\d+",string)                 # \d Returns a match where the string contains digits (numbers from 0-9)
print(x)
x = re.split(r"\D+",string)                 # \D  Returns a match where the string DOES NOT contain digits
print(x)

x = re.split(r"\s+",string)                # \s 	Returns a match where the string contains a white space character
print(x)
x = re.split(r"\S+",string)                # \S Returns a match where the string DOES NOT contain a white space character
print(x)

x = re.split(r'cha\w{3}',string)         #\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
print(x)
x = re.split(r'\W+',string)            #\W Returns a match where the string DOES NOT contain any word characters
print(x)

x = re.split(r'numbers\Z',string)         # \Z 	Returns a match if the specified characters are at the end of the string
print(x)
x = re.split(r'where\Z',string)
print(x)

x = re.split("[c-l]",string)                    # []  A set of characters
print(x)

x = re.split("s..ci.i.d",string)          # '.' Any character (except newline character) 
print(x)

x= re.split("cha.+at.*rs",string)           # ' * 'Zero or more occurrences
print(x)

x = re.split("sp.+cif.*ed",string)                          # '+'	One or more occurrences
print(x)

x= re.split("^numbers",string)              # '^'	Starts with
print(x)

x= re.split("^returns",string) 
print(x)

x = re.split("numbers$",string)             # '$' ends with
print(x)
x = re.split("charaters$",string)
print(x)

x = re.split('c.+arat.?rs ',string)         # ? zero or more occurrences    
print(x)

x = re.split('nu.{2}ers',string)            # {} exactly the specified number of occurances
print(x)
x = re.split('ch.{2}a.{3}s',string)
print(x)

x = re.split('numbers|alphabets',string)       # '|' either or 
print(x)
x = re.split('alphabets|specialsymbols',string)
print(x)
x = re.split('where|alphabets',string)       
print(x)
