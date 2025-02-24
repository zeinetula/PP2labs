import re

txt_file = '../test.txt'

with open('test.txt', encoding='utf-8') as file:
    text_to_match = file.read()


pattern = r'a.+b$'

result = re.findall(pattern, text_to_match)

if (result):
    print(result)
else:
    print("None")