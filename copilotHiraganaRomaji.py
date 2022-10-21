import os
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

#This is the first try at using github Copilot to write the 100% of the code.


# create a dictionari with all the japanese hiragana characters and his romaji equivalents
# this dictionary is used to convert romaji to hiragana
# the name of the dictionary is "romaji2hiragana"
# the keys are the romaji equivalents

romaji2hiraganaVocals = {
    'a': u'\u3042',
    'i': u'\u3044',
    'u': u'\u3046',
    'e': u'\u3048',
    'o': u'\u304a'
}
romaji2hiraganaConsonantsK = {
    'ka': u'\u304b',
    'ki': u'\u304d',
    'ku': u'\u304f',
    'ke': u'\u3051',
    'ko': u'\u3053'
}
romaji2hiraganaConsonantsS = {
    'sa': u'\u3055',
    'shi': u'\u3057',
    'su': u'\u3059',
    'se': u'\u305b',
    'so': u'\u305d'
}
romaji2hiraganaConsonantsT = {
    'ta': u'\u305f',
    'chi': u'\u3061',
    'tsu': u'\u3064',
    'te': u'\u3066',
    'to': u'\u3068'
}
romaji2hiraganaConsonantsN = {
    'na': u'\u306a',
    'ni': u'\u306b',
    'nu': u'\u306c',
    'ne': u'\u306d',
    'no': u'\u306e'
}
romaji2hiraganaConsonantsH = {
    'ha': u'\u306f',
    'hi': u'\u3072',
    'fu': u'\u3075',
    'he': u'\u3078',
    'ho': u'\u307b'
}
romaji2hiraganaConsonantsM = {
    'ma': u'\u307e',
    'mi': u'\u307f',
    'mu': u'\u3080',
    'me': u'\u3081',
    'mo': u'\u3082'
}
romaji2hiraganaConsonantsY = {
    'ya': u'\u3084',
    'yu': u'\u3086',
    'yo': u'\u3088'
}
romaji2hiraganaConsonantsR = {
    'ra': u'\u3089',
    'ri': u'\u308a',
    'ru': u'\u308b',
    're': u'\u308c',
    'ro': u'\u308d'
}
romaji2hiraganaConsonantsW = {
    'wa': u'\u308f',
    'wo': u'\u3092'
}
romaji2hiraganaConsonantsN2 = {
    'n': u'\u3093'
}
romaji2hiraganaConsonantsG = {
    'ga': u'\u304c',
    'gi': u'\u304e',
    'gu': u'\u3050',
    'ge': u'\u3052',
    'go': u'\u3054'
}
romaji2hiraganaConsonantsZ = {
    'za': u'\u3056',
    'ji': u'\u3058',
    'zu': u'\u305a',
    'ze': u'\u305c',
    'zo': u'\u305e'
}
romaji2hiraganaConsonantsD = {
    'da': u'\u3060',
    'ji2': u'\u3062',
    'zu2': u'\u3065',
    'de': u'\u3067',
    'do': u'\u3069'
}
romaji2hiraganaConsonantsB = {
    'ba': u'\u3070',
    'bi': u'\u3073',
    'bu': u'\u3076',
    'be': u'\u3079',
    'bo': u'\u307c'
}
romaji2hiraganaConsonantsP = {
    'pa': u'\u3071',
    'pi': u'\u3074',
    'pu': u'\u3077',
    'pe': u'\u307a',
    'po': u'\u307d'
}

romaji2hiragana = {}
romaji2hiragana.update(romaji2hiraganaVocals)
romaji2hiragana.update(romaji2hiraganaConsonantsK)
romaji2hiragana.update(romaji2hiraganaConsonantsS)
romaji2hiragana.update(romaji2hiraganaConsonantsT)
romaji2hiragana.update(romaji2hiraganaConsonantsN)
romaji2hiragana.update(romaji2hiraganaConsonantsH)
romaji2hiragana.update(romaji2hiraganaConsonantsM)
romaji2hiragana.update(romaji2hiraganaConsonantsY)
romaji2hiragana.update(romaji2hiraganaConsonantsR)
romaji2hiragana.update(romaji2hiraganaConsonantsW)
romaji2hiragana.update(romaji2hiraganaConsonantsN2)
romaji2hiragana.update(romaji2hiraganaConsonantsG)
romaji2hiragana.update(romaji2hiraganaConsonantsZ)
romaji2hiragana.update(romaji2hiraganaConsonantsD)
romaji2hiragana.update(romaji2hiraganaConsonantsB)
romaji2hiragana.update(romaji2hiraganaConsonantsP)


def getHiraganaFromRomaji(hiragana):
    if hiragana in romaji2hiragana:
        return romaji2hiragana[hiragana] 
    else:
        return "The character " + hiragana + " is not a valid hiragana character (not an individual sound).\n"

# Output:call getHiraganaFromRomaji once for each element in the input string
def getHiraganaFromRomajiString(hiraganaString):
    romajiString = ""
    #An important thing to note, is that hiragana chars can be constructed from 3 romajis
    # so first of all we need to check if the first 3 chars are a valid hiragana char, then 2 chars, then 1 char
    for i in range(0, len(hiraganaString)):
        firstThree = hiraganaString[i:i+3]
        firstTwo = hiraganaString[i:i+2]
        firstOne = hiraganaString[i]
        if firstThree in romaji2hiragana:
            romajiString += romaji2hiragana[firstThree] 
            i += 2
        elif firstTwo in romaji2hiragana:
            romajiString += romaji2hiragana[firstTwo] 
            i += 1
        elif firstOne in romaji2hiragana:
            romajiString += romaji2hiragana[firstOne] 
        else:
            romajiString += "The character " + firstOne + " is not a valid hiragana character (not an individual sound).\n"
    return romajiString


def getKeyFromValue(dictionary, value):
    for key in dictionary:
        if dictionary[key] == value:
            return key
    return "The value " + value + " is not a valid value.\n"

def debug():
    clearScreen()
    print("Start the testing!")
    print(getHiraganaFromRomaji('a'))
    print(getHiraganaFromRomaji('b')) 

    print("Printing the sequence 'あいうえお'")
    print(getHiraganaFromRomajiString('あいうえお'))
    
    print("Printing the sequence 'onegai'")
    print(getHiraganaFromRomajiString('onegai')) 
    #needs an update to differentiate between 'g' 'a' and 'ga' (and other sounds who needs more than one character)
    print(getKeyFromValue(romaji2hiragana, u'\u3042'))
    print(getKeyFromValue(romaji2hiragana, 'あ'))