import re

str = "Мэри любит порты горты, но не любит торты."
matches = re.findall(r'\b(\w*орт\w*)\b', str)

if matches:
    print(*matches[:-1])
else:
    print("Совпадений не найдено.")
