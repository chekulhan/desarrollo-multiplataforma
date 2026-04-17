#  https://regexr.com/

import re

text = "My phone number is 123-456-7890"

# .search  .match (desde el principio) .findall  
match = re.search(r"\d+", text)
print(match)


text ="Mi gato"
match = re.search("gato", text)
print(match)



text = "Tengo 2 platanos y 1 manzana"
match = re.search(r"\d+", text)
print(match)

text = "Tengo 2 platanos"
x = re.sub(r"\d+", "dos", text)
print(x)

"""
a → matches "a"
. → any character (except newline)

\d → digit (0–9)
\w → word character (letters, digits, _)
\s → whitespace

* → 0 or more
+ → 1 or more
? → 0 or 1
{n} → exactly n
{n,m} → between n and m

^ → start of string
$ → end of string
"""

print(re.search(r"^Hello", "Hello world"))
if re.search(r"world$", "Hello world"):
    print("Word found")
