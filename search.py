import re

string = "returns a match where the 10,746 specified charaters are 2,34,456 numbers"


# x = re.search(r"\Areturns",string)                # \A Returns a match if the specified characters are at the beginning of the string
# print(x)
# x = re.search(r"\Athe",string)                     
# print(x)

# x = re.search(r"\bmat",string)                     # \b Returns a match where the specified characters are at the beginning or at the end of a word
# print(x)
# y = re.search(r'\bere',string)
# print(y)
# x = re.search(r'ere\b',string)
# print(x)
# y = re.search(r"mat\b",string)
# print(y)

# x = re.search(r'wh\B',string)                  # \B Returns a match where the specified characters are present,but NOT at the beginning (or at the end) of a word                                  
# print(x)
# x = re.search(r'\Bhe',string)
# print(x)

x = re.search(r"\d",string)                 # \d Returns a match where the string contains digits (numbers from 0-9)
print(x)
x = re.search(r"\D",string)                 # \D  Returns a match where the string DOES NOT contain digits
print(x)

# x = re.search(r"\s",string)                # \s 	Returns a match where the string contains a white space character
# print(x)
# x = re.search(r"\S+",string)                # \S Returns a match where the string DOES NOT contain a white space character
# print(x)

# x = re.search(r'ma\w{3}',string)         #\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# print(x)
# x = re.search(r'\W',string)            #\W Returns a match where the string DOES NOT contain any word characters
# print(x)

# x = re.search(r'numbers\Z',string)         # \Z 	Returns a match if the specified characters are at the end of the string
# print(x)
# x = re.search(r'where\Z',string)
# print(x)

# x = re.findall("[c-l]",string)                # []  A set of characters
# print(x)

# x = re.search("s..ci.i.d",string)          
# print(x)
# x= re.search("cha.*aters",string)          # '.' Any character (except newline character)   ' * 'Zero or more occurrences
# print(x)

# x = re.search("sp.+cif.+ed",string)                          # '+'	One or more occurrences
# print(x)

# x= re.search("^numbers",string)              # '^'	Starts with
# print(x)

# x= re.search("^returns",string) 
# print(x)

# x = re.search("numbers$",string)             # '$' ends with
# print(x)
# x = re.search("charaters$",string)
# print(x)


# x = re.search('c.+a.?at.*rs ',string)         # ? zero or more occurrences    
# if x:
#     print('match found')
# else:
#     print('no match found')
# print(x)

# x = re.search('numb.{2}s',string)            # {} exactly the specified number of occurances
# print(x)
# x = re.search('ch.{2}a.{3}s',string)
# print(x)

# x = re.search('numbers|alphabets',string)       # '|' either or 
# if x:
#     print('match found')
# else:
#     print('no match found')

# x = re.search('alphabets|specialsymbols',string)
# print(x)

