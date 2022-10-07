import csv

with open('1.txt', encoding='utf8') as file_1:
    f_1 = file_1.readlines()
    len_1 = len(f_1)
with open('2.txt', encoding='utf8', ) as file_2:
    f_2 = file_2.readlines()
    len_2 = len(f_2)

with open('итог.txt', 'w', encoding='utf8') as file_3:
    csv_writer = csv.writer(file_3)
    if len_1 < len_2:
        csv_writer.writerows([['1.txt'], f_1, ['2.txt'], f_2])
    #     не знаю как избавиться от кавычек

    else:
        csv_writer.writerows([['2.txt'], str(len_2), f_2, ['1.txt'], str(len_1)])
        file_3.writelines(f_1)

with open('итог.txt', 'r', encoding='utf8') as file_3:
    f_3 = file_3.readlines()
    print(f_3, )
