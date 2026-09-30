import os
os.system("cls")

# pip install translate

from translate import Translator

# tarjimon = Translator(to_lang='ar', from_lang='uz')
# text = input(">>> ")
# text = tarjimon.translate(text)
# print(text[::-1])

tarjimon = Translator(to_lang='zh', from_lang='uz')
text = input(">>> ")
text = tarjimon.translate(text)
print(text)