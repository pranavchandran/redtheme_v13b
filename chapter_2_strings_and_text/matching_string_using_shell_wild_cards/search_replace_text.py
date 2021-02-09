# replace text in a case sensitive manner
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
# flags = re.findall('python', text, flags=re.IGNORECASE)
# rmv_python = re.sub('python', 'snake', text, flags=re.IGNORECASE)
# print(text)
# print(rmv_python)

# support function
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

match_func = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(match_func)
