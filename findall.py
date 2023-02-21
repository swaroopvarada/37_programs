import re

string = "returns a match where the 10,746 specified charaters are 2,34,456 numbers"


# x = re.findall(r"\Areturns",string)                # \A Returns a match if the specified characters are at the beginning of the string
# print(x)
# x = re.findall(r"\Athe",string)                     
# print(x)

# x = re.findall(r"\bmat",string)                     # \b Returns a match where the specified characters are at the beginning or at the end of a word
# print(x)
# y = re.findall(r'\bere',string)
# print(y)
# x = re.findall(r'ere\b',string)
# print(x)
# y = re.findall(r"mat\b",string)
# print(y)

# x = re.findall(r'h\B',string)                  # \B Returns a match where the specified characters are present,but NOT at the beginning (or at the end) of a word                                  
# print(x)
# x = re.findall(r'\Ba',string)
# print(x)

# x = re.findall(r"\d+",string)                 # \d Returns a match where the string contains digits (numbers from 0-9)
# print(x)
# x = re.findall(r"\D+",string)                 # \D  Returns a match where the string DOES NOT contain digits
# print(x)

# x = re.findall(r"\s",string)                # \s 	Returns a match where the string contains a white space character
# print(x)
# x = re.findall(r"\S+",string)                # \S Returns a match where the string DOES NOT contain a white space character
# print(x)

# x = re.findall(r'\w',string)         #\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# print(x)
# x = re.findall(r'\W',string)            #\W Returns a match where the string DOES NOT contain any word characters
# print(x)

# x = re.findall(r'numbers\Z',string)         # \Z 	Returns a match if the specified characters are at the end of the string
# print(x)
# x = re.findall(r'where\Z',string)
# print(x)

# x = re.findall("[c-l]",string)                    # []  A set of characters
# print(x)

# x = re.findall("s..ci.i.d",string)          
# print(x)
# x= re.findall("cha.*aters",string)          # '.' Any character (except newline character)   ' * 'Zero or more occurrences
# print(x)

# x = re.findall("sp.+cif.+ed",string)                          # '+'	One or more occurrences
# print(x)

# x= re.findall("^numbers",string)              # '^'	Starts with
# print(x)

# x= re.findall("^returns",string) 
# print(x)

# x = re.findall("numbers$",string)             # '$' ends with
# print(x)
# x = re.findall("charaters$",string)
# print(x)


# x = re.findall('c.+a.?at.*rs ',string)         # ? zero or more occurrences    
# print(x)

# x = re.findall('numb.{2}s',string)            # {} exactly the specified number of occurances
# print(x)
# x = re.findall('ch.{2}a.{3}s',string)
# print(x)

# x = re.findall('numbers|alphabets',string)       # '|' either or 
# print(x)
# x = re.findall('alphabets|specialsymbols',string)
# print(x)

