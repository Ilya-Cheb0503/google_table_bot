import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Определение области доступа
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Авторизация
creds = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Пользовательское\Dev\freelance\chemical_tutor\project\credentials\divine-climate-413017-03da630bc7ad.json', scope)
client = gspread.authorize(creds)

# Открытие таблицы
# sheet = client.open("test_table").sheet1

sheet = client.open("test_table")
for new_table in sheet:
    new_data = new_table.get('A1:D10')
    print(new_data)

# Получение всех значений
# data = sheet.get_all_records()
# data = sheet.get('A1:D10')  # Данный метод в отличие от предыдущего извлекает данные по-строчно, что в свою очередь
#                             # поможет собирать информацию с таблиц и идентифицировать

# # Вывод данных
# print(data)

# for record in data:
#     print(record)