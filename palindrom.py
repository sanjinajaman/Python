



def is_palindrom(word):
     reversed_word=word[: : -1]
     if reversed_word==word:
         return True
     else:
         return False
word=input('Enter any word:')
palindrom=is_palindrom(word)
print(palindrom)


def is_palindrom(word):
    if word == word[:: -1]:
        return True
    return False


word = input('Enter any word:')
palindrom = is_palindrom(word)
print(palindrom)




def is_palindrom(word):
    return word == word[::-1]


word = input('Enter any word:')
palindrom = is_palindrom(word)
print(palindrom)










