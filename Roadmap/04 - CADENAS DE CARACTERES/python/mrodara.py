#String
mystring = "Hello World"

print(mystring)

#List of words
mylist = mystring.split(" ")
print(mylist)

#List of chars
mylist = [i for i in mystring]
print(mylist)

#Reverse list of chars
print(mystring[::-1])

#Find a word into a string
print(mystring.find("World"))

#Substring
print(mystring[mystring.find("World"):])

string1 = "We are"
string2 = "the champions"

concatenated_string = string1 + " " + string2
print(concatenated_string)

#Upper case
print(concatenated_string.upper())

#Lower case
print(concatenated_string.lower())

#Capitalize
print(concatenated_string.capitalize())

#Title
print(concatenated_string.title())

word1 = "Anilina"
word2 = "Roma"

print(word1[::-1].lower())

print(word1.lower() == word2.lower())

sorted_word1 = sorted(word1.lower())
sorted_word2 = sorted(word2.lower())

print(sorted_word1 == sorted_word2)


def is_isogram(word: str) -> bool:
    result = True
    
    if word == "":
        return False
    
    for letter in word.lower():
        if word.lower().count(letter) > 1:
            result = False
            break
    return result

def is_anagram(word1: str, word2:str) -> bool:
    
    if word1 == "" or word2 == "":
        print("No se puede comparar palabras vacias")
        return False
    
    sorted_word1 = sorted(word1.lower())
    sorted_word2 = sorted(word2.lower())
    
    if sorted_word1 == sorted_word2:
        return True
    else:
        return False
         
def is_palindrome(word1: str, word2: str) -> bool:
    
    if word1 == "" or word2 == "":
        print("No se puede comparar palabras vacias")
        return False
    
    reverse_word1 = word1[::-1]
    reverse_word2 = word2[::-1]
   
    if word1.lower() == reverse_word1.lower() and word2.lower() == reverse_word2.lower():
        return True
    else:
        return False
    
def type_words(word1: str, word2: str):
    
    if word1 == "" or word2 == "":
        print("No se puede comparar palabras vacias")
        return False
    
    if is_anagram(word1=word1, word2=word2): #Anagramas
        return word1 + " y " + word2 + " son anagramas"
    elif is_palindrome(word1=word1, word2=word2):
        return word1 + " y " + word2 + " son palíndromos respectivamente"
    elif is_isogram(word1) and is_isogram(word2):
        print(f"{word1} y {word2} son isogramas respectivamente")
    else:
            print(f"{word1} y {word2} NO son nada de nada entre ellos")
        
print(type_words("Amor", "Roma"))
print(type_words("somos", "Anilina"))
print(type_words("Mucielago", "Frase"))
print(type_words("", "Frase"))



    