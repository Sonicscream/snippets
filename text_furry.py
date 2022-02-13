def furry(text, percentage = 0.75):
    from random import random as _random
    from random import choice as _choice
    result = ""
    vowels = ['a','e','i','o','u']
    skip = 0
    def getLower(s):
        try:
            return s.lower()
        except:
            pass
        return ''
    def getUpper(s):
        try:
            return s.upper()
        except:
            pass
        return ''
    for index, letter in enumerate(text):
        if skip > 0:
            skip -= 1
        else:
            if _random() < percentage:
                currLetter = letter
                currLetterCaps = True if getUpper(currLetter) in currLetter else False
                prevLetter = None
                prevLetterCaps = None
                if index > 0:
                    prevLetter = text[index-1]
                    prevLetterCaps = True if getUpper(prevLetter) in prevLetter else False
                nextLetter = None
                nextCase = None
                if index < len(text)-1:
                    nextLetter = text[index+1]
                    nextLetterCaps = True if getUpper(nextLetter) in nextLetter else False
                if getLower(currLetter) in 'rl':
                    if currLetterCaps:
                        result += 'W'
                    else:
                        result += 'w'
                elif getLower(currLetter) in 'nm' and getLower(nextLetter) in vowels:
                    result += currLetter + 'Y' if currLetterCaps else 'y'
                elif getLower(currLetter) in 't' and getLower(nextLetter) in 'h':
                    skip+=1
                    result += 'H' if currLetterCaps else 'h'
                else:
                    result += letter
            else:
                result += letter
    return result
