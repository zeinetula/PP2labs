import re

txt_file = '../test.txt'

with open('test.txt', encoding='utf-8') as file:
    text_to_match = file.read()

pattern = r"[ ,.]"

result = re.sub(pattern, ':', text_to_match)

print(result)