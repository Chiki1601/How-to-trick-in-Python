from PyDictionary import PyDictionary

dictionary = PyDictionary()
word =input("Enter the word: ")
meaning = dictionary.meaning(word)
for i in meaning:
    print(f'{i} = {meaning[i]} ')
    print('')
