import re

string = "returns a match where the 10,746 charaters specified  are 2,34,456 numbers"


x = re.sub(r"\Areturns",'player',string)                # \A Returns a match if the specified characters are at the beginning of the string
print(x)
x = re.sub(r"\Athe",' that',string)                     
print(x)

x = re.sub(r"\bmat",'0',string)                     # \b Returns a match where the specified characters are at the beginning or at the end of a word
print(x)
y = re.sub(r'\bere','1',string)
print(y)
x = re.sub(r'ere\b','2',string)
print(x)
y = re.sub(r"mat\b",'3',string)
print(y)

x = re.sub(r'\Bat','8',string)                  # \B Returns a match where the specified characters are present,but NOT at the beginning (or at the end) of a word                                  
print(x)
x = re.sub(r'\Beci','5',string)
print(x)

x = re.sub(r"\d+",'regex',string)                 # \d Returns a match where the string contains digits (numbers from 0-9)
print(x)
x = re.sub(r"\D+",'s',string)                 # \D  Returns a match where the string DOES NOT contain digits
print(x)

x = re.sub(r"\s",'p',string)                # \s 	Returns a match where the string contains a white space character
print(x)
x = re.sub(r"\S+",' 1',string)                # \S Returns a match where the string DOES NOT contain a white space character
print(x)

x = re.sub(r'\w{5}','?',string)         #\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
print(x)
x = re.sub(r'\W+','@',string)            #\W Returns a match where the string DOES NOT contain any word characters
print(x)

x = re.sub(r'numbers\Z','1000',string)         # \Z 	Returns a match if the specified characters are at the end of the string
print(x)
x = re.sub(r'where\Z','4',string)
print(x)

x = re.sub("[c-l]",'Z',string)                 # []  A set of characters
print(x)

x = re.sub("s..ci.i.d",'Q',string)         
print(x)


x= re.sub("cha.+a.+ers",'Last',string)          # '.' Any character (except newline character)   ' * 'Zero or more occurrences
print(x)

x = re.sub("sp.+cif.+ed",'WORD',string)           # '+'	One or more occurrences
print(x)

x= re.sub("^numbers",'Last',string)              # '^'	Starts with
print(x)

x= re.sub("^returns",'0000',string) 
print(x)

x = re.sub("numbers$",'last digit',string)             # '$' ends with
print(x)
x = re.sub("charaters$",'special symbols',string)
print(x)


x = re.sub('c.+a.?at.*rs ','special word',string)         # ? zero or more occurrences    
print(x)

x = re.sub('s.{7}d',' num',string)            # {} exactly the specified number of occurances
print(x)
x = re.sub('ch.{2}a.{3}s','symbols',string)
print(x)

x = re.sub('numbers|alphabets','digits',string)       # '|' either or 
print(x)

x = re.sub('alphabets|charaters',' symbol',string)
print(x)
