import re

def get_match(template, text):
    match = re.search(template, text)
    if match == None:
        return 'FAIL'
    else:
        return match[1]

template = r'^(?:\w|\.)+@([a-zA-z]+\.[a-zA-z.]{1,})$'

tests = ['students.spam@yandex.ru', 'example@example', 'example@example.com', 'grgr.gfdvgfs2323__sdkfjbfr@sdfdsfsfrs.fchg', 'gfdv$bd##v32df@itmo.ru']
answers = ['yandex.ru', 'FAIL', 'example.com', 'sdfdsfsfrs.fchg', 'FAIL']

for i in range(len(tests)):
    print("Тест {}:".format(i+1), tests[i])
    print("Ответ:", answers[i])

for i in range(len(tests)):
    match = get_match(template, tests[i])
    print("Вывод программы на тесте {}: {}".format(i+1, match))