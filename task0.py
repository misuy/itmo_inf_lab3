import re


def calc_faces(face, text):
    return(len(re.findall(face, text)))


eyes_dict = {0: ":", 1: ";", 2: "X", 3: "8", 4: "="}
noses_dict = {0: "-", 1: "<", 2: "-{", 3: "<{"}
mouths_dict = {0: "(", 1: ")", 2: "O", 3: "|", 4: "\\", 5: "/", 6: "P"}

print("Введите ваш номер ИСУ:")
ISU_number = int(input())

face = eyes_dict.get(ISU_number % 5) + noses_dict.get(ISU_number % 4) + mouths_dict.get(ISU_number % 7)
print("Ваш смайлик " + face)

tests = ["sedrrfthgjn:-O::----OO:-O:-O12343   !!2 ", "!!:-O:-O ! wfd[]:-O:-O:-O", "Hello world!", "test3))", "aboba: :-O ^^"] 
answers = [3, 5, 0, 0, 1]

for i in range(len(tests)):
    print("Тест {}:".format(i+1), tests[i])
    print("Ответ:", answers[i])

for i in range(len(tests)):
    ans = calc_faces(face, tests[i])
    print("Вывод программы на тесте {}: {}".format(i+1, ans))