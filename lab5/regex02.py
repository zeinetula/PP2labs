import re

txt_file = '../test.txt'

with open('test.txt', encoding='utf-8') as file:
    text_to_match = file.read()
    

pattern = r'ab{2,3}'

result = re.findall(pattern, text_to_match, re.IGNORECASE)

if(result):
    print(result)

else:
    print("None")