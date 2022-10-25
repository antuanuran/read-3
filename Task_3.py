with open('1.txt', 'rt') as file:
    i = 0
    for z in file:
        res = z.strip()
        i += 1

with open('1.txt', 'rt') as file:
    res_text = file.read()

name_text_1 = "1.txt"
count_str_1 = i
text_1 = res_text


# *************************************************


with open('2.txt', 'rt') as file:
    i = 0
    for z in file:
        res = z.strip()
        i += 1

with open('2.txt', 'rt') as file:
    res_text = file.read()

name_text_2 = "2.txt"
count_str_2 = i
text_2 = res_text


# *************************************************


with open('3.txt', 'rt') as file:
    i = 0
    for z in file:
        res = z.strip()
        i += 1

with open('3.txt', 'rt') as file:
    res_text = file.read()

name_text_3 = "3.txt"
count_str_3 = i
text_3 = res_text

# **********************   Вывод:

list_count = [count_str_1, count_str_2, count_str_3]
list_count.sort()

with open('result.txt', 'w') as a:
    a.write('')

for res in list_count:
    if (res == count_str_1):
        with open('result.txt', 'a') as a:
            a.writelines(f'{name_text_1} \n{str(count_str_1)} \n{text_1}\n\n')

    elif (res == count_str_2):
        with open('result.txt', 'a') as a:
            a.writelines(f'{name_text_2} \n{str(count_str_2)} \n{text_2}\n\n')

    else:
        with open('result.txt', 'a') as a:
            a.writelines(f'{name_text_3} \n{str(count_str_3)} \n{text_3}\n\n')










