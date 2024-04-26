from pprint import pprint
import csv
import re

# Читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ

def format_phone(phone):
  pattern = r"(\+7|8)*(\d{3})(\d{3})(\d{2})(\d{2})((\s)*(\d{4}))?"
  
  result = re.search(pattern, phone.strip())
  if result:
    formatted_phone = f"+7({result.group(2)}){result.group(3)}-{result.group(4)}-{result.group(5)}"
    if result.group(8):
      formatted_phone += f"{result.group(8)}"
    return formatted_phone
  else:
    return phone

for i in range(len(contacts_list)):
  name = contacts_list[i][:3]
  name = name[:2] + name[2:]
  contacts_list[i][:3] = name
  
  phone = contacts_list[i][5]
  formatted_phone = format_phone(phone)
  contacts_list[i][5] = formatted_phone
  
  for j in range(i+1, len(contacts_list)):
    if contacts_list[i][:3] == contacts_list[j][:3]:
      for k in range(7):
        contacts_list[i][k] = contacts_list[i][k] if contacts_list[i][k] else contacts_list[j][k]
      contacts_list.pop(j)

# TODO 2: сохраните получившиеся данные в другой файл
# Код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list[1:])