import re
import csv

with open('Inbox.mbox', 'r') as file:
    text = file.readlines()
    for t in text:
        if "Your message wasn't delivered to" in t:
            match = re.search(r'[\w\.-]+@[\w\.-]+', t)
            if match:
                email = match.group(0)
                with open('result.txt', 'a+') as file2:
                    file2.write(f'{email}\n')


with open('result.txt', 'r') as result_file:
    result_emails = set(result_file.read().splitlines())

# Чтение данных из base.csv и фильтрация
filtered_rows = []
with open('base.csv', 'r') as base_file:
    reader = csv.DictReader(base_file)
    for row in reader:
        if row['email'] not in result_emails:
            filtered_rows.append(row)

# Запись отфильтрованных данных обратно в base.csv
with open('base.csv', 'w', newline='') as base_file:
    fieldnames = ['company_name', 'email']
    writer = csv.DictWriter(base_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in filtered_rows:
        writer.writerow(row)