import re

def get_match(template, text):
    match = re.search(template, text)
    if match == None:
        return 'FAIL'
    else:
        return match[0]

template = r'\bВТ\b(\W+)?(\b\w+\b(\W+)?){0,4}(\W+)?\bИТМО\b'

tests = ['А ты знал, что ВТ – лучшая кафедра в ИТМО?', 'ergferger ВТ -   frerf fdf --- dfdf ИТМО  dfghjkhgvf -09', 'ВТ ИТМО', 'ВТ выаыавы ываыва авва вава ааа ИТМО', 'ИТМО ВТ']
answers = ['ВТ – лучшая кафедра в ИТМО', 'ВТ -   frerf fdf --- dfdf ИТМО', 'ВТ ИТМО', 'FAIL', 'FAIL']

for i in range(len(tests)):
    print("Тест {}:".format(i+1), tests[i])
    print("Ответ:", answers[i])

for i in range(len(tests)):
    match = get_match(template, tests[i])
    print("Вывод программы на тесте {}: {}".format(i+1, match))