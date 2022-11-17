a="Hello World!"

print(a.capitalize())      	#Converts the first character to upper case
#"Hello World!"
print(a.casefold())      	#Converts string into lower case
#"hello world!"
print(a.center(20))      	#Returns a centered string
#"                 Hello World!          "
print(a.count("l"))      	#Returns the number of times a specified value occurs in a string
#3
print(a.encode())      	#Returns an encoded version of the string

# txt = "My name is Ståle"

# x = txt.encode(encoding='utf_8', errors='backslashreplace')

# print(x)

# x = txt.encode(errors='backslashreplace')
# print(x)

# print(a.endswith("s"))      	#Returns true if the string ends with the specified value
# #False
# print(a.endswith("!"))      	#Returns true if the string ends with the specified value
# #True
print(a.expandtabs())      	#Sets the tab size of the string

# txt = 'H\te\t"l\t\'l\t"o'
# #\t  tab \ln new line  \"  "  \' '
# x =  txt.expandtabs(6)

# print(x)

a="Hello World!"
print(a.find())      	#Searches the string for a specified value and returns the position of where it was found
a = "Hello World!"
print(a.find('W')) 
#6

print(a.format())      	#Formats specified values in a string

# txt = "Company7\]\871பிள்யூ~23"

# x = txt.isascii()

# print(x)
# False

# txt = "For only {price:.4f} dollars!"
# print(txt.format(price=49))
# txt = "For only {price:.3f} dollars!"
# print(txt.format(price=49))

# txt = "For only {} dollars!"
# print(txt.format(49))

# txt = "For only {price:.4f} dollars{symbol}!"
# print(txt.format(price=49,symbol="$"))

# txt = "For only {} dollars!{}"
# print(txt.format(49, "$"))
# For only 49.0000 dollars!
# For only 49.000 dollars!
# For only 49 dollars!
# For only 49.0000 dollars$!
# For only 49 dollars!$



print(a.format_map())      	#Formats specified values in a string
print(a.index())      	#Searches the string for a specified value and returns the position of where it was found
print(a.isalnum())      	#Returns True if all characters in the string are alphanumeric
print(a.isalpha())      	#Returns True if all characters in the string are in the alphabet
print(a.isascii())      	#Returns True if all characters in the string are ascii characters
print(a.isdecimal())      	#Returns True if all characters in the string are decimals

# txt = "aas" #unicode for 3

# x = txt.isdecimal()

# print(x)
# False

print(a.isdigit())      	#Returns True if all characters in the string are digits Exponents, like ², are also considered to be a digit.


print(a.isidentifier())      	#Returns True if the string is an identifier
print(a.islower())      	#Returns True if all characters in the string are lower case
print(a.isnumeric())      	#Returns True if all characters in the string are numeric
print(a.isprintable())      	#Returns True if all characters in the string are printable
print(a.isspace())      	#Returns True if all characters in the string are whitespaces
print(a.istitle())      	#Returns True if the string follows the rules of a title
print(a.isupper())      	#Returns True if all characters in the string are upper case
print(a.join())      	#Converts the elements of an iterable into a string
print(a.ljust())      	#Returns a left justified version of the string
print(a.lower())      	#Converts a string into lower case
print(a.lstrip())      	#Returns a left trim version of the string
print(a.maketrans())      	#Returns a translation table to be used in translations
print(a.partition())      	#Returns a tuple where the string is parted into three parts
print(a.replace())      	#Returns a string where a specified value is replaced with a specified value
print(a.rfind())      	#Searches the string for a specified value and returns the last position of where it was found
print(a.rindex())    #	S#earches the string for a specified value and returns the last position of where it was found
print(a.rjust())    #	R#eturns a right justified version of the string
print(a.rpartition())    #	R#eturns a tuple where the string is parted into three parts
print(a.rsplit())    #	S#plits the string at the specified separator, and returns a list
print(a.rstrip())    #	R#eturns a right trim version of the string
print(a.split())    #	Splits the string at the specified separator, and returns a list
print(a.splitlines())    #	Splits the string at line breaks and returns a list
print(a.startswith())    #	Returns true if the string starts with the specified value
print(a.strip())    #	Returns a trimmed version of the string
print(a.swapcase())    #	Swaps cases, lower case becomes upper case and vice versa
print(a.title())    #	Converts the first character of each word to upper case
print(a.translate())    #	Returns a translated string
print(a.upper())    #	Converts a string into upper case
print(a.zfill())    #	Fills the string with a specified number of 0 values at the beginning