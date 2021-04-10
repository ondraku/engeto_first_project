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

separator = "-" * 50

users = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

username = input("Username: ")
password = input("Password: ")

print(separator)

if users.get(username) != password:
    print("You have entered INCORRECT username or password! Please try again...")
    exit()
else:
    print("Welcome to the Text Analyzer app, " + username.title() + "!")
    print("We have 3 texts to be analyzed.")

print(separator)
number = input("Enter a number between 1 and 3 to select: ")
print(separator)

if not number.isdigit() or int(number) < 1 or int (number) > 3:
    print("You have entered an incorrect number or symbol! Please try again...")
    exit()

text = TEXTS[int(number) - 1]
clean_words = [word.strip(',.:/') for word in text.split()]
print("There are " , len(clean_words) , "words in the selected text." )

title_case = 0
upper_case = 0
lower_case = 0
numeric = 0
summary = 0
words_length = dict()

for word in clean_words:
    if word.istitle():
        title_case = title_case + 1
    elif word.isupper():
        upper_case = upper_case + 1
    elif word.islower():
        lower_case = lower_case + 1
    elif word.isdigit():
        numeric = numeric +1
        summary = summary + int(word)

    words_length[len(word)] = words_length.setdefault(len(word), 0) + 1

print("There are ", title_case, "titlecase words.")
print("There are ", upper_case, "uppercase words.")
print("There are ", lower_case, "lower_case words.")
print("There are ", numeric, "numeric strings.")
print("The sum of all the number ", summary)
print(separator)

print("LEN |", "OCCURENCES |", "NR. |")
print(separator)

for index, frequency in enumerate(words_length):
    if index in words_length:
        frequency = words_length.get(index)
        print(index, "*" * frequency, frequency)
print(separator)

print("Process is finished, " + username.title() + "!")