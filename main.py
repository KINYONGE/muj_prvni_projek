
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

udaje_uzivatelu = ("bob")
heslo = 123
delka = "-" * 50
uzivatel = input("jake je vase jmeno? ")
heslo2 = input("jake je vas heslo? ")
vyberte_text = input( "jake je cislo sekce ? " )
print( "jmenuji : " + uzivatel)
print( "heslo : " + heslo2 )
print(delka)
if udaje_uzivatelu == uzivatel:
    print(" Vítejte v aplikaci, bobe. Máme 3 texty k analýze.")
    print(delka)
    print("zadejte cislo mezi 1 a 3 vyberte textu : " + vyberte_text)
    print(delka)
elif udaje_uzivatelu != uzivatel:
    print(" omlouvame se, nejste v nasi aplikaci ")
delka = "_" * 54
vyberte_text = TEXTS[0]
number_words = vyberte_text.split()
countWords = 0
for words in number_words:
    if words.count(words):
        countWords += 1
print("Ve vybraném textu je", countWords, "slov.")
count_title2 = 0
for number_title in number_words:
    if number_title.istitle():
        count_title2 += 1
print("Existuje", count_title2, "slov typu titlecase.")
count_upper2 = 0
for count_upper in number_words:
    if count_upper.isupper():
        count_upper2 += 1
print("Je zde", count_upper2, "velké slovo.")
count_lower2 = 0
for count_lower in number_words:
    if count_lower.islower():
        count_lower2 += 1
print("Obsahuje", count_lower2, "malých slov.")
count_numeric2 = 0
for count_numeric in number_words:
    if count_numeric.isnumeric():
        count_numeric2 += 1
print("Existují", count_numeric2, "číselné řetězce.")
sumText1 = int(number_words[2]) + int(number_words[19]) + int(number_words[31])
print("Součet všech čísel", sumText1)

print(delka)
print("LEN", "|", "OCCURENCES", "|", "NR.")
print(delka)
delka2 = 0
delka3 = 0
for number_len_words in number_words:
    if len(number_len_words):
        delka2 += 1
        delka3 = len(number_len_words)
    print(delka2, "|", "*" * len(number_len_words), "|", delka3)