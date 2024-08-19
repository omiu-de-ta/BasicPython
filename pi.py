text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
import re
cleaned_string = re.sub(r'[,.]', '', text)
words = cleaned_string.split()
pi=''
for i in list(map(len, words)):
    pi += str(i)
print(pi)
