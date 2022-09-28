punc = '''!()-[]{};:'"\,<.>/@#$%^&?*`~'''

string = input("Enter the string: ")

empty_str = ""

for i in string:
     if i not in punc:
        empty_str += i

print(empty_str)
